from __future__ import annotations

import argparse
import sys
from pathlib import Path

from runner.recorder import record
from runner.runner import run


def main() -> int:
    parser = argparse.ArgumentParser(prog="site-runner", description="site-runner — drive a Site through a Journey and capture artifacts for analysis")
    sub = parser.add_subparsers(dest="cmd", required=True)

    run_p = sub.add_parser("run", help="Run a Journey and capture artifacts for a Usability Review or Analytics Data Collection Run")
    run_p.add_argument("journey", type=Path, help="Path to Journey YAML (e.g. sites/redoio/journeys/bias_analysis.yaml)")
    run_p.add_argument(
        "--type",
        dest="run_type",
        choices=["analytics", "usability"],
        default="analytics",
        help="Run Type — determines which analysis pass runs (default: analytics)",
    )
    run_p.add_argument("--out", type=Path, default=None, help="Output directory (default: sites/<slug>/runs/<journey>_<type>_<timestamp>)")
    run_p.add_argument("--headless", action="store_true", help="Run in headless mode")

    rec_p = sub.add_parser("record", help="Record browser interactions into a Journey YAML")
    rec_p.add_argument("url", help="Starting URL to open")
    rec_p.add_argument("output", type=Path, help="Output Journey YAML path (e.g. sites/redoio/journeys/my-flow.yaml)")
    rec_p.add_argument("--role", default="default", help="Role slug to record into the Journey (default: 'default')")
    rec_p.add_argument("--journey", default=None, help="Journey slug (defaults to output filename stem)")
    rec_p.add_argument("--settle-ms", type=int, default=1500, metavar="MS",
                       help="Default settle delay added after each recorded action (default: 1500)")
    rec_p.add_argument("--width", type=int, default=1280, help="Viewport width (default: 1280)")
    rec_p.add_argument("--height", type=int, default=800, help="Viewport height (default: 800)")

    args = parser.parse_args()

    if args.cmd == "run":
        run(args.journey, run_type=args.run_type, out_dir=args.out, headless=args.headless)
        return 0

    if args.cmd == "record":
        record(
            start_url=args.url,
            output_path=args.output,
            journey_slug=args.journey,
            role=args.role,
            viewport_width=args.width,
            viewport_height=args.height,
            default_settle_ms=args.settle_ms,
        )
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
