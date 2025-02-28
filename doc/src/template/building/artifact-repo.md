# The artifact repository

In the Git repository of the _tool_, copy all files from the `template/artifact-repo/` directory of
the template.

Once that is done, you can now go through each file and edit it as described below.

## `AUTHORS`

You should most likely copy the `AUTHORS` file from the _tool_ repository.

## `build.sh`

You should replace `<TODO name & conf>` with the name of your tool and the target conference. For
example, `Spellcheck CONF'99`.

## `Dockerfile`

You should delete the contents of this file and replace them with the appropriate code to generate a
usable Docker image for the artifact. You can find the full reference at
<https://docs.docker.com/reference/dockerfile/>.

This template encourages basing the Docker image **on the Docker image of the _tool_ repository**.
For simple cases, this is as easy as adding `FROM <TOOL>:<VERSION>` at the top of the `Dockerfile`.
For more complex cases, see [_A note on stacking Docker images_](./stacking-docker-images.md).

## `.dockerignore`

This file contains some reasonable defaults that you will most likely want to omit from the
generated Docker image. However, you should adapt it to the needs of the artifact. For example, if
your artifact's build process generates build artifacts in a `build/` directory, that directory
should probably also be added to the `.dockerignore` (as well as the `.gitignore`).

## `IMAGE`

You should delete the contents of this file and replace them with the name of the Docker image of
your artifact. This should most likely just be `<tool_name>-<conf_name>-artifact`. For example,
`spellcheck-conf99-artifact`.

## `README.md`

In the first heading, on the first line, you should replace `TODO`s with the name of the associated
paper and the name of the conference.

The rest of the file is laid out loosely following the
[Artifact Evaluation track guidelines for ICSE'25](https://conf.researchr.org/track/icse-2025/icse-2025-artifact-evaluation),
but of course this will depend on your target conference. Consult with their guidelines and adapt
the file accordingly.

## `run-benchmark.py`

The scope of this script is to **run your tool** on a single _experimental unit_ and **evaluate**
the result. For example, if you are building a static analysis tool, it should probably:

1. Run your tool on a single program;
2. Evaluate the findings of your tool (e.g., using some ground-truth report).

You can either choose to use Python for the easy argument parsing and command running, or, if this
is not appropriate, you can delete this script entirely and replace it with a different one. In that
case, remember to update the other scripts accordingly; you can verify with
`grep "run-benchmark.py" *`. If you do wish to use this script, you can modify the existing argument
parsing and add code to launch your tool with the given benchmark/input, as well as add code to
evaluate the results.

## `run-full-evaluation.sh`

The scope of this script is to run the **full set of experiments** needed to reproduce the results
from the paper.

This template encourages basing this script on the "unit-level" `run-benchmark.py` script. This
makes it easier to modify how the experiments are run in a single place, but is not always feasible.
If possible, this script should remain essentially unchanged.

## `run-reduced-evaluation.sh`

The scope of this script is to run a **reduced set of experiments** with which the main trends and
conclusions from the paper can be verified. This script is to be used during artifact evaluation if
the `run-full-evaluation.sh` script cannot finish in a reasonable amount of time (which is often the
case).

This template encourages basing this script on the "unit-level" `run-benchmark.py` script. This
makes it easier to modify how the experiments are run in a single place, but is not always feasible.
If possible, this script should remain essentially unchanged.

## `run.sh`

You should replace `<TODO name & conf>` with the name of your tool and the target conference. For
example, `Spellcheck CONF'99`. You should also replace `<TODO fixed name>` with a good fixed name
for the Docker container. This fixed name can be used when instructing reviewers to interact with
the container, e.g., to copy a file out to their host machine. Since containers are given random
names by default, you can avoid confusion by providing a fixed name.

## `VERSION`

This file starts at a reasonable first version, so you do not need to edit it at first. You are,
however, expected to edit it as you keep track of the version of the tool. It is a good idea to make
sure this version number stays aligned with other version-tracking mechanisms (e.g., in
`pyproject.toml` for Python-based tools or in `Cargo.toml` for Rust-based tools).

Be aware that this version will not necessarily match the version of your tool from the _tool_
repository, or the version of the base Docker image of your tool.
