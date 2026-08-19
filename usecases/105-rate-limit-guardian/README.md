# 105 - Rate Limit Guardian

> **Category:** Developer & DevOps

Monitors API rate limits and queues requests to avoid 429s. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Request)"]
    B["Check Remaining Quota"]
    C["Queue Request"]
    D["IF: Quota low?"]
    E["Send Request"]
    F["Log Throttles"]
    G["Alert API Owner"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Request inbound |
| HTTP Request | Quota check |
| IF | Quota branch |
| SQLite | Queue store |
| HTTP Request | Send |
| Slack | Owner alert |

## Dockerfile

Dockerfile: [usecases/105-rate-limit-guardian/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/105-rate-limit-guardian/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `QUOTA_WEBHOOK_PATH=throttle`
- `QUOTA_WARN_PCT=20`

## Build & Run

```bash
cd usecases/105-rate-limit-guardian

# Build the image
docker build -t n8n-usecase-105 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-105 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-105

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-105:
    image: n8n-usecase-105
    container_name: n8n-usecase-105
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_105_data:/home/node/.n8n"]

volumes:
  n8n_usecase_105_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
