#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

uvicorn app.main:app --proxy-headers --host 0.0.0.0 --port 80
