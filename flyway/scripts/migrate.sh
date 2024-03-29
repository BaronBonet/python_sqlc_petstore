#!/usr/bin/env bash

set -e o pipefail
#
# if [[ -z "${FLYWAY_URL}" || -z "${DB_USERNAME}" ]]; then
#   echo "DB_USERNAME and FLYWAY URL is required"
#   exit 1
# fi

export FLYWAY_USER="${FLYWAY_USER:-${DB_USERNAME}}"
export FLYWAY_PASSWORD="${FLYWAY_PASSWORD:-${DB_PASSWORD}}"

export FLYWAY_URL="${FLYWAY_URL:-jdbc:postgresql://${DB_HOST}:${DB_PORT}/${DB_NAME}}"

flyway -connectRetries=5 -locations="filesystem:/flyway/migrations" migrate


