# 095 - CI/CD Status Notifier

> **Category:** Developer & DevOps

Sends build status notifications after each pipeline run. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Pipeline)"]
    B["Fetch Build Status"]
    C["Alert Developers"]
    D["IF: Build failed?"]
    E["Post Success"]
    F["Log Builds"]
    G["Notify Team Channel"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Pipeline event |
| HTTP Request | Build API |
| IF | Failure check |
| Slack | Failure alert |
| Slack | Success post |
| SQLite | Build log |

## Dockerfile

Dockerfile: [usecases/95-ci-cd-status-notifier/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/95-ci-cd-status-notifier/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `CI_WEBHOOK_PATH=ci-status`

## Build & Run

```bash
cd usecases/95-ci-cd-status-notifier

# Build the image
docker build -t n8n-usecase-095 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-095 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-095

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-095:
    image: n8n-usecase-095
    container_name: n8n-usecase-095
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_095_data:/home/node/.n8n"]

volumes:
  n8n_usecase_095_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
