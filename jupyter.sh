#!/bin/bash

docker run \
    --platform linux/amd64 \
    --rm \
    -v ${PWD}:/text-cleaning \
    -w /text-cleaning \
    -p $1:$1 \
        doublethinklab/text-cleaning:dev \
            jupyter notebook \
                --ip 0.0.0.0 \
                --port $1 \
                --no-browser \
                --allow-root
