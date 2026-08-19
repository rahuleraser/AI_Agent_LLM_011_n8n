# 166 - YouTube to Blog Converter

> **Category:** Content & Publishing

Turns YouTube videos into blog post drafts. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["YouTube Trigger (Video)"]
    B["Fetch Transcript"]
    C["Generate Blog Draft"]
    D["IF: Transcript length ok?"]
    E["Skip Video"]
    F["Save Draft"]
    G["Notify Editor"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| YouTube Trigger | New video |
| HTTP Request | Transcript |
| AI LLM | Draft generate |
| IF | Length check |
| Google Docs | Save draft |
| Slack | Editor notify |

## Dockerfile

Dockerfile: [usecases/166-youtube-to-blog-converter/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/166-youtube-to-blog-converter/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | `n8n-nodes-mcp` |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `YT_TO_BLOG_WEBHOOK_PATH=yt-blog`

## Build & Run

```bash
cd usecases/166-youtube-to-blog-converter

# Build the image
docker build -t n8n-usecase-166 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-166 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-166

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-166:
    image: n8n-usecase-166
    container_name: n8n-usecase-166
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_166_data:/home/node/.n8n"]

volumes:
  n8n_usecase_166_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
