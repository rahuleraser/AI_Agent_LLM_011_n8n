#!/usr/bin/env bash
# =============================================================================
# Build all 200 n8n use-case images + the base image.
# Run from the repository root:  ./scripts/build-all.sh
# =============================================================================
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "==> Building base n8n image"
docker build -f "$ROOT_DIR/docker/base/Dockerfile.n8n" -t n8n-base:latest "$ROOT_DIR/docker/base"

for dir in "$ROOT_DIR"/usecases/*/; do
  name="$(basename "$dir")"
  tag="n8n-${name}"
  echo "==> Building $tag"
  docker build -t "$tag" "$dir"
done

echo ""
echo "All images built:"
docker images | grep n8n || true
