#!/usr/bin/env bash

## Perform the full evaluation from the paper.

set -e


OUTPUT_DIR="/root/evaluation/full-evaluation"
BENCHMARKS_DIR="/root/artifact/benchmarks"

rm -rf "$OUTPUT_DIR"
mkdir -p "$OUTPUT_DIR"

for benchmark in "$BENCHMARKS_DIR"/*
do
    python3 /root/artifact/run-benchmark.py "$benchmark" "$OUTPUT_DIR/"
done
