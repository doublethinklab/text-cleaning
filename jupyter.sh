#!/bin/bash

docker run \
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
