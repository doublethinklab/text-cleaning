#!/bin/bash

export DOCKER_BUILDKIT=1
docker build \
    --ssh github=~/.ssh/github \
    -t doublethinklab/text-cleaning:dev \
    .
