#!/bin/bash

set -Eeuo pipefail

dd if=/dev/zero of=/tmp/8GB.bin bs=64M count=128 iflag=fullblock
