# 140 - Financial KPI Dashboard

> **Category:** Finance & Accounting

Updates a financial KPI dashboard from multiple sources. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Daily)"]
    B["Collect Financial KPIs"]
    C["Flag Missing Data"]
    D["IF: KPI missing?"]
    E["Compute Metrics"]
    F["Update Dashboard"]
    G["Email KPI Summary"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Daily run |
| SQLite | KPI data |
| Code | Metric compute |
| IF | Missing check |
| Google Sheets | Dashboard |
| Email | KPI summary |

## Dockerfile

Dockerfile: [usecases/140-financial-kpi-dashboard/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/140-financial-kpi-dashboard/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `KPI_CRON=0 6 * * *`

## Build & Run

```bash
cd usecases/140-financial-kpi-dashboard

# Build the image
docker build -t n8n-usecase-140 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-140 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-140

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-140:
    image: n8n-usecase-140
    container_name: n8n-usecase-140
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_140_data:/home/node/.n8n"]

volumes:
  n8n_usecase_140_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
