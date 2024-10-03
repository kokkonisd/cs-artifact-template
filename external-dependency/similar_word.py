#!/usr/bin/env python3

"""
Get the most similar word from a wordlist.
"""

import argparse
import multiprocessing


def hamming(word1: str, word2: str) -> tuple[float, str]:
    """Compute the Hamming distance between two words."""
    if len(word1) != len(word2):
        return (float("inf"), word2)

    distance = 0
    for i in range(0, len(word1)):
        if word1[i] != word2[i]:
            distance += 1

    return (distance, word2)


def main() -> None:
    """Run the program."""
    parser = argparse.ArgumentParser(
        description="Get the most similar word (to a given word) from a wordlist."
    )
    parser.add_argument("word", help="The base word.")
    parser.add_argument("wordlist", help="The wordlist file.")

    args = parser.parse_args()

    with open(args.wordlist) as wordlist_file:
        wordlist = wordlist_file.read().splitlines()

    with multiprocessing.Pool() as pool:
        results = pool.starmap(
            hamming, [(args.word, wordlist_word) for wordlist_word in wordlist]
        )

    min_distance, best_word = results[0]
    for distance, wordlist_word in results:
        if distance < min_distance:
            min_distance = distance
            best_word = wordlist_word

    print(best_word)


if __name__ == "__main__":
    main()
