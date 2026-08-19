# 162 - Press Release Distributor

> **Category:** Content & Publishing

Distributes press releases to media contacts. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Press Release)"]
    B["Load Contact List"]
    C["Send with PDF"]
    D["IF: Has release PDF?"]
    E["Send Text Version"]
    F["Track Opens"]
    G["Notify PR Team"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Release ready |
| Google Sheets | Media list |
| IF | Attachment check |
| Email | Send release |
| Email | Open tracking |
| Slack | PR team notify |

## Dockerfile

Dockerfile: [usecases/162-press-release-distributor/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/162-press-release-distributor/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `PRESS_WEBHOOK_PATH=press-release`

## Build & Run

```bash
cd usecases/162-press-release-distributor

# Build the image
docker build -t n8n-usecase-162 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-162 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-162

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-162:
    image: n8n-usecase-162
    container_name: n8n-usecase-162
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_162_data:/home/node/.n8n"]

volumes:
  n8n_usecase_162_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
