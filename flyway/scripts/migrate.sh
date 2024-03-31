#!/usr/bin/env bash

set -e o pipefail

export FLYWAY_USER="${FLYWAY_USER:-${DB_USERNAME}}"
export FLYWAY_PASSWORD="${FLYWAY_PASSWORD:-${DB_PASSWORD}}"

export FLYWAY_URL="${FLYWAY_URL:-jdbc:postgresql://${DB_HOST}:${DB_PORT}/${DB_NAME}}"

flyway -connectRetries=5 -locations="filesystem:/flyway/migrations" migrate


