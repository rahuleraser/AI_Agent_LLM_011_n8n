# 108 - Microservice Health Check

> **Category:** Developer & DevOps

Checks the health of all microservices in a stack. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (5 min)"]
    B["Poll All Services"]
    C["Alert On-call"]
    D["IF: Any unhealthy?"]
    E["Log All Healthy"]
    F["Send Status Snapshot"]
    G["Notify Team"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Health poll |
| HTTP Request | Service check |
| IF | Health branch |
| Slack | On-call alert |
| Google Sheets | Status board |
| SQLite | Health log |

## Dockerfile

Dockerfile: [usecases/108-microservice-health-check/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/108-microservice-health-check/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `MS_HEALTH_CRON=*/5 * * * *`
- `SERVICE_LIST=service-a,service-b`

## Build & Run

```bash
cd usecases/108-microservice-health-check

# Build the image
docker build -t n8n-usecase-108 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-108 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-108

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-108:
    image: n8n-usecase-108
    container_name: n8n-usecase-108
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_108_data:/home/node/.n8n"]

volumes:
  n8n_usecase_108_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
