# 077 - Database Health Monitor

> **Category:** Data & Database

Checks database health metrics and alerts on anomalies. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (5 min)"]
    B["Query Health Metrics"]
    C["Alert DBA"]
    D["IF: Metric out of range?"]
    E["Log Healthy"]
    F["Update Dashboard"]
    G["Notify Team"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Health poll |
| Postgres | Metrics query |
| IF | Threshold check |
| Slack | DBA alert |
| Google Sheets | Dashboard |
| SQLite | Health log |

## Dockerfile

Dockerfile: [usecases/77-database-health-monitor/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/77-database-health-monitor/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `DB_HEALTH_CRON=*/5 * * * *`
- `LATENCY_WARN_MS=500`

## Build & Run

```bash
cd usecases/77-database-health-monitor

# Build the image
docker build -t n8n-usecase-077 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-077 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-077

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-077:
    image: n8n-usecase-077
    container_name: n8n-usecase-077
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_077_data:/home/node/.n8n"]

volumes:
  n8n_usecase_077_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
