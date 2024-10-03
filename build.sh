#!/usr/bin/bash

## Build Docker image for the artifact.
## The name of the Docker image is specified by the ARTIFACT file.
## The version of the Docker image is specified by the VERSION file.


set -e

docker build -t $(cat ARTIFACT):$(cat VERSION) . --label "version=$(cat VERSION)"
