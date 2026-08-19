# 064 - Quota vs Actual Tracker

> **Category:** CRM & Sales

Tracks sales rep quota attainment against actuals in real time. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Daily)"]
    B["Fetch Rep Quotas"]
    C["Fetch Actual Sales"]
    D["IF: Below 80%?"]
    E["Alert Rep + Manager"]
    F["Log Progress"]
    G["Update Scorecard"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Daily sync |
| CRM API | Quota data |
| CRM API | Actual sales |
| IF | Warning threshold |
| Email | Rep alert |
| Google Sheets | Scorecard |

## Dockerfile

Dockerfile: [usecases/64-quota-vs-actual-tracker/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/64-quota-vs-actual-tracker/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `QUOTA_CRON=0 8 * * *`
- `QUOTA_WARN_PCT=80`

## Build & Run

```bash
cd usecases/64-quota-vs-actual-tracker

# Build the image
docker build -t n8n-usecase-064 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-064 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-064

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-064:
    image: n8n-usecase-064
    container_name: n8n-usecase-064
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_064_data:/home/node/.n8n"]

volumes:
  n8n_usecase_064_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
