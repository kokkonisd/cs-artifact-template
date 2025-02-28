# Documentation for Spellcheck

Spellcheck can be used by providing a WORDLIST (i.e., a list of correct spellings of words) and an
INPUT FILE to be spell-checked.

You can then run Spellcheck with the following command:

```console
$ python3 spellcheck.py WORDLIST INPUT_FILE
```

## Extending Spellcheck

You can extend Spellcheck by providing different _similar word finder_ backends. In order to do so,
you simply need to change the path to the backend used by modifying the `SIMILAR_WORD_FINDER`
constant in `spellcheck.py`. The backend should expect to be fed a candidate word and a list of
words, and it should in turn print (on `stdout`) the most similar word to the candidate word from
the list.
