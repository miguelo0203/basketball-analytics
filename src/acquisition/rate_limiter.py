"""Token bucket rate limiter respecting source-level access policies."""

import time
import threading
from typing import Dict


class RateLimiter:
    """Thread-safe rate limiter ensuring request caps per minute."""

    def __init__(self, requests_per_minute: int = 20):
        self.rate = requests_per_minute
        self.interval = 60.0 / max(requests_per_minute, 1)
        self.lock = threading.Lock()
        self.last_request_time = 0.0

    def wait(self) -> None:
        with self.lock:
            now = time.time()
            elapsed = now - self.last_request_time
            if elapsed < self.interval:
                sleep_time = self.interval - elapsed
                time.sleep(sleep_time)
            self.last_request_time = time.time()


# Global source rate limiter instances
SOURCE_LIMITERS: Dict[str, RateLimiter] = {
    "SRC_FIBA_ARCHIVE": RateLimiter(requests_per_minute=30),
    "SRC_FIBA_MODERN": RateLimiter(requests_per_minute=20),
    "SRC_FIBA_LIVESTATS": RateLimiter(requests_per_minute=20),
    "SRC_BREF": RateLimiter(requests_per_minute=20),
    "SRC_FEB": RateLimiter(requests_per_minute=20),
    "SRC_IOC": RateLimiter(requests_per_minute=10),
}


def get_limiter(source_id: str) -> RateLimiter:
    """Get or create rate limiter for source."""
    if source_id not in SOURCE_LIMITERS:
        SOURCE_LIMITERS[source_id] = RateLimiter(requests_per_minute=20)
    return SOURCE_LIMITERS[source_id]
