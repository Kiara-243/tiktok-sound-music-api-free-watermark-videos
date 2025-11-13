thonimport argparse
import json
import os
import sys
from typing import Any, Dict, Optional

from cli import main as cli_main

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="TikTok Sound Music API (free-watermark videos) Scraper entrypoint."
    )
    parser.add_argument(
        "--config",
        "-c",
        type=str,
        help="Path to a JSON config file. If omitted, delegates to CLI subcommands.",
    )
    parser.add_argument(
        "--mode",
        "-m",
        type=str,
        choices=["post_list", "search"],
        help="Shortcut to run in a specific mode when using --config.",
    )
    return parser.parse_args()

def load_config(path: str) -> Dict[str, Any]:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Config file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def main() -> None:
    args = parse_args()
    if args.config:
        # When a config file is provided, call CLI with equivalent arguments.
        sys.argv = ["cli.py"]
        sys.argv.extend(["--config", args.config])
        if args.mode:
            sys.argv.extend(["--mode", args.mode])
        cli_main()
    else:
        # No config provided: jump into rich CLI experience.
        cli_main()

if __name__ == "__main__":
    main()