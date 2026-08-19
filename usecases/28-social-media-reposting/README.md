# 028 - Social Media Reposting

> **Category:** Social Media & Marketing

Cross-posts content between platforms to maximize reach. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (New Content)"]
    B["Normalize Content"]
    C["Repost to Targets"]
    D["IF: Platform supported?"]
    E["Skip Platform"]
    F["Log Cross-post"]
    G["Notify Poster"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Content event |
| Code | Normalizes content |
| Switch | Target platforms |
| IF | Support check |
| Social APIs | Cross-post |
| Spreadsheet | Repost log |

## Dockerfile

Dockerfile: [usecases/28-social-media-reposting/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/28-social-media-reposting/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `REPOST_WEBHOOK_PATH=repost`

## Build & Run

```bash
cd usecases/28-social-media-reposting

# Build the image
docker build -t n8n-usecase-028 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-028 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-028

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-028:
    image: n8n-usecase-028
    container_name: n8n-usecase-028
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_028_data:/home/node/.n8n"]

volumes:
  n8n_usecase_028_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
