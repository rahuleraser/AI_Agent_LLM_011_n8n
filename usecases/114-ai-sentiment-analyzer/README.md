# 114 - AI Sentiment Analyzer

> **Category:** AI & LLM

Analyzes sentiment of reviews and messages at scale. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Text)"]
    B["Classify Sentiment"]
    C["Alert Support"]
    D["IF: Negative score?"]
    E["Tag Positive / Neutral"]
    F["Store Score"]
    G["Update Dashboard"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Text inbound |
| AI LLM | Sentiment score |
| IF | Negative branch |
| Slack | Support alert |
| Google Sheets | Score store |
| SQLite | Analysis log |

## Dockerfile

Dockerfile: [usecases/114-ai-sentiment-analyzer/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/114-ai-sentiment-analyzer/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `SENTIMENT_WEBHOOK_PATH=sentiment`

## Build & Run

```bash
cd usecases/114-ai-sentiment-analyzer

# Build the image
docker build -t n8n-usecase-114 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-114 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-114

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-114:
    image: n8n-usecase-114
    container_name: n8n-usecase-114
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_114_data:/home/node/.n8n"]

volumes:
  n8n_usecase_114_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
