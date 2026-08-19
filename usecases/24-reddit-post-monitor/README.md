# 024 - Reddit Post Monitor

> **Category:** Social Media & Marketing

Tracks Reddit mentions of your brand and routes them to the team. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Reddit Trigger (New Post)"]
    B["Classify Post Sentiment"]
    C["Notify Community Manager"]
    D["IF: Brand mentioned?"]
    E["Log to Monitor Sheet"]
    F["Reply if Needed"]
    G["Score Sentiment"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Reddit Trigger | New posts |
| Code | Sentiment score |
| IF | Brand mention |
| Slack | Community alert |
| Google Sheets | Monitor log |
| Code | Reply draft |

## Dockerfile

Dockerfile: [usecases/24-reddit-post-monitor/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/24-reddit-post-monitor/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `REDDIT_WEBHOOK_PATH=reddit-monitor`
- `BRAND_KEYWORDS=yourbrand`

## Build & Run

```bash
cd usecases/24-reddit-post-monitor

# Build the image
docker build -t n8n-usecase-024 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-024 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-024

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-024:
    image: n8n-usecase-024
    container_name: n8n-usecase-024
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_024_data:/home/node/.n8n"]

volumes:
  n8n_usecase_024_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
