#!/bin/bash

set -Eeuo pipefail

if [ "$#" -ne 2 ]; then
    echo "usage: create_cg.sh <user> <group>"
fi

cgcreate -g memory:test_cg_1gb -a "${1}":"${2}" -t "${1}":"${2}"
echo 1G >/sys/fs/cgroup/memory/test_cg_1gb/memory.limit_in_bytes
