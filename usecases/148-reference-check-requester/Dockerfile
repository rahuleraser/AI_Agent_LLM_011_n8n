# =============================================================================
# Use Case 148 - Reference Check Requester
# -----------------------------------------------------------------------------
# n8n self-hosted Docker image for: Reference Check Requester.
# Built on the official n8n community image. Runs locally on Docker Desktop.
#
# Build:
#   docker build -t n8n-usecase-148 .
# Run:
#   docker run -d --name n8n-usecase-148 -p 5678:5678 \
#     -v ~/.n8n:/home/node/.n8n n8n-usecase-148
# =============================================================================
FROM n8nio/n8n:latest

USER root

# This use case is powered by n8n built-in nodes (400+ included).
# Add community nodes later if needed, e.g.:
# RUN cd /usr/local/lib/node_modules/n8n \
#     && npm install n8n-nodes-mcp --save \
#     && npm cache clean --force

# Use-case specific environment defaults (override at runtime with -e):
ENV N8N_PROTOCOL=http \
    N8N_HOST=localhost \
    TZ=UTC \
    N8N_ENCRYPTION_KEY=CHANGE_ME_148_STRONG_KEY \
    REFERENCE_WEBHOOK_PATH=reference

EXPOSE 5678
VOLUME ["/home/node/.n8n"]

USER node
ENTRYPOINT ["docker-entrypoint.sh"]
