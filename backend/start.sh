#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

cp app/backend_pre_start.py .
python3 backend_pre_start.py

uvicorn app.main:app --proxy-headers --host 0.0.0.0 --port 80
