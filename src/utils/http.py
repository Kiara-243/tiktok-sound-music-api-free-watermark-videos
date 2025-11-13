thonfrom __future__ import annotations

import json
from typing import Any, Dict, Optional

import requests

from .logging_utils import get_logger

LOGGER = get_logger(__name__)

class HttpRequestError(RuntimeError):
    """Raised when an HTTP request fails or returns an unexpected response."""

class HttpClient:
    """
    Minimal wrapper around requests to centralize JSON handling and logging.
    """

    def __init__(self, timeout: float = 15.0) -> None:
        self.timeout = timeout

    def get_json(
        self,
        url: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        hdrs = {
            "User-Agent": (
                "Mozilla/5.0 (compatible; TikTokSoundMusicAPI/0.1; +https://bitbash.dev)"
            ),
            "Accept": "application/json,text/plain,*/*",
        }
        if headers:
            hdrs.update(headers)

        LOGGER.debug("GET %s params=%s headers=%s", url, params, hdrs)
        try:
            resp = requests.get(url, params=params, headers=hdrs, timeout=self.timeout)
        except requests.RequestException as exc:
            raise HttpRequestError(f"HTTP GET failed for {url}: {exc}") from exc

        if not resp.ok:
            raise HttpRequestError(
                f"HTTP GET {url} failed with status {resp.status_code}: {resp.text[:200]}"
            )

        try:
            return resp.json()
        except json.JSONDecodeError as exc:
            raise HttpRequestError(
                f"Failed to parse JSON response from {url}: {exc}"
            ) from exc