# 123 - AI Data Extractor

> **Category:** AI & LLM

Extracts structured data from unstructured documents. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Document)"]
    B["Send Document to AI"]
    C["Map to Database"]
    D["IF: Fields extracted?"]
    E["Flag Extraction Error"]
    F["Store Data"]
    G["Notify User"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Document in |
| AI LLM | Field extract |
| IF | Success check |
| Postgres | Store data |
| Slack | Error flag |
| Email | User notify |

## Dockerfile

Dockerfile: [usecases/123-ai-data-extractor/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/123-ai-data-extractor/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `EXTRACT_WEBHOOK_PATH=ai-extract`

## Build & Run

```bash
cd usecases/123-ai-data-extractor

# Build the image
docker build -t n8n-usecase-123 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-123 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-123

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-123:
    image: n8n-usecase-123
    container_name: n8n-usecase-123
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_123_data:/home/node/.n8n"]

volumes:
  n8n_usecase_123_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
