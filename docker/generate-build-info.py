import argparse
import json
from datetime import UTC, datetime
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Generate build metadata for app static assets.")
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--branch", required=True)
    parser.add_argument("--commit", required=True)
    args = parser.parse_args()

    build_info = {
        "branch": args.branch,
        "commit": args.commit,
        "date": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(build_info, indent=2) + "\n", encoding="utf-8")
    print(f"Generated build info in {args.output}")


if __name__ == "__main__":
    main()
