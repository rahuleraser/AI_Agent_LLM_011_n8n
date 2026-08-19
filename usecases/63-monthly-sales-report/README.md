# 063 - Monthly Sales Report

> **Category:** CRM & Sales

Generates and emails a monthly sales performance report. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Monthly)"]
    B["Aggregate Sales Data"]
    C["Compute KPIs"]
    D["IF: Target met?"]
    E["Mark Achievement"]
    F["Show Gap"]
    G["Email Report"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Monthly run |
| SQLite | Sales data |
| Code | KPI compute |
| IF | Target check |
| Email | Report send |
| Google Sheets | Archive |

## Dockerfile

Dockerfile: [usecases/63-monthly-sales-report/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/63-monthly-sales-report/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `SALES_CRON=0 7 1 * *`
- `TARGET_REVENUE=100000`

## Build & Run

```bash
cd usecases/63-monthly-sales-report

# Build the image
docker build -t n8n-usecase-063 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-063 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-063

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-063:
    image: n8n-usecase-063
    container_name: n8n-usecase-063
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_063_data:/home/node/.n8n"]

volumes:
  n8n_usecase_063_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
