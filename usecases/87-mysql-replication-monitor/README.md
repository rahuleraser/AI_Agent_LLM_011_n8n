# 087 - MySQL Replication Monitor

> **Category:** Data & Database

Monitors MySQL replication lag and alerts on issues. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (5 min)"]
    B["Query Replication Status"]
    C["Alert DBA"]
    D["IF: Lag > threshold?"]
    E["Log Status"]
    F["Send Replication Report"]
    G["Notify On-call"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Lag poll |
| MySQL | Status query |
| IF | Lag check |
| Slack | DBA alert |
| SQLite | Status log |
| Email | Periodic report |

## Dockerfile

Dockerfile: [usecases/87-mysql-replication-monitor/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/87-mysql-replication-monitor/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `MYSQL_LAG_CRON=*/5 * * * *`
- `LAG_WARN_SECONDS=30`

## Build & Run

```bash
cd usecases/87-mysql-replication-monitor

# Build the image
docker build -t n8n-usecase-087 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-087 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-087

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-087:
    image: n8n-usecase-087
    container_name: n8n-usecase-087
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_087_data:/home/node/.n8n"]

volumes:
  n8n_usecase_087_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
