# 025 - Social Mention Tracker

> **Category:** Social Media & Marketing

Monitors brand mentions across social platforms in one dashboard. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (30 min)"]
    B["Query Mention APIs"]
    C["Aggregate Mentions"]
    D["IF: Sentiment negative?"]
    E["Alert Team"]
    F["Store Mention"]
    G["Update Dashboard"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Polling |
| HTTP Request | Multiple APIs |
| Code | Aggregates mentions |
| IF | Negative flag |
| Slack | Team alert |
| Google Sheets | Dashboard |

## Dockerfile

Dockerfile: [usecases/25-social-mention-tracker/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/25-social-mention-tracker/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `MENTION_CRON=*/30 * * * *`
- `BRAND_NAME=yourbrand`

## Build & Run

```bash
cd usecases/25-social-mention-tracker

# Build the image
docker build -t n8n-usecase-025 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-025 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-025

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-025:
    image: n8n-usecase-025
    container_name: n8n-usecase-025
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_025_data:/home/node/.n8n"]

volumes:
  n8n_usecase_025_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
