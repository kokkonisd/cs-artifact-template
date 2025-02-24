## Dockerfile for the Spellcheck CONF'YY artifact.

FROM spellcheck:0.1.0-dev

LABEL maintainer="maintainer@email.com"
LABEL description="Docker image artifact for the paper \"XYZ\""


RUN apt-get clean && apt-get update


# Assume we have to install extra dependencies for the artifact itself.
RUN apt-get update && apt-get install -y bison flex

WORKDIR /root/artifact
COPY . .
