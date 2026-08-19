# 085 - MongoDB Collection Sync

> **Category:** Data & Database

Syncs collections between MongoDB databases. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Hourly)"]
    B["Read Source Collection"]
    C["Write to Target"]
    D["IF: Documents changed?"]
    E["Skip Unchanged"]
    F["Log Sync"]
    G["Alert on Errors"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Hourly sync |
| MongoDB | Source read |
| IF | Change detection |
| MongoDB | Target write |
| SQLite | Sync log |
| Slack | Error alert |

## Dockerfile

Dockerfile: [usecases/85-mongodb-collection-sync/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/85-mongodb-collection-sync/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | `n8n-nodes-mongodb` |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `MONGO_SYNC_CRON=0 * * * *`
- `MONGO_SOURCE=mongodb://source`

## Build & Run

```bash
cd usecases/85-mongodb-collection-sync

# Build the image
docker build -t n8n-usecase-085 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-085 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-085

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-085:
    image: n8n-usecase-085
    container_name: n8n-usecase-085
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_085_data:/home/node/.n8n"]

volumes:
  n8n_usecase_085_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
