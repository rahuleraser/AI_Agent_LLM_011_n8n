# 195 - Webhook Retry Handler

> **Category:** API Integration & Automation

Retries failed webhook deliveries with backoff. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Delivery)"]
    B["Check Delivery Status"]
    C["Retry with Backoff"]
    D["IF: Failed?"]
    E["Mark Delivered"]
    F["Log Attempts"]
    G["Alert After Max"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Delivery event |
| Code | Status check |
| IF | Failure branch |
| Wait | Backoff delay |
| HTTP Request | Retry send |
| SQLite | Attempt log |

## Dockerfile

Dockerfile: [usecases/195-webhook-retry-handler/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/195-webhook-retry-handler/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `RETRY_WEBHOOK_PATH=retry`
- `MAX_RETRIES=5`

## Build & Run

```bash
cd usecases/195-webhook-retry-handler

# Build the image
docker build -t n8n-usecase-195 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-195 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-195

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-195:
    image: n8n-usecase-195
    container_name: n8n-usecase-195
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_195_data:/home/node/.n8n"]

volumes:
  n8n_usecase_195_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
