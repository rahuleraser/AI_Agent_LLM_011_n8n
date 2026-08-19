# 160 - Content Idea Collector

> **Category:** Content & Publishing

Collects content ideas from multiple sources into one board. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Idea)"]
    B["Normalize Idea"]
    C["Skip Idea"]
    D["IF: Duplicate?"]
    E["Add to Ideas Board"]
    F["Tag by Topic"]
    G["Notify Editor"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Idea inbound |
| Code | Normalize |
| IF | Dup check |
| Baserow | Ideas board |
| Code | Topic tags |
| Slack | Editor notify |

## Dockerfile

Dockerfile: [usecases/160-content-idea-collector/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/160-content-idea-collector/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `IDEA_WEBHOOK_PATH=idea`

## Build & Run

```bash
cd usecases/160-content-idea-collector

# Build the image
docker build -t n8n-usecase-160 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-160 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-160

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-160:
    image: n8n-usecase-160
    container_name: n8n-usecase-160
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_160_data:/home/node/.n8n"]

volumes:
  n8n_usecase_160_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
