#!/usr/bin/env bash
# Clean-up script for application. Wipes the DB by removing docker volume.

docker compose down -v
