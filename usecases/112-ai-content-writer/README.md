# 112 - AI Content Writer

> **Category:** AI & LLM

Generates blog and social content from a topic list. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Spreadsheet Trigger (Topics)"]
    B["Build Prompt"]
    C["Generate Article"]
    D["IF: Style selected?"]
    E["Generate Short Post"]
    F["Save Content"]
    G["Notify Editor"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Spreadsheet File | Topic list |
| AI LLM | Content generate |
| IF | Style branch |
| Google Docs | Save article |
| Google Sheets | Save posts |
| Slack | Editor notify |

## Dockerfile

Dockerfile: [usecases/112-ai-content-writer/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/112-ai-content-writer/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | `n8n-nodes-mcp` |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `CONTENT_WEBHOOK_PATH=content-gen`

## Build & Run

```bash
cd usecases/112-ai-content-writer

# Build the image
docker build -t n8n-usecase-112 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-112 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-112

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-112:
    image: n8n-usecase-112
    container_name: n8n-usecase-112
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_112_data:/home/node/.n8n"]

volumes:
  n8n_usecase_112_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
