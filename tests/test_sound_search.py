thonfrom typing import Any, Dict, List

from pipelines.sound_search import run_sound_search
from models.sound_item import SoundItem

class DummyClient:
    def __init__(self, items: List[Dict[str, Any]]):
        self._items = items

    def fetch_sounds_by_keyword(
        self,
        keyword: str,
        region: str,
        filter_by: str = "ALL",
        sort_type: str = "RELEVANCE",
        limit: int = 20,
    ):
        # Ignore parameters for this dummy client and return sample items.
        return self._items[:limit]

def _sample_search_items() -> List[Dict[str, Any]]:
    return [
        {
            "search_music_result": {
                "id": "1234567890",
                "title": "Love You So",
                "author": "King Khan & BBQ Show",
                "duration": 120,
                "play_url": "https://example-cdn.tiktok.com/music/1234567890.mp3",
                "cover_large": "https://example-cdn.tiktok.com/cover/large2.jpg",
                "cover_medium": "https://example-cdn.tiktok.com/cover/medium2.jpg",
                "cover_thumb": "https://example-cdn.tiktok.com/cover/thumb2.jpg",
                "user_count": 98765
            }
        }
    ]

def test_run_sound_search_produces_sound_items():
    raw_items = _sample_search_items()
    client = DummyClient(raw_items)
    config = {
        "type": "SEARCH",
        "keyword": "Love You So",
        "region": "GB",
        "filterBy": "ALL",
        "sortType": "RELEVANCE",
        "limit": 5,
    }

    sounds = run_sound_search(client, config)
    assert isinstance(sounds, list)
    assert len(sounds) == 1
    sound = sounds[0]
    assert isinstance(sound, SoundItem)
    assert sound.title == "Love You So"
    assert sound.author == "King Khan & BBQ Show"
    assert sound.user_count == 98765