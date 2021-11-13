#!/bin/bash

docker run \
    --rm \
    -v ${PWD}:/text-cleaning \
    -w /text-cleaning \
        doublethinklab/text-cleaning:dev \
            python -m unittest discover
