#!/usr/bin/env bash

## Perform the full evaluation from the paper.


set -e

if [ "$#" -ne 1 ]
then
    echo "Usage: $0 OUTPUT_DIR"
    exit 1
fi

output_dir=$1

for benchmark in $(ls /root/benchmarks/*.txt)
do
    for wordlist in $(ls /root/evaluation/wordlists/*.txt)
    do
        python3 run_benchmark.py $benchmark $wordlist $output_dir
    done
done
