#!/usr/bin/env bash

## Build Docker image for the <TODO name & conf> artifact.
## The name of the Docker image is specified by the IMAGE file.
## The version of the Docker image is specified by the VERSION file.


set -e

docker build -t "$(cat IMAGE):$(cat VERSION)" . --label "version=$(cat VERSION)"
