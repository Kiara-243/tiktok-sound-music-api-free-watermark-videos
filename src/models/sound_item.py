thonfrom __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Optional

@dataclass
class SoundItem:
    id: str
    title: str
    author: str
    duration: int
    play_url: str
    cover_large: Optional[str] = None
    cover_medium: Optional[str] = None
    cover_thumb: Optional[str] = None
    user_count: Optional[int] = None
    raw: Dict[str, Any] = field(default_factory=dict, repr=False)

    @classmethod
    def from_raw(cls, data: Dict[str, Any]) -> "SoundItem":
        """
        Build a SoundItem from raw JSON object. The input may come from:
          - added_sound_music_info
          - search_music_result
          - a flattened representation with similar keys
        """
        # Prefer explicit nested keys used in the README.
        added = data.get("added_sound_music_info") or data
        search_info = data.get("search_music_result") or data

        # Decide which portion to use as canonical music object.
        music_data = {}
        if "id" in added and "title" in added:
            music_data = added
        elif "id" in search_info and "title" in search_info:
            music_data = search_info
        else:
            music_data = data

        return cls(
            id=str(music_data.get("id", "")),
            title=str(music_data.get("title", "")),
            author=str(music_data.get("author", "")),
            duration=int(music_data.get("duration", 0) or 0),
            play_url=str(music_data.get("play_url", "")),
            cover_large=music_data.get("cover_large"),
            cover_medium=music_data.get("cover_medium"),
            cover_thumb=music_data.get("cover_thumb"),
            user_count=(
                int(music_data["user_count"]) if "user_count" in music_data else None
            ),
            raw=data,
        )

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert to a JSON-serializable dictionary.
        """
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "duration": self.duration,
            "play_url": self.play_url,
            "cover_large": self.cover_large,
            "cover_medium": self.cover_medium,
            "cover_thumb": self.cover_thumb,
            "user_count": self.user_count,
        }