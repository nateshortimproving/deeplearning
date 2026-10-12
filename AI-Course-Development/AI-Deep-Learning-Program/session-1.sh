#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="$HOME/source/ai-dlp"

if [ -d "$TARGET_DIR" ]; then
  rm -rf "$TARGET_DIR"
fi

mkdir -p "$TARGET_DIR"

cp "$SCRIPT_DIR/student-workspace/skills/create-"*.skill.md "$TARGET_DIR/"
cp "$SCRIPT_DIR/student-workspace/sample-docs/"* "$TARGET_DIR/"
