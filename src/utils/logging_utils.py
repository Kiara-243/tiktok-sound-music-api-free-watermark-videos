thonimport logging
import os
from typing import Optional

def _get_log_level() -> int:
    level_name = os.getenv("TIKTOK_SOUND_LOG_LEVEL", "INFO").upper()
    return getattr(logging, level_name, logging.INFO)

def configure_root_logger(level: Optional[int] = None) -> None:
    if level is None:
        level = _get_log_level()

    if logging.getLogger().handlers:
        # Already configured.
        logging.getLogger().setLevel(level)
        return

    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    )

def get_logger(name: str) -> logging.Logger:
    configure_root_logger()
    return logging.getLogger(name)