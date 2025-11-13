thonfrom __future__ import annotations

from typing import Any, Dict, Iterable, List

from client.tiktok_sound_client import TikTokSoundClient
from models.sound_item import SoundItem
from utils.logging_utils import get_logger

LOGGER = get_logger(__name__)

def run_sound_search(
    client: TikTokSoundClient,
    config: Dict[str, Any],
) -> List[SoundItem]:
    """
    Orchestrates a SEARCH run.

    Expected config keys:
      - type: "SEARCH"
      - keyword: query string
      - region: two-letter region code
      - filterBy: ALL | TITLE | CREATOR
      - sortType: RELEVANCE | MOST_USED | MOST_RECENT | SHORTEST | LONGEST
      - limit: max number of items
    """
    keyword = config.get("keyword")
    region = config.get("region", "GB")
    filter_by = config.get("filterBy", "ALL")
    sort_type = config.get("sortType", "RELEVANCE")
    limit = int(config.get("limit", 20))

    if not keyword:
        raise ValueError("Missing 'keyword' in SEARCH config")

    LOGGER.info(
        "Running sound_search pipeline keyword=%s region=%s filterBy=%s sortType=%s limit=%s",
        keyword,
        region,
        filter_by,
        sort_type,
        limit,
    )

    raw_items: Iterable[Dict[str, Any]] = client.fetch_sounds_by_keyword(
        keyword=keyword,
        region=region,
        filter_by=filter_by,
        sort_type=sort_type,
        limit=limit,
    )
    sounds: List[SoundItem] = [SoundItem.from_raw(item) for item in raw_items]

    LOGGER.info("sound_search pipeline produced %d sound items", len(sounds))
    return sounds