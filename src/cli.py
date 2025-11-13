thonimport argparse
import json
import os
from typing import Any, Dict, List

from client.tiktok_sound_client import TikTokSoundClient
from pipelines.sound_post_list import run_sound_post_list
from pipelines.sound_search import run_sound_search
from utils.http import HttpClient
from utils.logging_utils import get_logger
from utils.rate_limiter import RateLimiter

LOGGER = get_logger(__name__)

def _load_json_file(path: str) -> Dict[str, Any]:
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def _build_client() -> TikTokSoundClient:
    http_client = HttpClient()
    rate_limiter = RateLimiter(max_calls=5, period_seconds=1.0)
    return TikTokSoundClient(http_client=http_client, rate_limiter=rate_limiter)

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="TikTok Sound Music API (free-watermark videos) Scraper CLI"
    )

    parser.add_argument(
        "--config",
        "-c",
        type=str,
        help="Path to a JSON config file. If provided, used as primary input.",
    )

    subparsers = parser.add_subparsers(dest="command", required=False)

    # post_list command
    post_list_parser = subparsers.add_parser(
        "post-list",
        help="Fetch videos that use a specific TikTok sound/music URL.",
    )
    post_list_parser.add_argument(
        "--url",
        required=False,
        help="TikTok sound/music URL.",
    )
    post_list_parser.add_argument(
        "--region",
        default="GB",
        help="Two-letter region code (e.g. GB, US, VN).",
    )
    post_list_parser.add_argument(
        "--limit",
        type=int,
        default=20,
        help="Maximum number of videos to fetch.",
    )

    # search command
    search_parser = subparsers.add_parser(
        "search",
        help="Search TikTok sounds by keyword.",
    )
    search_parser.add_argument(
        "--keyword",
        required=False,
        help="Keyword to search TikTok sounds.",
    )
    search_parser.add_argument(
        "--region",
        default="GB",
        help="Two-letter region code (e.g. GB, US, VN).",
    )
    search_parser.add_argument(
        "--filterBy",
        default="ALL",
        help="Filter strategy, e.g. ALL, TITLE, CREATOR.",
    )
    search_parser.add_argument(
        "--sortType",
        default="RELEVANCE",
        help="Sort strategy, e.g. RELEVANCE, MOST_USED, MOST_RECENT.",
    )
    search_parser.add_argument(
        "--limit",
        type=int,
        default=20,
        help="Maximum number of sounds to fetch.",
    )

    parser.add_argument(
        "--mode",
        "-m",
        choices=["post_list", "search"],
        help="Explicit mode when using --config (POST_LIST or SEARCH).",
    )

    return parser.parse_args()

def _run_from_config(config: Dict[str, Any], mode: str | None) -> List[Dict[str, Any]]:
    client = _build_client()

    effective_type = config.get("type")
    if mode == "post_list":
        effective_type = "POST_LIST"
    elif mode == "search":
        effective_type = "SEARCH"

    if effective_type == "POST_LIST":
        return [item.to_dict() for item in run_sound_post_list(client, config)]
    elif effective_type == "SEARCH":
        return [item.to_dict() for item in run_sound_search(client, config)]
    else:
        raise ValueError(
            f"Unsupported type '{effective_type}'. Expected 'POST_LIST' or 'SEARCH'."
        )

def _run_post_list(args: argparse.Namespace) -> List[Dict[str, Any]]:
    client = _build_client()
    if not args.url:
        raise ValueError("Missing --url for post-list mode.")
    config = {
        "type": "POST_LIST",
        "url": args.url,
        "region": args.region,
        "limit": args.limit,
    }
    LOGGER.info("Running POST_LIST with config: %s", config)
    return [item.to_dict() for item in run_sound_post_list(client, config)]

def _run_search(args: argparse.Namespace) -> List[Dict[str, Any]]:
    client = _build_client()
    if not args.keyword:
        raise ValueError("Missing --keyword for search mode.")
    config = {
        "type": "SEARCH",
        "keyword": args.keyword,
        "region": args.region,
        "filterBy": args.filterBy,
        "sortType": args.sortType,
        "limit": args.limit,
    }
    LOGGER.info("Running SEARCH with config: %s", config)
    return [item.to_dict() for item in run_sound_search(client, config)]

def main() -> None:
    args = parse_args()

    if args.config:
        config = _load_json_file(args.config)
        results = _run_from_config(config, args.mode)
    else:
        if args.command == "post-list":
            results = _run_post_list(args)
        elif args.command == "search":
            results = _run_search(args)
        else:
            # No command and no config: show help and exit.
            print("No command provided. Use 'post-list' or 'search' subcommands.")
            return

    print(json.dumps(results, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()