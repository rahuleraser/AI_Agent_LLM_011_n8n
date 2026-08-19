# 187 - Monthly KPI Digest

> **Category:** Monitoring & Alerts

Sends a monthly KPI digest to leadership. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Monthly)"]
    B["Compute Monthly KPIs"]
    C["Build Digest"]
    D["IF: KPI vs target?"]
    E["Add Variance Note"]
    F["Standard Format"]
    G["Email Digest"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Monthly run |
| SQLite | KPI data |
| Code | Variance compute |
| IF | Target check |
| Email | Digest send |
| Google Sheets | KPI log |

## Dockerfile

Dockerfile: [usecases/187-monthly-kpi-digest/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/187-monthly-kpi-digest/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `KPI_DIGEST_CRON=0 9 1 * *`

## Build & Run

```bash
cd usecases/187-monthly-kpi-digest

# Build the image
docker build -t n8n-usecase-187 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-187 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-187

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-187:
    image: n8n-usecase-187
    container_name: n8n-usecase-187
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_187_data:/home/node/.n8n"]

volumes:
  n8n_usecase_187_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
