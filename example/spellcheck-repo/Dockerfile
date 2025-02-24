## Dockerfile for the `spellcheck` tool.

FROM ubuntu:24.04

LABEL maintainer="jane.doe@example.fr"
LABEL description="Docker image for the spellcheck tool"


RUN apt-get clean && apt-get update


# Assume we need to install some dependencies.
RUN apt-get update && apt-get install -y build-essential python3-dev

WORKDIR /root
COPY . ./spellcheck/
