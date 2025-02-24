#!/usr/bin/env bash

## Perform a partial evaluation on a subset of the benchmark dataset.

set -e


OUTPUT_DIR="/root/evaluation/reduced-evaluation/"
BENCHMARKS_DIR="/root/artifact/benchmarks"
TARGET_BENCHMARKS=("$BENCHMARKS_DIR/A" "$BENCHMARKS_DIR/B")

rm -rf "$OUTPUT_DIR"
mkdir -p "$OUTPUT_DIR"

for benchmark in "${TARGET_BENCHMARKS[@]}"
do
    python3 /root/artifact/run-benchmark.py "$benchmark" "$OUTPUT_DIR"
done
