# 200 - Data Warehouse Syncer

> **Category:** API Integration & Automation

Syncs data from sources into a data warehouse. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Hourly)"]
    B["Pull Source Data"]
    C["Update Schema"]
    D["IF: Schema changed?"]
    E["Sync Data"]
    F["Log Sync State"]
    G["Alert on Failure"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Sync schedule |
| HTTP Request | Source pull |
| IF | Schema check |
| Postgres | Load data |
| Baserow | Warehouse tables |
| Slack | Failure alert |

## Dockerfile

Dockerfile: [usecases/200-data-warehouse-syncer/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/200-data-warehouse-syncer/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | `n8n-nodes-baserow` |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `DW_SYNC_CRON=0 * * * *`

## Build & Run

```bash
cd usecases/200-data-warehouse-syncer

# Build the image
docker build -t n8n-usecase-200 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-200 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-200

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-200:
    image: n8n-usecase-200
    container_name: n8n-usecase-200
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_200_data:/home/node/.n8n"]

volumes:
  n8n_usecase_200_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
