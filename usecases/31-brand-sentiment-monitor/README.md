# 031 - Brand Sentiment Monitor

> **Category:** Social Media & Marketing

Tracks brand sentiment on social media and reports trends. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Hourly)"]
    B["Collect Social Mentions"]
    C["Analyze Sentiment"]
    D["IF: Sentiment shift?"]
    E["Generate Alert"]
    F["Update Scoreboard"]
    G["Email Weekly Sentiment"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Collection |
| HTTP Request | Mention APIs |
| AI | Sentiment analysis |
| IF | Shift detection |
| Google Sheets | Scoreboard |
| Email | Weekly report |

## Dockerfile

Dockerfile: [usecases/31-brand-sentiment-monitor/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/31-brand-sentiment-monitor/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `SENTIMENT_CRON=0 * * * *`
- `BRAND_ALIAS=yourbrand`

## Build & Run

```bash
cd usecases/31-brand-sentiment-monitor

# Build the image
docker build -t n8n-usecase-031 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-031 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-031

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-031:
    image: n8n-usecase-031
    container_name: n8n-usecase-031
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_031_data:/home/node/.n8n"]

volumes:
  n8n_usecase_031_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
