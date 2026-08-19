# 062 - Sales Pipeline Dashboard

> **Category:** CRM & Sales

Keeps a live sales pipeline dashboard updated in Google Sheets. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (15 min)"]
    B["Fetch All Deals"]
    C["Update Dashboard Row"]
    D["IF: Stage changed?"]
    E["Log Deal"]
    F["Refresh Chart"]
    G["Notify Sales Team"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Refresh |
| CRM API | Deal fetch |
| IF | Change detection |
| Google Sheets | Dashboard |
| Code | Chart data |
| Slack | Team update |

## Dockerfile

Dockerfile: [usecases/62-sales-pipeline-dashboard/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/62-sales-pipeline-dashboard/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `PIPELINE_CRON=*/15 * * * *`

## Build & Run

```bash
cd usecases/62-sales-pipeline-dashboard

# Build the image
docker build -t n8n-usecase-062 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-062 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-062

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-062:
    image: n8n-usecase-062
    container_name: n8n-usecase-062
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_062_data:/home/node/.n8n"]

volumes:
  n8n_usecase_062_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
