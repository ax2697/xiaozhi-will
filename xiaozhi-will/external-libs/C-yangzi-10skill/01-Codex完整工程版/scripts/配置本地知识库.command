#!/bin/sh
set -eu

if [ "$#" -lt 1 ]; then
  echo "用法：配置本地知识库.command <知识库文件夹或SQLite文件>"
  exit 2
fi

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
CODEX_HOME_VALUE=${CODEX_HOME:-"$HOME/.codex"}
INSTALLED_SCRIPT="$CODEX_HOME_VALUE/skills/film-knowledge-bridge/scripts/configure_knowledge_base.py"
PACKAGE_SCRIPT="$SCRIPT_DIR/../skills/film-knowledge-bridge/scripts/configure_knowledge_base.py"

if [ -f "$INSTALLED_SCRIPT" ]; then
  python3 "$INSTALLED_SCRIPT" "$1"
else
  python3 "$PACKAGE_SCRIPT" "$1"
fi
