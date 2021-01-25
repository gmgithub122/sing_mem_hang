#!/bin/bash

set -Eeuo pipefail

PIDS=""
CONTAINER="/tmp/minimal.sif"

for _ in $(seq 1 10); do
  cgexec -g memory:test_cg_1gb singularity exec ${CONTAINER} python read_h5.py &
  PID=$!
  echo "started" ${PID}
  PIDS="$PIDS $PID"
done

echo "waiting..."
# shellcheck disable=SC2086
wait ${PIDS}
echo "done"
