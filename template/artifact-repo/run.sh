#!/usr/bin/env bash

## Run a Docker container with the <TODO name & conf> artifact image.
## The name of the Docker image is specified by the IMAGE file.
## The version of the Docker image is specified by the VERSION file.


set -e


docker run -ti --rm --name <TODO fixed name> "$(cat IMAGE):$(cat VERSION)"
