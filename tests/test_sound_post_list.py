thonimport json
import os
from typing import Any, Dict, List

from pipelines.sound_post_list import run_sound_post_list
from models.video_item import VideoItem

class DummyClient:
    def __init__(self, items: List[Dict[str, Any]]):
        self._items = items

    def fetch_videos_by_sound(self, url: str, region: str, limit: int = 20):
        # Ignore parameters in this dummy implementation and just return samples.
        return self._items[:limit]

def _load_sample_output() -> List[Dict[str, Any]]:
    base_dir = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(base_dir, "data", "sample_output.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def test_run_sound_post_list_produces_video_items():
    raw_items = _load_sample_output()
    client = DummyClient(raw_items)
    config = {
        "type": "POST_LIST",
        "url": raw_items[0]["url"],
        "region": raw_items[0]["region"],
        "limit": 10,
    }

    videos = run_sound_post_list(client, config)
    assert isinstance(videos, list)
    assert len(videos) == 1
    video = videos[0]
    assert isinstance(video, VideoItem)
    assert video.aweme_id == raw_items[0]["aweme_id"]
    assert video.author.nickname == raw_items[0]["author"]["nickname"]
    assert video.statistics.play_count == raw_items[0]["statistics"]["play_count"]