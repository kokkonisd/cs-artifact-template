#!/usr/bin/env bash

## Perform a partial evaluation on a subset of the benchmark dataset.


set -e

if [ "$#" -ne 1 ]
then
    echo "Usage: $0 OUTPUT_DIR"
    exit 1
fi

output_dir=$1

python3 run_benchmark.py /root/benchmarks/brown_fox.txt /root/evaluation/wordlists/194434-English-Word-List_djvu.txt $output_dir
