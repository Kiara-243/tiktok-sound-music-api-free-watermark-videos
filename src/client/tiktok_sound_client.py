thonfrom __future__ import annotations

from typing import Any, Dict, List, Optional
from urllib.parse import urlencode, urljoin

from utils.http import HttpClient, HttpRequestError
from utils.logging_utils import get_logger
from utils.rate_limiter import RateLimiter

LOGGER = get_logger(__name__)

class TikTokSoundClient:
    """
    Lightweight HTTP client that talks to TikTok (or an upstream proxy/actor)
    to fetch sound-based video lists and music search results.

    The concrete API paths are intentionally generic so this client can be
    used with a custom proxy or Apify actor that mimics TikTok's API shape.
    """

    def __init__(
        self,
        http_client: Optional[HttpClient] = None,
        base_url: str = "https://www.tiktok.com/api/",
        rate_limiter: Optional[RateLimiter] = None,
    ) -> None:
        self.http_client = http_client or HttpClient()
        if not base_url.endswith("/"):
            base_url = base_url + "/"
        self.base_url = base_url
        self.rate_limiter = rate_limiter

    def _throttle(self) -> None:
        if self.rate_limiter:
            self.rate_limiter.acquire()

    def _request_json(self, path: str, params: Dict[str, Any]) -> Dict[str, Any]:
        self._throttle()
        url = urljoin(self.base_url, path)
        try:
            LOGGER.debug("Requesting URL %s with params %s", url, params)
            return self.http_client.get_json(url, params=params)
        except HttpRequestError as exc:
            LOGGER.error("HTTP request failed: %s", exc, exc_info=True)
            raise

    def fetch_videos_by_sound(
        self,
        url: str,
        region: str,
        limit: int = 20,
    ) -> List[Dict[str, Any]]:
        """
        Fetch videos that use a given TikTok sound/music URL.

        This method assumes a proxy endpoint that accepts 'sound_url', 'region',
        and 'limit' as query parameters and responds with a JSON object
        containing a 'results' array of video entries.
        """
        query = {
            "sound_url": url,
            "region": region,
            "limit": limit,
        }
        LOGGER.info(
            "Fetching videos for sound_url=%s region=%s limit=%s", url, region, limit
        )
        response = self._request_json("music/post_list/", query)
        results = response.get("results", [])
        if not isinstance(results, list):
            LOGGER.warning("Unexpected response shape: 'results' is not a list")
            return []
        LOGGER.info("Fetched %d video entries", len(results))
        return results

    def fetch_sounds_by_keyword(
        self,
        keyword: str,
        region: str,
        filter_by: str = "ALL",
        sort_type: str = "RELEVANCE",
        limit: int = 20,
    ) -> List[Dict[str, Any]]:
        """
        Search TikTok sounds by keyword.

        Assumes an upstream endpoint that accepts 'keyword', 'region',
        'filterBy', 'sortType', and 'limit' and returns a JSON object with a
        'results' array of sound entries.
        """
        query = {
            "keyword": keyword,
            "region": region,
            "filterBy": filter_by,
            "sortType": sort_type,
            "limit": limit,
        }
        LOGGER.info(
            "Searching sounds keyword=%s region=%s filterBy=%s sortType=%s limit=%s",
            keyword,
            region,
            filter_by,
            sort_type,
            limit,
        )
        response = self._request_json("music/search/", query)
        results = response.get("results", [])
        if not isinstance(results, list):
            LOGGER.warning("Unexpected response shape: 'results' is not a list")
            return []
        LOGGER.info("Fetched %d sound entries", len(results))
        return results

    def build_query_string(self, params: Dict[str, Any]) -> str:
        """
        Utility to build a canonical query string for logging or debugging.
        """
        return urlencode(params, doseq=True)