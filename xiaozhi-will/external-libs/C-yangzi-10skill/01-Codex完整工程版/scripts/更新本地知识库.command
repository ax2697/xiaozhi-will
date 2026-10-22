#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
bash "$SCRIPT_DIR/../skills/film-knowledge-bridge/scripts/update_knowledge_index.command" "$@"
