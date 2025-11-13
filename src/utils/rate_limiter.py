thonfrom __future__ import annotations

import threading
import time
from typing import Optional

class RateLimiter:
    """
    Simple rate limiter that allows up to `max_calls` within `period_seconds`
    across all threads. When the limit is hit, callers sleep until the window
    resets.

    This is good enough to avoid overly aggressive traffic when scraping.
    """

    def __init__(self, max_calls: int, period_seconds: float) -> None:
        if max_calls <= 0:
            raise ValueError("max_calls must be > 0")
        if period_seconds <= 0:
            raise ValueError("period_seconds must be > 0")

        self.max_calls = max_calls
        self.period_seconds = period_seconds
        self._lock = threading.Lock()
        self._calls = 0
        self._period_start = time.monotonic()

    def acquire(self) -> None:
        """
        Block until a slot is available within the rate window.
        """
        while True:
            with self._lock:
                now = time.monotonic()
                elapsed = now - self._period_start

                if elapsed >= self.period_seconds:
                    # Reset window.
                    self._period_start = now
                    self._calls = 0

                if self._calls < self.max_calls:
                    self._calls += 1
                    return

                # Need to wait for the next period.
                remaining = self.period_seconds - elapsed
                if remaining < 0:
                    remaining = 0.0

            # Sleep outside lock to avoid blocking others.
            time.sleep(remaining or 0.01)