#!/usr/bin/bash

set -o xtrace

cp .env.sample .env

docker login container-registry.oracle.com
