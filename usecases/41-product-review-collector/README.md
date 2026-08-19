# 041 - Product Review Collector

> **Category:** E-commerce & Retail

Collects product reviews from multiple platforms into one place. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Daily)"]
    B["Fetch New Reviews"]
    C["Alert Support Team"]
    D["IF: Review rating low?"]
    E["Add to Review DB"]
    F["Reply to Reviewer"]
    G["Update Review Dashboard"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Review pull |
| HTTP Request | Platform APIs |
| IF | Low rating flag |
| MongoDB | Review store |
| Email | Reply drafting |
| Google Sheets | Dashboard |

## Dockerfile

Dockerfile: [usecases/41-product-review-collector/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/41-product-review-collector/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | `n8n-nodes-mongodb` |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `REVIEW_CRON=0 6 * * *`
- `LOW_RATING=2`

## Build & Run

```bash
cd usecases/41-product-review-collector

# Build the image
docker build -t n8n-usecase-041 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-041 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-041

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-041:
    image: n8n-usecase-041
    container_name: n8n-usecase-041
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_041_data:/home/node/.n8n"]

volumes:
  n8n_usecase_041_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
