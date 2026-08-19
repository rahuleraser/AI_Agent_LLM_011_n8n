# 167 - Quote Generator for Blog

> **Category:** Content & Publishing

Adds relevant quotes to blog posts automatically. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Post)"]
    B["Extract Post Topic"]
    C["Insert Quote"]
    D["IF: Quote available?"]
    E["Leave Placeholder"]
    F["Update Post"]
    G["Log Quotations"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Post content |
| Code | Topic extract |
| IF | Quote match |
| Code | Quote insert |
| Google Docs | Post update |
| SQLite | Quote log |

## Dockerfile

Dockerfile: [usecases/167-quote-generator-for-blog/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/167-quote-generator-for-blog/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `QUOTE_WEBHOOK_PATH=quote`

## Build & Run

```bash
cd usecases/167-quote-generator-for-blog

# Build the image
docker build -t n8n-usecase-167 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-167 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-167

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-167:
    image: n8n-usecase-167
    container_name: n8n-usecase-167
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_167_data:/home/node/.n8n"]

volumes:
  n8n_usecase_167_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
