#!/usr/bin/bash

## Run a Docker container with the artifact.
## The name of the Docker image is specified by the ARTIFACT file.
## The version of the Docker image is specified by the VERSION file.


set -e

if [ "$#" -ne "1" ]
then
    echo "Usage: $0 [BENCHMARK_DIR_NAME]"
    exit 1
fi

# Mount a directory as a shared volume between the container and the host. This is to prevent the
# default volume used by Docker from being saturated, and to avoid losing experiment data if the
# container is killed.
benchmark_dir=$1
echo "Using $HOME/$benchmark_dir as a shared volume"
sleep 2

docker run -ti --rm --name $USER-$(date +%d.%m.%y-%Hh%Mm%Ss) \
    -v $HOME/$benchmark_dir:/root/evaluation/$benchmark_dir $(cat ARTIFACT):$(cat VERSION)
