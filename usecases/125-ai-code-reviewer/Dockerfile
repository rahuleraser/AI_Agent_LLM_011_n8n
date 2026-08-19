# =============================================================================
# Use Case 125 - AI Code Reviewer
# -----------------------------------------------------------------------------
# n8n self-hosted Docker image for: AI Code Reviewer.
# Built on the official n8n community image. Runs locally on Docker Desktop.
#
# Build:
#   docker build -t n8n-usecase-125 .
# Run:
#   docker run -d --name n8n-usecase-125 -p 5678:5678 \
#     -v ~/.n8n:/home/node/.n8n n8n-usecase-125
# =============================================================================
FROM n8nio/n8n:latest

USER root

# Install verified community nodes from npm registry:
RUN cd /usr/local/lib/node_modules/n8n \
    && npm install n8n-nodes-github n8n-nodes-mcp --save \
    && npm cache clean --force

# Use-case specific environment defaults (override at runtime with -e):
ENV N8N_PROTOCOL=http \
    N8N_HOST=localhost \
    TZ=UTC \
    N8N_ENCRYPTION_KEY=CHANGE_ME_125_STRONG_KEY \
    AI_REVIEW_WEBHOOK_PATH=code-review

EXPOSE 5678
VOLUME ["/home/node/.n8n"]

USER node
ENTRYPOINT ["docker-entrypoint.sh"]
