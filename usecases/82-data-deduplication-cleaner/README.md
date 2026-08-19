# 082 - Data Deduplication Cleaner

> **Category:** Data & Database

Finds and removes duplicate records across datasets. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Monthly)"]
    B["Scan for Duplicates"]
    C["Merge / Remove"]
    D["IF: Duplicate found?"]
    E["Keep Record"]
    F["Log Cleanup"]
    G["Email Cleanup Report"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Monthly scan |
| Postgres | Scan query |
| IF | Duplicate detect |
| Postgres | Merge action |
| SQLite | Cleanup log |
| Email | Report send |

## Dockerfile

Dockerfile: [usecases/82-data-deduplication-cleaner/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/82-data-deduplication-cleaner/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `DEDUPE_CRON=0 4 1 * *`

## Build & Run

```bash
cd usecases/82-data-deduplication-cleaner

# Build the image
docker build -t n8n-usecase-082 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-082 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-082

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-082:
    image: n8n-usecase-082
    container_name: n8n-usecase-082
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_082_data:/home/node/.n8n"]

volumes:
  n8n_usecase_082_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
