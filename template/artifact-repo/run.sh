#!/usr/bin/env bash

## Run a Docker container with the Spellcheck CONF'YY artifact image.
## The name of the Docker image is specified by the IMAGE file.
## The version of the Docker image is specified by the VERSION file.


set -e


docker run -ti --rm --name spellcheck-confYY-artifact "$(cat IMAGE):$(cat VERSION)"
