#!/bin/bash

set -Eeuo pipefail

PIDS=""

for _ in $(seq 1 10); do
  cgexec -g memory:test_cg_1gb python read_bin.py &
  PID=$!
  echo "started" ${PID}
  PIDS="$PIDS $PID"
done

echo "waiting..."
# shellcheck disable=SC2086
wait ${PIDS}
echo "done"
