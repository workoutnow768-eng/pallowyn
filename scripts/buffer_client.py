"""
Buffer GraphQL client for scheduling video posts.

Uses the current Buffer API (https://api.buffer.com), not the older
graph.buffer.com endpoint / schema that earlier code was written
against -- that mismatch caused persistent 401s even with a valid
token, since a GraphQL request to the wrong host is rejected before
the token is even checked.

Schema notes (per developers.buffer.com):
  - organizations live under `account { organizations { id } }`
  - channels are fetched via `channels(input: { organizationId })`,
    where organizationId is Buffer's custom `OrganizationId` scalar,
    not a plain String (a plain String! variable is rejected with
    GRAPHQL_VALIDATION_FAILED).
  - posts are created via `createPost(input: {...})`, with
    `mode: customScheduled` + `dueAt` for a specific scheduled time,
    and a `video` entry in `assets` for video posts.
"""
import os
import requests

BUFFER_GRAPHQL_URL = "https://api.buffer.com"

def _headers(token_env):
    token = os.environ[token_env]
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

def _post(query, variables, token_env):
    resp = requests.post(
        BUFFER_GRAPHQL_URL,
        headers=_headers(token_env),
        json={"query": query, "variables": variables},
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    if "errors" in data:
        raise RuntimeError(f"Buffer GraphQL error: {data['errors']}")
    return data["data"]

def get_organization_id(token_env):
    query = """
    query GetOrganizations {
      account {
        organizations {
          id
        }
      }
    }
    """
    data = _post(query, {}, token_env)
    orgs = data["account"]["organizations"]
    if not orgs:
        raise ValueError("No organizations found on this Buffer account.")
    return orgs[0]["id"]

def get_channels(token_env):
    organization_id = get_organization_id(token_env)
    query = """
    query GetChannels($organizationId: OrganizationId!) {
      channels(input: { organizationId: $organizationId }) {
        id
        name
        displayName
        service
      }
    }
    """
    data = _post(query, {"organizationId": organization_id}, token_env)
    return data["channels"]

def find_channel_id(channel_name, token_env):
    channels = get_channels(token_env)
    for ch in channels:
        candidates = [ch.get("name"), ch.get("displayName")]
        if any(c and c.lower() == channel_name.lower() for c in candidates):
            return ch["id"], ch["service"]
    raise ValueError(
        f"No Buffer channel found named '{channel_name}'. "
        f"Available: {[(c.get('name'), c.get('displayName')) for c in channels]}"
    )

def create_video_post(channel_name, text, video_url, scheduled_at_iso8601, token_env):
    channel_id, _service = find_channel_id(channel_name, token_env)

    mutation = """
    mutation CreatePost($input: CreatePostInput!) {
      createPost(input: $input) {
        ... on PostActionSuccess {
          post {
            id
          }
        }
        ... on MutationError {
          message
        }
      }
    }
    """
    variables = {
        "input": {
            "text": text,
            "channelId": channel_id,
            "schedulingType": "automatic",
            "mode": "customScheduled",
            "dueAt": scheduled_at_iso8601,
            "assets": [
                {"video": {"url": video_url}}
            ],
        }
    }
    data = _post(mutation, variables, token_env)
    result = data["createPost"]
    if "message" in result:
        raise RuntimeError(f"Buffer error scheduling post to {channel_name}: {result['message']}")
    return result["post"]["id"]
