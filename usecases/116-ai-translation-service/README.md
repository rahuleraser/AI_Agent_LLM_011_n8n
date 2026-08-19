# 116 - AI Translation Service

> **Category:** AI & LLM

Translates content between languages automatically. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Translate)"]
    B["Detect Language"]
    C["Translate Text"]
    D["IF: Target set?"]
    E["Use Default Target"]
    F["Return Translation"]
    G["Log Requests"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Text inbound |
| Code | Language detect |
| IF | Target check |
| AI LLM | Translate |
| Webhook | Response send |
| SQLite | Request log |

## Dockerfile

Dockerfile: [usecases/116-ai-translation-service/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/116-ai-translation-service/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `TRANSLATE_WEBHOOK_PATH=translate`

## Build & Run

```bash
cd usecases/116-ai-translation-service

# Build the image
docker build -t n8n-usecase-116 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-116 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-116

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-116:
    image: n8n-usecase-116
    container_name: n8n-usecase-116
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_116_data:/home/node/.n8n"]

volumes:
  n8n_usecase_116_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
