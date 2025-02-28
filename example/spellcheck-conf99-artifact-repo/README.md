# Artifact for the paper "Spellcheck: Checking New Spells" (CONF'99)

## Purpose

This artifact allows for the evaluation of Spellcheck, a novel spell checking tool built on top of
the `similar-word-finder` tool. More precisely, this artifact makes it possible to reproduce the
evaluation results reported in our CONF'99 paper about Spellcheck, as they are detailed in Table III
and Figure 5 of this paper.

We are applying for the _Available_ and _Coolest_ badges, for the following reasons:

- **Available**: the artifact satisfies the requirements of this badge, as it has been fully
  archived on the Zenodo public archival repository with an associated unique identifier:
  <https://zenodo.org/records/00000000> (DOI: <https://doi.org/10.1234/zenodo.4321>).
- **Coolest**: the artifact satisfies the requirements of this badge, as it is _really really_ cool.

## Provenance

This artifact can be obtained from Zenodo: <https://zenodo.org/records/00000000>

## Data

The benchmarks used to evaluate the Spellcheck tool are part of the
[EXAMPLE word benchmark](https://example.com). As such, they are licensed under the
[LGPL-2.1](https://opensource.org/license/lgpl-2-1) license.

## Setup

### Hardware

This artifact does not require specific hardware for its evaluation.

### Software

While the Spellcheck tool can be run natively in all major OSes, it is recommended to use the
provided **Docker image** (powered either by [Docker Desktop](https://docs.docker.com/desktop/) or
[Docker Engine](https://docs.docker.com/engine/)).

#### Installing the Docker image

The image can be loaded transparently via [Docker Hub](https://hub.docker.com):

```console
$ docker pull spellcheck-conf99-artifact:0.1.0
```

As a more durable alternative, it can also be downloaded from the Zenodo archive and then loaded
locally. For example, using [curl](https://curl.se/):

```console
$ curl https://zenodo.org/records/00000000/files/spellcheck-docker-image_0-1-0.tar | docker load
```

Once the image has been loaded, a container can be started using the following command:

```console
$ docker run -ti --rm --name spellcheck-conf99-artifact spellcheck-conf99-artifact:0.1.0
```

This will immediately start an interactive session within the container, from which you can start
using the artifact.

##### Uninstalling the Docker image

Once you are done using the artifact, you can dispose of it by simply removing the Docker image.
Make sure to exit any running container(s) associated with the artifact's Docker image, and then
run:

```console
$ docker rmi spellcheck-conf99-artifact:0.1.0
```

## Usage

The artifact can be used in three different ways:

- To reproduce the results of the paper in a reasonable amount of time, you can run the reduced
  evaluation **from within the container**:
  ```console
  $ /root/artifact/run-reduced-evaluation.sh
  ```
- To reproduce the full results of the paper, you can run the full evaluation **from within the
  container**:
  ```console
  $ /root/artifact/run-full-evaluation.sh
  ```
- To reproduce any single benchmark, or to evaluate Spellcheck on new examples, you can run the
  following **from within the container**:
  ```console
  $ /root/artifact/run-benchmark.py BENCHMARK WORDLIST OUTPUT_DIR
  ```
