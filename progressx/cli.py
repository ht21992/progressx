from __future__ import annotations

import argparse
import time

from .manager import ProgressManager
from .progress import ProgressBar
from .spinner import Spinner


def demo() -> None:
    with ProgressManager(refresh_rate=0.08) as manager:
        spinner = manager.add(
            Spinner(
                label="Preparing",
            )
        )
        bar1 = manager.add(ProgressBar(total=100, label="Download", color="blue"))
        bar2 = manager.add(ProgressBar(total=60, label="Process", color="REVERSED"))

        for i in range(100):
            spinner.tick()
            if i == 10:
                spinner.succeed("ready")
            bar1.update(1)
            if i < 60:
                bar2.update(1)
            time.sleep(0.05)

        bar1.finish()
        bar2.finish()

    print("Demo complete")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="progressx")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("demo", help="Run the demo progress UI")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "demo":
        demo()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
