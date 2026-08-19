# 186 - Weekly Report Generator

> **Category:** Monitoring & Alerts

Generates weekly activity reports for stakeholders. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Weekly)"]
    B["Collect Metrics"]
    C["Build Report"]
    D["IF: Data complete?"]
    E["Send Report"]
    F["Flag Missing Data"]
    G["Archive Report"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Weekly run |
| SQLite | Metric store |
| Code | Report build |
| IF | Completeness check |
| Email | Report send |
| Google Sheets | Archive |

## Dockerfile

Dockerfile: [usecases/186-weekly-report-generator/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/186-weekly-report-generator/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `WEEKLY_REPORT_CRON=0 16 * * 5`

## Build & Run

```bash
cd usecases/186-weekly-report-generator

# Build the image
docker build -t n8n-usecase-186 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-186 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-186

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-186:
    image: n8n-usecase-186
    container_name: n8n-usecase-186
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_186_data:/home/node/.n8n"]

volumes:
  n8n_usecase_186_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
