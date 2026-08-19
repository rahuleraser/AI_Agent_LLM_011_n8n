# 022 - TikTok Trend Watcher

> **Category:** Social Media & Marketing

Watches TikTok hashtags and collects trending video insights. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Hourly)"]
    B["Query Hashtag Feed"]
    C["Collect Video Stats"]
    D["IF: Above threshold?"]
    E["Save to Trend Sheet"]
    F["Skip Video"]
    G["Notify Marketer"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Polling |
| HTTP Request | TikTok API |
| Code | Collects stats |
| IF | Threshold check |
| Google Sheets | Trend store |
| Slack | Marketer alert |

## Dockerfile

Dockerfile: [usecases/22-tiktok-trend-watcher/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/22-tiktok-trend-watcher/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `TT_TREND_CRON=0 * * * *`
- `TT_HASHTAG=trending`

## Build & Run

```bash
cd usecases/22-tiktok-trend-watcher

# Build the image
docker build -t n8n-usecase-022 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-022 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-022

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-022:
    image: n8n-usecase-022
    container_name: n8n-usecase-022
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_022_data:/home/node/.n8n"]

volumes:
  n8n_usecase_022_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
