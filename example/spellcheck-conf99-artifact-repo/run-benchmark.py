#!/usr/bin/env python3

"""
Run a specific benchmark and evaluate the result (comparing it to a ground-truth
result).
"""

import argparse
import datetime
import os
import subprocess
import sys


SPELLCHECK = os.path.join("/root", "spellcheck", "spellcheck.py")
GROUND_TRUTH = os.path.join("/root", "artifact", "benchmarks", "ground-truth")


def run(benchmark: str, wordlist: str) -> list[list[str]]:
    """Run a specific benchmark with an associated wordlist."""
    result = subprocess.run(
        [sys.executable, SPELLCHECK, wordlist, benchmark],
        capture_output=True,
        text=True,
    ).stdout.rstrip()

    return [pair.split(" -> ") for pair in result.split("\n")]


def evaluate(
    corrections: list[list[str]], benchmark: str
) -> tuple[tuple[int, int], tuple[int, int]]:
    """Evaluate a set of corrections produced by the tool.

    The return value is:
    ```
    (
        (<misspellings detected>, <total misspellings>),
        (<correct spelling fixes>, <total correct spelling fixes>),
    )
    """
    with open(
        os.path.join(GROUND_TRUTH, os.path.basename(benchmark))
    ) as ground_truth_file:
        ground_truth = [
            pair.split(" -> ") for pair in ground_truth_file.read().splitlines()
        ]

    true_misspellings = 0
    true_corrections = 0

    for found_misspelling, found_correction in corrections:
        for actual_misspelling, actual_correction in ground_truth:
            if found_misspelling == actual_misspelling:
                true_misspellings += 1
                if found_correction == actual_correction:
                    true_corrections += 1

    return (
        (true_misspellings, len(ground_truth)),
        (true_corrections, len(ground_truth)),
    )


def main() -> None:
    """Run a benchmark and evaluate it."""
    parser = argparse.ArgumentParser(
        description="Run a single benchmark and evaluate it."
    )
    parser.add_argument("benchmark", help="The benchmark to run.")
    parser.add_argument("wordlist", help="The wordlist to use.")
    parser.add_argument(
        "output_dir",
        help="The directory where the result of the evaluation should be placed.",
    )

    args = parser.parse_args()

    print(
        f"Running benchmark '{args.benchmark}' with wordlist '{args.wordlist}'...",
        file=sys.stderr,
    )

    corrections = run(benchmark=args.benchmark, wordlist=args.wordlist)
    (found_misspellings, total_misspellings), (found_corrections, total_corrections) = (
        evaluate(corrections=corrections, benchmark=args.benchmark)
    )

    benchmark_name = os.path.splitext(os.path.basename(args.benchmark))[0]
    wordlist_name = os.path.splitext(os.path.basename(args.wordlist))[0]
    date = datetime.date.today().strftime("%Y-%m-%d")
    benchmark_file = os.path.join(
        args.output_dir, f"benchmark__{benchmark_name}__{wordlist_name}__{date}.csv"
    )

    with open(benchmark_file, "w") as output_file:
        output_file.write(
            ",".join(
                (
                    "misspellings_detected",
                    "total_misspellings",
                    "misspellings_corrected",
                    "total_corrections",
                )
            )
            + "\n"
        )
        output_file.write(
            ",".join(
                (
                    str(found_misspellings),
                    str(total_misspellings),
                    str(found_corrections),
                    str(total_corrections),
                )
            )
            + "\n"
        )

    print(f"Done! The results can be found in '{benchmark_file}'.", file=sys.stderr)


if __name__ == "__main__":
    main()
