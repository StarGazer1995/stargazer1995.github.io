#!/bin/sh
set -eu

repo_root=$(git -C "$(dirname "$0")/.." rev-parse --show-toplevel)
git -C "$repo_root" config core.hooksPath .githooks
printf 'Installed repository hooks from %s/.githooks\n' "$repo_root"
