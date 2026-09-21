"""
Two-phase orchestrator for the pallowyn (Halloween/Spooky Seasonal) video
pipeline, adapted from dark-fantasy's main.py. Usage:

    python scripts/main.py generate    # still -> video -> mux music
    python scripts/main.py schedule    # read manifest -> schedule on Buffer

Run via GitHub Actions (.github/workflows/daily-post.yml).
"""
import os
import sys
import json
import time
import datetime

sys.path.insert(0, os.path.dirname(__file__))

import higgsfield_client
import mux_audio
import buffer_client
from scene_bank import SCENES

STATE_PATH = os.path.join(os.path.dirname(__file__), "..", "state", "pallowyn_state.json")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output", "pallowyn")
MANIFEST_PATH = os.path.join(OUTPUT_DIR, "manifest.json")

# Buffer channels on this niche's account: "pallowyn" (TikTok), "durantale"
# (Instagram), "Haloween" (YouTube) -- all three confirmed connected, just
# named differently from each other since they were set up separately.
CHANNELS = ["pallowyn", "durantale", "Haloween"]
BUFFER_TOKEN_ENV = "BUFFER_API"
MUSIC_TRACK_URL_ENV = "MUSIC_TRACK_URL"

HASHTAGS = "#halloween #spookyseason #jackolantern #autumnvibes #aiart"
CAPTION = ""  # silent-visual page, no captions, same as dark-fantasy

# raw.githubusercontent.com can lag a few seconds behind a push, so a
# freshly-committed video URL can 404 if Buffer fetches it immediately.
# Retry with backoff instead of failing the whole run over a transient miss.
SCHEDULE_MAX_RETRIES = 4
SCHEDULE_RETRY_DELAY_SECONDS = 15

def load_state():
    with open(STATE_PATH, "r") as f:
        return json.load(f)

def save_state(state):
    with open(STATE_PATH, "w") as f:
        json.dump(state, f, indent=2)

def download_music_track(out_path):
    import requests
    url = os.environ[MUSIC_TRACK_URL_ENV]
    resp = requests.get(url, timeout=120)
    resp.raise_for_status()
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "wb") as f:
        f.write(resp.content)
    return out_path

def cmd_generate():
    state = load_state()
    posts_per_day = state.get("posts_per_day", 3)
    last_index = state.get("last_scene_index", 0)

    scenes = []
    indices = []
    for i in range(posts_per_day):
        idx = (last_index + i) % len(SCENES)
        scenes.append(SCENES[idx])
        indices.append(idx)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_dirs = [os.path.join(OUTPUT_DIR, f"post_{i}") for i in range(posts_per_day)]

    print(f"[OK] Generating {posts_per_day} scenes: {[s['title'] for s in scenes]}")
    results, errors = higgsfield_client.generate_posts_concurrent(scenes, out_dirs, max_workers=3)

    for i, err in enumerate(errors):
        if err is not None:
            print(f"[ERROR] Scene {indices[i]} ('{scenes[i]['title']}') failed: {err}")

    if all(r is None for r in results):
        raise SystemExit("[SAFETY] All scenes failed generation -- aborting run, nothing to schedule.")

    music_path = os.path.join(OUTPUT_DIR, "music_track.mp3")
    download_music_track(music_path)
    track_duration = mux_audio.get_audio_duration(music_path)
    print(f"[OK] Music track duration: {track_duration:.1f}s")

    offset = mux_audio.next_offset(state, track_duration)

    manifest = []
    daily_slots = state.get("daily_time_slots_uk", ["09:00", "15:00", "19:00"])
    scheduled_up_to = datetime.datetime.fromisoformat(state["scheduled_up_to"].replace("Z", "+00:00"))

    for i, result in enumerate(results):
        if result is None:
            continue
        final_path = os.path.join(out_dirs[i], "final.mp4")
        mux_audio.mux(result["video_path"], music_path, offset, final_path)
        offset += mux_audio.CLIP_DURATION_SECONDS
        if offset >= track_duration:
            offset = 0.0

        scheduled_up_to = scheduled_up_to + datetime.timedelta(hours=6)
        manifest.append({
            "scene_index": indices[i],
            "title": scenes[i]["title"],
            "final_path": final_path,
            "scheduled_at": scheduled_up_to.isoformat().replace("+00:00", "Z"),
        })
        print(f"[OK] Scene {indices[i]} ('{scenes[i]['title']}') ready -> {final_path}")

    with open(MANIFEST_PATH, "w") as f:
        json.dump(manifest, f, indent=2)

    state["last_scene_index"] = (last_index + posts_per_day) % len(SCENES)
    state["music_offset_seconds"] = offset
    state["scheduled_up_to"] = scheduled_up_to.isoformat().replace("+00:00", "Z")
    state["last_run_at"] = datetime.datetime.utcnow().isoformat() + "Z"
    state["last_run_slot"] = "github_actions_autonomous_bot"
    save_state(state)

    if not manifest:
        raise SystemExit("[SAFETY] No posts were successfully generated -- aborting before schedule step.")

def _schedule_with_retry(channel, text, video_url, scheduled_at, token_env):
    last_err = None
    for attempt in range(SCHEDULE_MAX_RETRIES):
        try:
            return buffer_client.create_video_post(
                channel_name=channel,
                text=text,
                video_url=video_url,
                scheduled_at_iso8601=scheduled_at,
                token_env=token_env,
            )
        except Exception as e:
            last_err = e
            if attempt < SCHEDULE_MAX_RETRIES - 1:
                print(f"[WARN] Buffer schedule attempt {attempt + 1} failed ({e}); "
                      f"retrying in {SCHEDULE_RETRY_DELAY_SECONDS}s (raw.githubusercontent.com "
                      f"may not have caught up to the push yet)")
                time.sleep(SCHEDULE_RETRY_DELAY_SECONDS)
    raise last_err

def cmd_schedule():
    if not os.path.exists(MANIFEST_PATH):
        print("[OK] No manifest found -- nothing to schedule (generate step may have failed).")
        return

    with open(MANIFEST_PATH, "r") as f:
        manifest = json.load(f)

    repo = os.environ.get("GITHUB_REPOSITORY", "workoutnow768-eng/pallowyn")
    branch = "main"

    for entry in manifest:
        rel_path = os.path.relpath(entry["final_path"], os.path.join(os.path.dirname(__file__), ".."))
        rel_path = rel_path.replace("\\", "/")
        video_url = f"https://raw.githubusercontent.com/{repo}/{branch}/{rel_path}"

        for channel in CHANNELS:
            try:
                post_id = _schedule_with_retry(
                    channel=channel,
                    text=f"{CAPTION} {HASHTAGS}".strip(),
                    video_url=video_url,
                    scheduled_at=entry["scheduled_at"],
                    token_env=BUFFER_TOKEN_ENV,
                )
                print(f"[OK] Scheduled '{entry['title']}' to {channel} at {entry['scheduled_at']} (post id {post_id})")
            except Exception as e:
                print(f"[ERROR] Failed to schedule '{entry['title']}' to {channel}: {e}")

    os.remove(MANIFEST_PATH)

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in ("generate", "schedule"):
        print("Usage: python scripts/main.py [generate|schedule]")
        sys.exit(1)

    if sys.argv[1] == "generate":
        cmd_generate()
    else:
        cmd_schedule()
