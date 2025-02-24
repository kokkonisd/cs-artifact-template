## Dockerfile for the Spellcheck CONF'99 artifact.

FROM spellcheck:0.1.0

LABEL maintainer="jane.doe@example.com"
LABEL description="Docker image artifact for the paper \"Spellcheck: Checking New Spells\""


RUN apt-get clean && apt-get update


# Assume we have to install extra dependencies for the artifact itself.
RUN apt-get update && apt-get install -y bison flex

WORKDIR /root/artifact
COPY . .
