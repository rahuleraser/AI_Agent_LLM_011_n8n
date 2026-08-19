# 029 - Viral Content Curator

> **Category:** Social Media & Marketing

Curates trending content from sources and schedules reposts. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["RSS / Cron Trigger"]
    B["Fetch Trending Items"]
    C["Score Viral Potential"]
    D["IF: Score high?"]
    E["Queue for Posting"]
    F["Archive Item"]
    G["Notify Curator"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| RSS Trigger | Trending feed |
| Code | Scores content |
| IF | High-score queue |
| Spreadsheet | Posting queue |
| Slack | Curator alert |
| Code | Archive logic |

## Dockerfile

Dockerfile: [usecases/29-viral-content-curator/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/29-viral-content-curator/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `CURATE_CRON=0 6 * * *`
- `MIN_VIRAL_SCORE=70`

## Build & Run

```bash
cd usecases/29-viral-content-curator

# Build the image
docker build -t n8n-usecase-029 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-029 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-029

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-029:
    image: n8n-usecase-029
    container_name: n8n-usecase-029
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_029_data:/home/node/.n8n"]

volumes:
  n8n_usecase_029_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
