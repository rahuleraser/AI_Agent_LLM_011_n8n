# 183 - Business Hours Tracker

> **Category:** Monitoring & Alerts

Tracks service availability during business hours. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (5 min)"]
    B["Check Service Status"]
    C["Log Availability"]
    D["IF: Within business hours?"]
    E["Skip Check"]
    F["Compute Uptime"]
    G["Email Weekly Uptime"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Status poll |
| HTTP Request | Service check |
| IF | Hours window |
| SQLite | Availability log |
| Code | Uptime compute |
| Email | Uptime report |

## Dockerfile

Dockerfile: [usecases/183-business-hours-tracker/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/183-business-hours-tracker/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `AVAIL_CRON=*/5 * * * *`
- `BIZ_HOURS=9-17`

## Build & Run

```bash
cd usecases/183-business-hours-tracker

# Build the image
docker build -t n8n-usecase-183 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-183 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-183

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-183:
    image: n8n-usecase-183
    container_name: n8n-usecase-183
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_183_data:/home/node/.n8n"]

volumes:
  n8n_usecase_183_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
