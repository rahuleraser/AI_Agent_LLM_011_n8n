# 096 - Docker Event Watcher

> **Category:** Developer & DevOps

Monitors Docker events and logs container activity. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Docker Event)"]
    B["Parse Event Type"]
    C["Alert On-call"]
    D["IF: Container stopped?"]
    E["Log Event"]
    F["Update Status Board"]
    G["Notify Team"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Docker event |
| Code | Event parsing |
| IF | Stop detection |
| Slack | On-call alert |
| SQLite | Event log |
| Google Sheets | Status board |

## Dockerfile

Dockerfile: [usecases/96-docker-event-watcher/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/96-docker-event-watcher/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `DOCKER_WEBHOOK_PATH=docker-event`

## Build & Run

```bash
cd usecases/96-docker-event-watcher

# Build the image
docker build -t n8n-usecase-096 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-096 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-096

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-096:
    image: n8n-usecase-096
    container_name: n8n-usecase-096
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_096_data:/home/node/.n8n"]

volumes:
  n8n_usecase_096_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
