# 129 - Payroll Summary Reporter

> **Category:** Finance & Accounting

Compiles payroll summaries for the finance team. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Monthly)"]
    B["Fetch Timesheets"]
    C["Compute Totals"]
    D["IF: Discrepancy found?"]
    E["Flag for Review"]
    F["Generate Summary"]
    G["Email Report"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Monthly run |
| Google Sheets | Timesheets |
| Code | Total compute |
| IF | Discrepancy check |
| Google Sheets | Summary |
| Email | Report send |

## Dockerfile

Dockerfile: [usecases/129-payroll-summary-reporter/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/129-payroll-summary-reporter/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `PAYROLL_CRON=0 6 1 * *`

## Build & Run

```bash
cd usecases/129-payroll-summary-reporter

# Build the image
docker build -t n8n-usecase-129 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-129 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-129

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-129:
    image: n8n-usecase-129
    container_name: n8n-usecase-129
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_129_data:/home/node/.n8n"]

volumes:
  n8n_usecase_129_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
