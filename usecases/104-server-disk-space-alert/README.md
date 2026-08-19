# 104 - Server Disk Space Alert

> **Category:** Developer & DevOps

Alerts when server disk space runs low. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Hourly)"]
    B["Query Disk Usage"]
    C["Alert Sysadmin"]
    D["IF: Above 90%?"]
    E["Log Usage"]
    F["Send Weekly Report"]
    G["Clean Temp Files"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Usage poll |
| HTTP Request | Metrics API |
| IF | Threshold check |
| Slack | Sysadmin alert |
| SQLite | Usage log |
| Email | Weekly report |

## Dockerfile

Dockerfile: [usecases/104-server-disk-space-alert/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/104-server-disk-space-alert/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `DISK_CRON=0 * * * *`
- `DISK_WARN_PCT=90`

## Build & Run

```bash
cd usecases/104-server-disk-space-alert

# Build the image
docker build -t n8n-usecase-104 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-104 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-104

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-104:
    image: n8n-usecase-104
    container_name: n8n-usecase-104
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_104_data:/home/node/.n8n"]

volumes:
  n8n_usecase_104_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
