# 106 - Webhook Debugger

> **Category:** Developer & DevOps

Receives webhook payloads and lets developers inspect them. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Payload)"]
    B["Pretty-print Payload"]
    C["Show to Developer"]
    D["IF: Fields valid?"]
    E["Flag Malformed"]
    F["Store Payload"]
    G["Notify Developer"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Payload inbound |
| Code | Pretty print |
| IF | Validation check |
| Slack | Dev notification |
| MongoDB | Payload store |
| Email | Malformed alert |

## Dockerfile

Dockerfile: [usecases/106-webhook-debugger/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/106-webhook-debugger/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `DEBUG_WEBHOOK_PATH=debug`

## Build & Run

```bash
cd usecases/106-webhook-debugger

# Build the image
docker build -t n8n-usecase-106 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-106 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-106

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-106:
    image: n8n-usecase-106
    container_name: n8n-usecase-106
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_106_data:/home/node/.n8n"]

volumes:
  n8n_usecase_106_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
