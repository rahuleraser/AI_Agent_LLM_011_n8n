# 102 - Deploy Status Reporter

> **Category:** Developer & DevOps

Reports deployment status after each release. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Deploy)"]
    B["Fetch Deploy Result"]
    C["Post Success Report"]
    D["IF: Deploy success?"]
    E["Post Failure Report"]
    F["Update Status Page"]
    G["Notify Stakeholders"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Deploy event |
| HTTP Request | Deploy API |
| IF | Result check |
| Slack | Success post |
| Slack | Failure post |
| Email | Stakeholder notify |

## Dockerfile

Dockerfile: [usecases/102-deploy-status-reporter/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/102-deploy-status-reporter/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `DEPLOY_WEBHOOK_PATH=deploy-status`

## Build & Run

```bash
cd usecases/102-deploy-status-reporter

# Build the image
docker build -t n8n-usecase-102 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-102 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-102

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-102:
    image: n8n-usecase-102
    container_name: n8n-usecase-102
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_102_data:/home/node/.n8n"]

volumes:
  n8n_usecase_102_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
