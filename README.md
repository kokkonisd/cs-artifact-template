# CS artifact template
This is a simple template for an artifact in the form of a Docker image, to accompany a scientific
paper. It's tailored for typical Computer Science artifacts, but can potentially serve as a basis
for other types of artifacts.

## How to use
This template contains a toy example to demonstrate how an artifact evaluation could play out. The
toy example is an extremely naive spellchecker with an (unnecessary) external dependency, in order
to show how to manage those as well. It is evaluated by running it against misspelled text and some
wordlist (containing valid words), and then comparing it to a ground-truth result produced with a
perfect oracle. Ideally, the results of the evaluation should be as close as possible to the
ground-truth results.

### Repo summary
Here is the breakdown of the repo:
- `ARTIFACT`: contains the name of the artifact. It is used to tag the Docker image with the
  appropriate name.
- `benchmarks/`: contains the benchmarks (misspelled text) for the evaluation as well as the
  ground-truth spelling fixes. For example, `benchmarks/ground-truth/brown_fox.txt` contains the
  spelling fixes for `benchmarks/brown_fox.txt`.
- `build.sh`: builds the Docker image using `ARTIFACT` and `VERSION`, specifically the image called
  `{ARTIFACT}:{VERSION}`.
- `Dockerfile`: describes how to build the Docker image. Handles installation of system-level
  dependencies, building external dependencies, tools and so on.
- `evaluation/`: contains the evaluation environment, in which the person running the evaluation is
  expected to run stuff and produce results. The wordlists used by the tool are placed here (such
  is my personal preference), but they could also be placed in their own directory as an additional
  external dependency.
- `external-dependency/`: an example of an external dependency needed by the main tool. For this
  specific example this dependency is completely unnecessary, but serves as an example of how one
  would deal with dependencies. This program accepts a base word and a wordlist and returns (prints
  in `stdout`) the word from the wordlist which is the most similar compared to the base word. This
  similarity is computed using the
  [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance).
- `README.md`: the file you're reading right now.
- `run.sh`: runs a Docker container with the image specified by `ARTIFACT` and `VERSION`, so the
  image called `{ARTIFACT}:{VERSION}`.
- `tool/`: the tool that this artifact is built to evaluate. The toy example presented here is a
  naive spellchecker, using the program found under `external-dependency/` to attempt to spell
  check a given text file.
- `VERSION`: the current version of the artifact. It is used to tag the Docker image with the
  appropriate version.

### Architecture
You can build the image by running `./build`, then start up a container by running `./run
DIR_NAME`. In this instance, `DIR_NAME` is a directory that either exists or will be created at
`$HOME/DIR_NAME`, serving as a generic "output directory" for any and all results generated during
the evaluation. This directory will be mounted as a separate volume inside the Docker container, to
ensure that any and all experiment results will end up in an actual directory of the host machine,
and will not be lost if the container crashes or runs out of space.

You can see that the container starts up in the `evaluation/` directory; all external dependencies,
benchmarks and the main tool are placed in separate directories under `/root/`, and the
`evaluation/` directory contains appropriate scripts to invoke them. There are 3 scripts here:
- `run_benchmark.py`: this script runs a single benchmark with a given wordlist. The idea is you
  would invoke it with `./run_benchmark.py BENCHMARK WORDLIST /root/evaluation/DIR_NAME`, with the
  `DIR_NAME` being the same as the one you chose when creating the container with `./run.sh`. This
  will produce a CSV file containing the results of the experiment. This script is very versatile
  if you want to run one specific experiment.
- `partial_evaluation.sh`: this is actually what is meant to be used by an artifact evaluator. In
  order to encourage a more "push-button" approach, we hardcode a specific set of experiments to
  run, and the artifact evaluator only needs to provide a valid output directory
  (`/root/evaluation/DIR_NAME`, like before). The idea of a partial evaluation is to convince the
  artifact evaluator of the results presented in the paper, without forcing them to sit through an
  enormous amount of CPU hours.
- `full_evaluation.sh`: while most artifact reviewers will only run the partial evaluation, for
  completeness' sake we should also provide a way to run _all_ of the experiments which are present
  in the paper. This is exactly what this script does, and it otherwise works in the same way as
  `partial_evaluation.sh`.

## Adapting the template to your needs
Here is the list of things you need to adapt in this template in order to build your own real
artifact, on a per-file basis:
- `ARTIFACT`: change the content of the file to match the name of the artifact you want to submit.
- `benchmarks/`: replace with your actual benchmarks. This can be as simple as a Git submodule
  pointing to another repo. You don't _have_ to store the ground-truth results here; adapt the
  specifics of the evaluation to your needs.
- `Dockerfile`: change the base image, install the system-level dependencies you need, add
  compilation/install steps if needed for either the external dependencies or your tool.
- `evaluation/`:
    - `run_benchmark.py`: modify or replace with your actual benchmark runner.
    - `*_evaluation.sh`: adapt to use your benchmark runner and the appropriate experiments.
    - Overall: add evaluation-specific data (like the wordlists here) or move it under `/root/` if
      that seems better to you.
- `external-dependency/`: replace with external dependency(ies) if any and rename accordingly.
- `README.md`: completely rewrite it to adhere to the submission guidelines, and explain how to use
  the artifact itself.
- `tool/`: replace and rename with your actual tool.

Last but not least, don't forget to update `VERSION` when you modify your artifact (and ideally tag
the commit when you do so). This can save you a lot of headaches when you're trying to find a very
specific version of your artifact that worked.

## License
The license found in `LICENSE` is the [Creative Commons Attribution-ShareAlike 4.0 International](
https://creativecommons.org/licenses/by-sa/4.0/?ref=chooser-v1) and applies to all contents of the
repo except for the file `evaluation/wordlists/194434-English-Word-List_djvu.txt`.

## Credits
The wordlist `evaluation/wordlists/194434-English-Word-List_djvu.txt` comes from
<https://archive.org/details/194000-english-words-list-compilation/194k-English-words-list/>.
