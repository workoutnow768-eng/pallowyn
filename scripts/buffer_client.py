"""
Buffer GraphQL client for scheduling video posts, same pattern as
dark-fantasy's buffer_client.py.
"""
import os
import requests

BUFFER_GRAPHQL_URL = "https://graph.buffer.com"

_VIDEO_METADATA_BY_SERVICE = {
    "instagram": lambda: {"instagram": {"type": "reel", "shouldShareToFeed": True}},
    "facebook": lambda: {"facebook": {"type": "reel"}},
}


def _headers(token_env):
    token = os.environ[token_env]
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}


def get_channels(token_env):
    query = """
    query {
      organizations {
        id
        channels {
          id
          name
          service
        }
      }
    }
    """
    resp = requests.post(BUFFER_GRAPHQL_URL, headers=_headers(token_env), json={"query": query}, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    channels = []
    for org in data.get("data", {}).get("organizations", []):
        channels.extend(org.get("channels", []))
    return channels


def find_channel_id(channel_name, token_env):
    channels = get_channels(token_env)
    for ch in channels:
        if ch["name"] == channel_name or ch["name"].lower() == channel_name.lower():
            return ch["id"], ch["service"]
    raise ValueError(f"No Buffer channel found named '{channel_name}'. Available: {[c['name'] for c in channels]}")


def create_video_post(channel_name, text, video_url, scheduled_at_iso8601, token_env):
    channel_id, service = find_channel_id(channel_name, token_env)

    metadata = {}
    if service in _VIDEO_METADATA_BY_SERVICE:
        metadata = _VIDEO_METADATA_BY_SERVICE[service]()

    mutation = """
    mutation CreatePost($input: CreatePostInput!) {
      createPost(input: $input) {
        id
      }
    }
    """
    variables = {
        "input": {
            "channelId": channel_id,
            "text": text,
            "assets": [{"video": {"url": video_url}}],
            "scheduledAt": scheduled_at_iso8601,
            "metadata": metadata,
        }
    }
    resp = requests.post(
        BUFFER_GRAPHQL_URL,
        headers=_headers(token_env),
        json={"query": mutation, "variables": variables},
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    if "errors" in data:
        raise RuntimeError(f"Buffer error scheduling post to {channel_name}: {data['errors']}")
    return data["data"]["createPost"]["id"]
