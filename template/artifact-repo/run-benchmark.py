#!/usr/bin/env python3

"""
Run a specific benchmark and evaluate the result (comparing it to a ground-truth
result).
"""

import argparse
import sys


def main() -> None:
    """Run a benchmark and evaluate it."""
    parser = argparse.ArgumentParser(
        description="Run a single benchmark and evaluate it."
    )
    parser.add_argument("benchmark", help="The benchmark to run.")
    parser.add_argument(
        "output_dir",
        help="The directory where the result of the evaluation should be placed.",
    )

    args = parser.parse_args()

    print(
        f"Running benchmark '{args.benchmark}' with wordlist '{args.wordlist}'...",
        file=sys.stderr,
    )

    # TODO: implement

    print(f"Done! The results can be found in '{output_dir}'.", file=sys.stderr)


if __name__ == "__main__":
    main()
