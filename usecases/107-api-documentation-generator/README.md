# 107 - API Documentation Generator

> **Category:** Developer & DevOps

Generates API documentation from request logs. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Weekly)"]
    B["Fetch Request Logs"]
    C["Build Documentation"]
    D["IF: New endpoints?"]
    E["Add to Docs"]
    F["Skip Endpoints"]
    G["Publish Docs"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Weekly run |
| SQLite | Request logs |
| Code | Docs build |
| IF | New endpoint |
| Google Docs | Publish |
| Slack | API team notify |

## Dockerfile

Dockerfile: [usecases/107-api-documentation-generator/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/107-api-documentation-generator/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `DOCS_CRON=0 5 * * 1`

## Build & Run

```bash
cd usecases/107-api-documentation-generator

# Build the image
docker build -t n8n-usecase-107 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-107 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-107

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-107:
    image: n8n-usecase-107
    container_name: n8n-usecase-107
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_107_data:/home/node/.n8n"]

volumes:
  n8n_usecase_107_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
