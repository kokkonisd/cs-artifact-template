#!/usr/bin/env bash

## Perform the full evaluation from the paper.

set -e


OUTPUT_DIR="/root/evaluation/full-evaluation"
BENCHMARKS_DIR="/root/artifact/benchmarks"
WORDLISTS_DIR="/root/artifact/wordlists"

rm -rf "$OUTPUT_DIR"
mkdir -p "$OUTPUT_DIR"

for benchmark in "$BENCHMARKS_DIR"/*.txt
do
    for wordlist in "$WORDLISTS_DIR"/*.txt
    do
        python3 /root/artifact/run-benchmark.py "$benchmark" "$wordlist" "$OUTPUT_DIR"
    done
done
