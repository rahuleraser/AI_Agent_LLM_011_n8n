# 020 - LinkedIn Article Publisher

> **Category:** Social Media & Marketing

Cross-publishes blog content to LinkedIn as articles. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["RSS Trigger (New Blog Post)"]
    B["Extract Article Content"]
    C["Convert to LinkedIn Format"]
    D["IF: Content too long?"]
    E["Trim and Publish"]
    F["Publish Full Article"]
    G["Log Publishing"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| RSS Trigger | New post |
| Code | Extracts content |
| LinkedIn | Publishes article |
| IF | Length check |
| Spreadsheet | Publish log |
| Code | Formatting |

## Dockerfile

Dockerfile: [usecases/20-linkedin-article-publisher/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/20-linkedin-article-publisher/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `LINKEDIN_WEBHOOK_PATH=li-publish`

## Build & Run

```bash
cd usecases/20-linkedin-article-publisher

# Build the image
docker build -t n8n-usecase-020 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-020 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-020

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-020:
    image: n8n-usecase-020
    container_name: n8n-usecase-020
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_020_data:/home/node/.n8n"]

volumes:
  n8n_usecase_020_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
