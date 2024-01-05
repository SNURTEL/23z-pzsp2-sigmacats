#!/usr/bin/env bash

set -o xtrace

cp .env.sample .env

docker login container-registry.oracle.com

git submodule update --init --remote

git submodule foreach git checkout main

cp -r data/cloudbeaver.default data/cloudbeaver
mkdir data/attachments
cp -r data/attachments.default/* data/attachments
