# The `spellcheck-conf99-artifact` artifact repository
The repository for the `spellcheck` artifact can be found under
`example/spellcheck-conf99-artifact`.

As a reminder, this repository is destined to _artifact evaluators_ at the Artifact Evaluation
track of the fictional CONF'99 conference. As such, its contents are in reality heavily dictated by
the guidelines of the Artifact Evaluation track. For example, the `README.md` file is loosely based
on the guidelines for
[ICSE'25](https://conf.researchr.org/track/icse-2025/icse-2025-artifact-evaluation).

## Docker image
Apart from the files and general structure imposed by the guidelines, this repository shares the
same Docker infrastructure as the [tool repository](./spellcheck-tool-repo.md). One subtlety is
that, as you can see in the `Dockerfile`, the image of the artifact is based on the image of the
tool from the _tool_ repository. This helps to both (1) pin the version of Spellcheck and (2) reuse
the Spellcheck Docker image, but it is not strictly necessary&mdash;we could also use [Git
submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules), but we would probably have to
partially reimplement the dependency installation and setup done in the Spellcheck _tool_
repository. Also see [_A note on stacking Docker
images_](../template/building/stacking-docker-images.md) for more details.

## Data needed for the (re)production of experiments
The following files and directories are new:
- `benchmarks/`: this directory contains a list of benchmarks on which Spellcheck is evaluated. In
  the case of Spellcheck, a benchmark is a text file potentially containing misspelled words. In
  order to evaluate the precision of Spellcheck, the "ground truth" (i.e., correct spelling fixes)
  version of each text file is provided, under `benchmarks/ground-truth`. In reality, this
  `benchmarks/` directory may be organized very differently based on the "target" of the tool, or
  it might even be a [Git submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules) pointing
  to a different repository which contains the benchmark. Finally, in the case where the benchmark
  is part of the contributions of the paper (and thus an artifact), it might have its own _tool_
  repository which will then get referenced here.
- `wordlists/`: since Spellcheck also takes a list of correctly spelled words as input, such lists
  need to be provided. Again, in reality this is the same as the `benchmarks/` directory; it could
  also be an external Git repository or a Docker image we build upon.

## Utility scripts
The following utility scripts can be used (e.g., by the artifact evaluators) to simplify the
reproduction of the results of the paper:
- `run-full-evaluation.sh`: this script runs _all_ of the experiments needed to reproduce the
  results from the paper. In this case, it is very simple, but in reality it most often translates
  to _months_ or even _years_ of CPU time.
- `run-reduced-evaluation.sh`: this script runs a selected benchmark only, in the interest of time.
  In reality, this is often done as the full evaluation is infeasible given the deadlines of the
  reviewers, so a reduced evaluation that is still capable of showing e.g., the trends and
  conclusions from the paper is preferred.
- `run-benchmark.py`: this script runs a single benchmark. As such, it can both be used to
  _perform_ the experiments in the first place (by the authors) and _reproduce_ selected
  experiments or even to be tried out on new benchmarks (by the reviewers).


## Versioning
Again, [Semantic Versioning](https://semver.org/) is used (in tandem with Git) for the artifact
repository. The only difference is that, in this case, we also have to choose the version of the
Spellcheck tool used in the artifact. This is easy to do via the base Docker image selected in the
`Dockerfile`. Again, the `VERSION` file defines the version of the entire repository and generated
image, so it is possible that the version of the Spellcheck _tool_ and the version of the
Spellcheck _artifact_ will not be the same.
