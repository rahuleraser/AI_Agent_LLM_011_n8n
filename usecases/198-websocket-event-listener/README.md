# 198 - WebSocket Event Listener

> **Category:** API Integration & Automation

Listens to WebSocket events and processes them. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["WebSocket Trigger (Event)"]
    B["Parse Event Message"]
    C["Process Event"]
    D["IF: Event type known?"]
    E["Log Unknown Type"]
    F["Store Event"]
    G["Notify Subscribers"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| WebSocket Trigger | Event stream |
| Code | Message parse |
| IF | Type check |
| HTTP Request | Process |
| SQLite | Event store |
| Slack | Unknown alert |

## Dockerfile

Dockerfile: [usecases/198-websocket-event-listener/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/198-websocket-event-listener/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `WS_WEBHOOK_PATH=websocket`

## Build & Run

```bash
cd usecases/198-websocket-event-listener

# Build the image
docker build -t n8n-usecase-198 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-198 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-198

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-198:
    image: n8n-usecase-198
    container_name: n8n-usecase-198
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_198_data:/home/node/.n8n"]

volumes:
  n8n_usecase_198_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
