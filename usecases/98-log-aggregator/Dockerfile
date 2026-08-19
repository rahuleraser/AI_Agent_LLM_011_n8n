# =============================================================================
# Use Case 098 - Log Aggregator
# -----------------------------------------------------------------------------
# n8n self-hosted Docker image for: Log Aggregator.
# Built on the official n8n community image. Runs locally on Docker Desktop.
#
# Build:
#   docker build -t n8n-usecase-098 .
# Run:
#   docker run -d --name n8n-usecase-098 -p 5678:5678 \
#     -v ~/.n8n:/home/node/.n8n n8n-usecase-098
# =============================================================================
FROM n8nio/n8n:latest

USER root

# Install verified community nodes from npm registry:
RUN cd /usr/local/lib/node_modules/n8n \
    && npm install n8n-nodes-mongodb --save \
    && npm cache clean --force

# Use-case specific environment defaults (override at runtime with -e):
ENV N8N_PROTOCOL=http \
    N8N_HOST=localhost \
    TZ=UTC \
    N8N_ENCRYPTION_KEY=CHANGE_ME_098_STRONG_KEY \
    LOG_WEBHOOK_PATH=log-ingest

EXPOSE 5678
VOLUME ["/home/node/.n8n"]

USER node
ENTRYPOINT ["docker-entrypoint.sh"]
