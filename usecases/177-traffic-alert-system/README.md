# 177 - Traffic Alert System

> **Category:** IoT & Smart Home

Sends traffic alerts before the daily commute. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Daily)"]
    B["Fetch Traffic Data"]
    C["Send Route Alert"]
    D["IF: Congestion high?"]
    E["Log Traffic"]
    F["Suggest Alternative"]
    G["Notify Commuter"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Morning check |
| HTTP Request | Traffic API |
| IF | Congestion check |
| Telegram | Route alert |
| SQLite | Traffic log |
| Email | Alternatives send |

## Dockerfile

Dockerfile: [usecases/177-traffic-alert-system/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/177-traffic-alert-system/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `TRAFFIC_CRON=0 7 * * 1-5`
- `CONGESTION_WARN=70`

## Build & Run

```bash
cd usecases/177-traffic-alert-system

# Build the image
docker build -t n8n-usecase-177 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-177 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-177

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-177:
    image: n8n-usecase-177
    container_name: n8n-usecase-177
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_177_data:/home/node/.n8n"]

volumes:
  n8n_usecase_177_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
