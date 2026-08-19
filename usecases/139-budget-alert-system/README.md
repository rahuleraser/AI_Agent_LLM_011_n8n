# 139 - Budget Alert System

> **Category:** Finance & Accounting

Alerts department heads when budgets approach limits. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Weekly)"]
    B["Fetch Department Spend"]
    C["Alert Department Head"]
    D["IF: Over 80% budget?"]
    E["Log Spending"]
    F["Update Budget Dashboard"]
    G["Send Weekly Summary"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Weekly check |
| SQLite | Spend data |
| IF | Threshold check |
| Email | Head alert |
| Google Sheets | Budget dashboard |
| Slack | Finance notify |

## Dockerfile

Dockerfile: [usecases/139-budget-alert-system/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/139-budget-alert-system/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `BUDGET_CRON=0 9 * * 1`
- `BUDGET_WARN_PCT=80`

## Build & Run

```bash
cd usecases/139-budget-alert-system

# Build the image
docker build -t n8n-usecase-139 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-139 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-139

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-139:
    image: n8n-usecase-139
    container_name: n8n-usecase-139
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_139_data:/home/node/.n8n"]

volumes:
  n8n_usecase_139_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
