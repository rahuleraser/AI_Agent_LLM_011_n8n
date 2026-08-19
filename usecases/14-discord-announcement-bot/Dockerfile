# =============================================================================
# Use Case 014 - Discord Announcement Bot
# -----------------------------------------------------------------------------
# n8n self-hosted Docker image for: Discord Announcement Bot.
# Built on the official n8n community image. Runs locally on Docker Desktop.
#
# Build:
#   docker build -t n8n-usecase-014 .
# Run:
#   docker run -d --name n8n-usecase-014 -p 5678:5678 \
#     -v ~/.n8n:/home/node/.n8n n8n-usecase-014
# =============================================================================
FROM n8nio/n8n:latest

USER root

# Install verified community nodes from npm registry:
RUN cd /usr/local/lib/node_modules/n8n \
    && npm install n8n-nodes-discord --save \
    && npm cache clean --force

# Use-case specific environment defaults (override at runtime with -e):
ENV N8N_PROTOCOL=http \
    N8N_HOST=localhost \
    TZ=UTC \
    N8N_ENCRYPTION_KEY=CHANGE_ME_014_STRONG_KEY \
    ANNOUNCE_CRON=0 10 * * * \
    DISCORD_CHANNEL=announcements

EXPOSE 5678
VOLUME ["/home/node/.n8n"]

USER node
ENTRYPOINT ["docker-entrypoint.sh"]
