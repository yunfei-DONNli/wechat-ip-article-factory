#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
for runtime in "$HOME/.codex/skills" "$HOME/.agents/skills" "$HOME/.claude/skills"; do
  mkdir -p "$runtime"
  rsync -a --delete --exclude='.DS_Store' "$ROOT/skills/" "$runtime/"
  find "$runtime" -name '.DS_Store' -delete
  echo "synced $runtime"
done
