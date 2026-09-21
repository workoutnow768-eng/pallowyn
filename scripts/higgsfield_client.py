"""
Thin client for Higgsfield's developer REST API, adapted from
dark-fantasy's higgsfield_client.py for the pallowyn/creepvale pipelines.

Difference from dark-fantasy: this account's newer Higgsfield API keys are
issued as a single combined "HIGGSFIELD_API_KEY" secret already shaped as
"<key_id>:<key_secret>" -- so the auth header just uses that value directly
instead of assembling it from two separate env vars.

FIX: per current docs.higgsfield.ai, both image and video endpoints live
under api.higgsfield.ai (not platform.higgsfield.ai) -- the platform.*
host used by the old dark-fantasy code returned HTTP 401 "Invalid
credentials" for this newer key, confirmed via a live GitHub Actions run.
"""
import os
import time
import requests
import concurrent.futures

API_BASE_URL = "https://api.higgsfield.ai"
GENERATE_IMAGE_ENDPOINT = f"{API_BASE_URL}/higgsfield-ai/soul/v2/standard"
GENERATE_VIDEO_ENDPOINT = f"{API_BASE_URL}/minimax/hailuo-2.3/standard/image-to-video"

POLL_INTERVAL_SECONDS = 5
POLL_TIMEOUT_SECONDS = 300


class GenerationBlocked(Exception):
    """Raised when Higgsfield flags a generation as nsfw -- never use the result."""


class GenerationFailed(Exception):
    pass


def _auth_header():
    combined = os.environ["HIGGSFIELD_API_KEY"]
    return {"Authorization": f"Key {combined}"}


def _submit(endpoint, payload):
    resp = requests.post(
        endpoint,
        headers={**_auth_header(), "Content-Type": "application/json", "Accept": "application/json"},
        json=payload,
        timeout=30,
    )
    if not resp.ok:
        raise GenerationFailed(f"HTTP {resp.status_code} from Higgsfield ({endpoint}): {resp.text[:500]}")
    data = resp.json()
    status_url = data.get("status_url")
    if not status_url:
        raise GenerationFailed(f"No status_url in response: {data}")
    return status_url


def poll_until_done(status_url, poll_interval=POLL_INTERVAL_SECONDS, timeout=POLL_TIMEOUT_SECONDS):
    elapsed = 0
    while elapsed < timeout:
        resp = requests.get(status_url, headers=_auth_header(), timeout=30)
        resp.raise_for_status()
        data = resp.json()
        status = data.get("status")
        if status == "completed":
            return data
        if status == "nsfw":
            raise GenerationBlocked(f"Higgsfield flagged this generation as nsfw: {data}")
        if status in ("failed", "canceled"):
            raise GenerationFailed(f"Generation ended in status={status}: {data}")
        time.sleep(poll_interval)
        elapsed += poll_interval
    raise GenerationFailed(f"Timed out after {timeout}s waiting on {status_url}")


def _first_url_in(result, *candidate_keys):
    for key in candidate_keys:
        val = result.get(key)
        if isinstance(val, list) and val:
            item = val[0]
            if isinstance(item, dict) and item.get("url"):
                return item["url"]
            if isinstance(item, str):
                return item
        if isinstance(val, dict) and val.get("url"):
            return val["url"]
        if isinstance(val, str):
            return val
    return None


def download_file(url, out_path):
    resp = requests.get(url, timeout=120)
    resp.raise_for_status()
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "wb") as f:
        f.write(resp.content)
    return out_path


def generate_image(prompt, out_path, aspect_ratio="9:16", resolution="1080p", max_retries=2):
    last_err = None
    for attempt in range(max_retries):
        try:
            status_url = _submit(GENERATE_IMAGE_ENDPOINT, {
                "prompt": prompt, "aspect_ratio": aspect_ratio, "resolution": resolution,
            })
            result = poll_until_done(status_url)
            image_url = _first_url_in(result, "images", "image", "outputs")
            if not image_url:
                raise GenerationFailed(f"Completed but no image url in payload: {result}")
            download_file(image_url, out_path)
            return out_path, image_url
        except GenerationBlocked:
            raise
        except (GenerationFailed, requests.RequestException) as e:
            last_err = e
            time.sleep(3)
    raise GenerationFailed(f"Failed after {max_retries} attempts: {last_err}")


def generate_video_from_image(prompt, image_url, out_path, duration=6, max_retries=2):
    last_err = None
    for attempt in range(max_retries):
        try:
            status_url = _submit(GENERATE_VIDEO_ENDPOINT, {
                "prompt": prompt,
                "image_url": image_url,
                "duration": duration,
                "prompt_optimizer": False,
            })
            result = poll_until_done(status_url)
            video_url = _first_url_in(result, "videos", "video", "outputs")
            if not video_url:
                raise GenerationFailed(f"Completed but no video url in payload: {result}")
            download_file(video_url, out_path)
            return out_path
        except GenerationBlocked:
            raise
        except (GenerationFailed, requests.RequestException) as e:
            last_err = e
            time.sleep(3)
    raise GenerationFailed(f"Failed after {max_retries} attempts: {last_err}")


def generate_one_post(scene, out_dir):
    still_path = os.path.join(out_dir, "still.png")
    video_path = os.path.join(out_dir, "video_silent.mp4")

    _, image_url = generate_image(scene["still_prompt"], still_path)
    generate_video_from_image(scene["animate_prompt"], image_url, video_path)

    return {"still_path": still_path, "video_path": video_path}


def generate_posts_concurrent(scenes, out_dirs, max_workers=3):
    results = [None] * len(scenes)
    errors = [None] * len(scenes)

    def _run_one(index, scene, out_dir):
        try:
            return index, generate_one_post(scene, out_dir), None
        except (GenerationBlocked, GenerationFailed) as e:
            return index, None, e

    if not scenes:
        return results, errors

    with concurrent.futures.ThreadPoolExecutor(max_workers=min(max_workers, len(scenes))) as pool:
        futures = [pool.submit(_run_one, i, scenes[i], out_dirs[i]) for i in range(len(scenes))]
        for future in concurrent.futures.as_completed(futures):
            index, result, err = future.result()
            results[index] = result
            errors[index] = err

    return results, errors
