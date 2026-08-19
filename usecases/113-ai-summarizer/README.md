# 113 - AI Summarizer

> **Category:** AI & LLM

Summarizes long documents and emails automatically. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Document)"]
    B["Extract Text"]
    C["Summarize Chunks"]
    D["IF: Length over limit?"]
    E["Summarize Full Text"]
    F["Return Summary"]
    G["Log Usage"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Document in |
| Code | Text extract |
| IF | Length check |
| AI LLM | Chunk summary |
| AI LLM | Full summary |
| SQLite | Usage log |

## Dockerfile

Dockerfile: [usecases/113-ai-summarizer/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/113-ai-summarizer/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `SUMMARIZE_WEBHOOK_PATH=summary`
- `CHUNK_SIZE=4000`

## Build & Run

```bash
cd usecases/113-ai-summarizer

# Build the image
docker build -t n8n-usecase-113 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-113 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-113

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-113:
    image: n8n-usecase-113
    container_name: n8n-usecase-113
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_113_data:/home/node/.n8n"]

volumes:
  n8n_usecase_113_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
