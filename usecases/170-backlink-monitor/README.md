# 170 - Backlink Monitor

> **Category:** Content & Publishing

Monitors new backlinks to your content. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Weekly)"]
    B["Fetch Backlink Data"]
    C["Add to Tracker"]
    D["IF: New backlink?"]
    E["Skip Duplicate"]
    F["Rate Link Quality"]
    G["Notify SEO Team"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Weekly scan |
| HTTP Request | Backlink API |
| IF | New link check |
| Google Sheets | Backlink tracker |
| Code | Quality score |
| Slack | SEO team notify |

## Dockerfile

Dockerfile: [usecases/170-backlink-monitor/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/170-backlink-monitor/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `BACKLINK_CRON=0 7 * * 1`

## Build & Run

```bash
cd usecases/170-backlink-monitor

# Build the image
docker build -t n8n-usecase-170 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-170 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-170

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-170:
    image: n8n-usecase-170
    container_name: n8n-usecase-170
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_170_data:/home/node/.n8n"]

volumes:
  n8n_usecase_170_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
