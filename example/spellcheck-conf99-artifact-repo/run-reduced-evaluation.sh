#!/usr/bin/env bash

## Perform a partial evaluation on a subset of the benchmark dataset.

set -e


OUTPUT_DIR="/root/evaluation/reduced-evaluation/"
BENCHMARKS_DIR="/root/artifact/benchmarks"
WORDLISTS_DIR="/root/artifact/wordlists"

rm -rf "$OUTPUT_DIR"
mkdir -p "$OUTPUT_DIR"

python3 /root/artifact/run-benchmark.py \
    "$BENCHMARKS_DIR/brown_fox.txt" \
    "$WORDLISTS_DIR/194434-English-Word-List_djvu.txt" \
    "$OUTPUT_DIR"
