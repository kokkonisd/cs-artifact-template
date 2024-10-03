FROM ubuntu:24.04

LABEL maintainer="maintainer@email.com"
LABEL description="Docker image artifact for the paper \"XYZ\""


RUN apt-get clean && apt-get update


# Install dependencies.
# NOTE: this is not actually a dependency for the toy example, but you should install whatever you
# need here.
RUN apt-get update && apt-get install -y build-essential python3-dev

# Prepare external dependency.
WORKDIR /root/
COPY external-dependency/ ./external-dependency/

# Prepare the tool.
WORKDIR /root/
COPY tool/ ./tool/

# Prepare benchmarks. 
WORKDIR /root/
COPY benchmarks/ ./benchmarks/

# Prepare the evaluation environment.
WORKDIR /root/
COPY evaluation/ ./evaluation/

# Start shell.
WORKDIR /root/evaluation/
CMD ["/usr/bin/bash"]
