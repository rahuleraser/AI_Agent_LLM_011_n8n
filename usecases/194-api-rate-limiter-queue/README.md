# 194 - API Rate Limiter Queue

> **Category:** API Integration & Automation

Queues API calls to respect rate limits. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Request)"]
    B["Check Current Usage"]
    C["Queue Request"]
    D["IF: Limit reached?"]
    E["Send Request"]
    F["Replay Queue"]
    G["Log Throttling"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Request inbound |
| HTTP Request | Usage check |
| IF | Limit check |
| SQLite | Queue store |
| HTTP Request | Send |
| Google Sheets | Throttle log |

## Dockerfile

Dockerfile: [usecases/194-api-rate-limiter-queue/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/194-api-rate-limiter-queue/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `RATE_QUEUE_WEBHOOK_PATH=rate-queue`

## Build & Run

```bash
cd usecases/194-api-rate-limiter-queue

# Build the image
docker build -t n8n-usecase-194 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-194 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-194

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-194:
    image: n8n-usecase-194
    container_name: n8n-usecase-194
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_194_data:/home/node/.n8n"]

volumes:
  n8n_usecase_194_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
