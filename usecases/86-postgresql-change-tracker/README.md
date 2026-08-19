# 086 - PostgreSQL Change Tracker

> **Category:** Data & Database

Tracks changes to PostgreSQL tables and logs them. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Postgres Trigger (Change)"]
    B["Capture Changed Rows"]
    C["Log Insert / Update"]
    D["IF: Change type?"]
    E["Log Delete"]
    F["Store Change Feed"]
    G["Notify Subscribers"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Postgres Trigger | Table change |
| Postgres | Row capture |
| IF | Change type |
| SQLite | Change feed |
| Webhook | Subscriber push |
| Slack | Change alert |

## Dockerfile

Dockerfile: [usecases/86-postgresql-change-tracker/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/86-postgresql-change-tracker/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `PG_CHANGE_WEBHOOK_PATH=pg-change`

## Build & Run

```bash
cd usecases/86-postgresql-change-tracker

# Build the image
docker build -t n8n-usecase-086 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-086 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-086

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-086:
    image: n8n-usecase-086
    container_name: n8n-usecase-086
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_086_data:/home/node/.n8n"]

volumes:
  n8n_usecase_086_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
