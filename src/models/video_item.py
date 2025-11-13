thonfrom __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

@dataclass
class AuthorInfo:
    uid: str
    unique_id: str
    nickname: str
    signature: Optional[str] = None
    region: Optional[str] = None
    follower_count: int = 0
    following_count: int = 0
    total_favorited: int = 0
    custom_verify: Optional[str] = None

    @classmethod
    def from_raw(cls, data: Dict[str, Any]) -> "AuthorInfo":
        return cls(
            uid=str(data.get("uid", "")),
            unique_id=str(data.get("unique_id", "")),
            nickname=str(data.get("nickname", "")),
            signature=data.get("signature"),
            region=data.get("region"),
            follower_count=int(data.get("follower_count", 0) or 0),
            following_count=int(data.get("following_count", 0) or 0),
            total_favorited=int(data.get("total_favorited", 0) or 0),
            custom_verify=data.get("custom_verify"),
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "uid": self.uid,
            "unique_id": self.unique_id,
            "nickname": self.nickname,
            "signature": self.signature,
            "region": self.region,
            "follower_count": self.follower_count,
            "following_count": self.following_count,
            "total_favorited": self.total_favorited,
            "custom_verify": self.custom_verify,
        }

@dataclass
class StatisticsInfo:
    play_count: int
    digg_count: int
    comment_count: int
    share_count: int
    collect_count: int

    @classmethod
    def from_raw(cls, data: Dict[str, Any]) -> "StatisticsInfo":
        return cls(
            play_count=int(data.get("play_count", 0) or 0),
            digg_count=int(data.get("digg_count", 0) or 0),
            comment_count=int(data.get("comment_count", 0) or 0),
            share_count=int(data.get("share_count", 0) or 0),
            collect_count=int(data.get("collect_count", 0) or 0),
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "play_count": self.play_count,
            "digg_count": self.digg_count,
            "comment_count": self.comment_count,
            "share_count": self.share_count,
            "collect_count": self.collect_count,
        }

@dataclass
class VideoInfo:
    duration_ms: int
    ratio: str
    play_addr: str
    download_addr: str
    has_watermark: bool

    @classmethod
    def from_raw(cls, data: Dict[str, Any]) -> "VideoInfo":
        return cls(
            duration_ms=int(data.get("duration", 0) or 0),
            ratio=str(data.get("ratio", "")),
            play_addr=str(data.get("play_addr", "")),
            download_addr=str(data.get("download_addr", "")),
            has_watermark=bool(data.get("has_watermark", False)),
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "duration": self.duration_ms,
            "ratio": self.ratio,
            "play_addr": self.play_addr,
            "download_addr": self.download_addr,
            "has_watermark": self.has_watermark,
        }

@dataclass
class VideoItem:
    type: str
    region: str
    url: str
    aweme_id: str
    desc: str
    create_time: int
    author: AuthorInfo
    statistics: StatisticsInfo
    video: VideoInfo
    share_url: str
    share_title: Optional[str] = None
    added_sound_music_info: Optional[Dict[str, Any]] = None
    raw: Dict[str, Any] = field(default_factory=dict, repr=False)

    @classmethod
    def from_raw(cls, data: Dict[str, Any]) -> "VideoItem":
        author_raw = data.get("author", {})
        stats_raw = data.get("statistics", {})
        video_raw = data.get("video", {})
        share_info = data.get("share_info", {})

        return cls(
            type=str(data.get("type", "")),
            region=str(data.get("region", "")),
            url=str(data.get("url", "")),
            aweme_id=str(data.get("aweme_id", "")),
            desc=str(data.get("desc", "")),
            create_time=int(data.get("create_time", 0) or 0),
            author=AuthorInfo.from_raw(author_raw),
            statistics=StatisticsInfo.from_raw(stats_raw),
            video=VideoInfo.from_raw(video_raw),
            share_url=str(share_info.get("share_url", "")),
            share_title=share_info.get("share_title"),
            added_sound_music_info=data.get("added_sound_music_info"),
            raw=data,
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": self.type,
            "region": self.region,
            "url": self.url,
            "aweme_id": self.aweme_id,
            "desc": self.desc,
            "create_time": self.create_time,
            "author": self.author.to_dict(),
            "statistics": self.statistics.to_dict(),
            "video": self.video.to_dict(),
            "share_info": {
                "share_url": self.share_url,
                "share_title": self.share_title,
            },
            "added_sound_music_info": self.added_sound_music_info,
        }