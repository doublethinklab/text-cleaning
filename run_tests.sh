#!/bin/bash

docker run \
    --platform linux/amd64 \
    --rm \
    -v ${PWD}:/text-cleaning \
    -w /text-cleaning \
        doublethinklab/text-cleaning:dev \
            python -m unittest discover
