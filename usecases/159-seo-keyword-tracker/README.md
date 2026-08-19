# 159 - SEO Keyword Tracker

> **Category:** Content & Publishing

Tracks keyword rankings and reports movements. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Weekly)"]
    B["Fetch Rankings"]
    C["Mark Green"]
    D["IF: Rank improved?"]
    E["Mark Red"]
    F["Update Tracker"]
    G["Email SEO Report"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Weekly run |
| HTTP Request | Rank API |
| IF | Change check |
| Google Sheets | Rank tracker |
| Email | SEO report |
| Slack | SEO team notify |

## Dockerfile

Dockerfile: [usecases/159-seo-keyword-tracker/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/159-seo-keyword-tracker/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `SEO_CRON=0 8 * * 1`

## Build & Run

```bash
cd usecases/159-seo-keyword-tracker

# Build the image
docker build -t n8n-usecase-159 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-159 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-159

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-159:
    image: n8n-usecase-159
    container_name: n8n-usecase-159
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_159_data:/home/node/.n8n"]

volumes:
  n8n_usecase_159_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
