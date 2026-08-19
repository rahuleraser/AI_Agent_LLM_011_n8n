# 084 - ETL Nightly Pipeline

> **Category:** Data & Database

Runs nightly extract-transform-load jobs between sources. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Nightly)"]
    B["Extract from Sources"]
    C["Transform Data"]
    D["IF: Transforms pass?"]
    E["Load to Warehouse"]
    F["Retry Failed Steps"]
    G["Send Pipeline Report"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Nightly job |
| HTTP Request | Extract |
| Code | Transform |
| IF | Pass check |
| Postgres | Load data |
| Email | Pipeline report |

## Dockerfile

Dockerfile: [usecases/84-etl-nightly-pipeline/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/84-etl-nightly-pipeline/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `ETL_CRON=0 1 * * *`

## Build & Run

```bash
cd usecases/84-etl-nightly-pipeline

# Build the image
docker build -t n8n-usecase-084 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-084 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-084

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-084:
    image: n8n-usecase-084
    container_name: n8n-usecase-084
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_084_data:/home/node/.n8n"]

volumes:
  n8n_usecase_084_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
