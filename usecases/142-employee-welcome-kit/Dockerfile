# =============================================================================
# Use Case 142 - Employee Welcome Kit
# -----------------------------------------------------------------------------
# n8n self-hosted Docker image for: Employee Welcome Kit.
# Built on the official n8n community image. Runs locally on Docker Desktop.
#
# Build:
#   docker build -t n8n-usecase-142 .
# Run:
#   docker run -d --name n8n-usecase-142 -p 5678:5678 \
#     -v ~/.n8n:/home/node/.n8n n8n-usecase-142
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
    N8N_ENCRYPTION_KEY=CHANGE_ME_142_STRONG_KEY \
    WELCOME_WEBHOOK_PATH=welcome-kit

EXPOSE 5678
VOLUME ["/home/node/.n8n"]

USER node
ENTRYPOINT ["docker-entrypoint.sh"]
