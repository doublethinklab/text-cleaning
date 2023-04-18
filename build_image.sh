#!/bin/bash

export DOCKER_BUILDKIT=1
docker build \
    --platform linux/amd64 \
    --ssh github=~/.ssh/github \
    -t doublethinklab/text-cleaning:dev \
    .
