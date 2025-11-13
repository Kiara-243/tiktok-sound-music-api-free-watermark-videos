thonfrom __future__ import annotations

from typing import Any, Dict, Iterable, List

from client.tiktok_sound_client import TikTokSoundClient
from models.video_item import VideoItem
from utils.logging_utils import get_logger

LOGGER = get_logger(__name__)

def run_sound_post_list(
    client: TikTokSoundClient,
    config: Dict[str, Any],
) -> List[VideoItem]:
    """
    Orchestrates a POST_LIST run.

    Expected config keys:
      - type: "POST_LIST"
      - url: TikTok sound/music URL
      - region: two-letter region code
      - limit: max number of items
    """
    sound_url = config.get("url")
    region = config.get("region", "GB")
    limit = int(config.get("limit", 20))

    if not sound_url:
        raise ValueError("Missing 'url' in POST_LIST config")

    LOGGER.info(
        "Running sound_post_list pipeline for url=%s region=%s limit=%s",
        sound_url,
        region,
        limit,
    )

    raw_items: Iterable[Dict[str, Any]] = client.fetch_videos_by_sound(
        url=sound_url, region=region, limit=limit
    )
    videos: List[VideoItem] = [VideoItem.from_raw(item) for item in raw_items]

    LOGGER.info("sound_post_list pipeline produced %d video items", len(videos))
    return videos