# =============================================================================
# Use Case 037 - Shopify Inventory Sync
# -----------------------------------------------------------------------------
# n8n self-hosted Docker image for: Shopify Inventory Sync.
# Built on the official n8n community image. Runs locally on Docker Desktop.
#
# Build:
#   docker build -t n8n-usecase-037 .
# Run:
#   docker run -d --name n8n-usecase-037 -p 5678:5678 \
#     -v ~/.n8n:/home/node/.n8n n8n-usecase-037
# =============================================================================
FROM n8nio/n8n:latest

USER root

# Install verified community nodes from npm registry:
RUN cd /usr/local/lib/node_modules/n8n \
    && npm install n8n-nodes-sqlite --save \
    && npm cache clean --force

# Use-case specific environment defaults (override at runtime with -e):
ENV N8N_PROTOCOL=http \
    N8N_HOST=localhost \
    TZ=UTC \
    N8N_ENCRYPTION_KEY=CHANGE_ME_037_STRONG_KEY \
    INV_CRON=0 * * * * \
    LOW_STOCK_THRESHOLD=5

EXPOSE 5678
VOLUME ["/home/node/.n8n"]

USER node
ENTRYPOINT ["docker-entrypoint.sh"]
