#!/usr/bin/env bash
# Setup script for application. Copies default data (including envfile), logs in to Oracle Image Registry to download DB container image and initializes submodules.

set -o xtrace

cp .env.sample .env

docker login container-registry.oracle.com

git submodule update --init --remote

git submodule foreach git checkout main

cp -r data/cloudbeaver.default data/cloudbeaver
mkdir data/attachments
cp -r data/attachments.default/* data/attachments
