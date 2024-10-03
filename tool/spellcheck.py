#!/usr/bin/env python3

"""
Implement a naive spellchecker.
"""

import argparse
import os
import subprocess
import sys
from typing import Optional

MOST_SIMILAR_WORD_PROGRAM = os.path.join(
    "/root", "external-dependency", "similar_word.py"
)


def spell_check(
    text: str, wordlist_file: str, max_sensitivity: int = 5
) -> list[tuple[str, str]]:
    """Spell check some text (naively)."""
    spelling_errors = []

    words = list(
        map(
            lambda word: word.rstrip("\n.,;!?"),
            filter(lambda word: len(word), text.split(" ")),
        )
    )

    for actual_word in words:
        # Call external dependency.
        correct_word = subprocess.run(
            [
                sys.executable,
                MOST_SIMILAR_WORD_PROGRAM,
                actual_word.lower(),
                wordlist_file,
            ],
            capture_output=True,
            text=True,
        ).stdout.rstrip()
        if actual_word.lower() != correct_word:
            spelling_errors.append((actual_word, correct_word))

    return spelling_errors


def main() -> None:
    """Run the spellchecker given a text file to spellcheck and a wordlist."""
    parser = argparse.ArgumentParser(description="Run a spell checker on a text file.")
    parser.add_argument("wordlist", help="A list of valid words to check against.")
    parser.add_argument(
        "input_files", help="The file(s) to spell check.", nargs="+", metavar="FILE"
    )

    args = parser.parse_args()

    spelling_errors = []
    for input_file in args.input_files:
        with open(input_file, "r") as text_file:
            spelling_errors += spell_check(
                text=text_file.read(), wordlist_file=args.wordlist
            )

    for actual_word, correct_word in spelling_errors:
        print(f"{actual_word} -> {correct_word}")


if __name__ == "__main__":
    main()
