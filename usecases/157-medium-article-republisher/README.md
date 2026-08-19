# 157 - Medium Article Republisher

> **Category:** Content & Publishing

Republishes blog posts to Medium automatically. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["RSS Trigger (New Post)"]
    B["Fetch Article HTML"]
    C["Upload with Images"]
    D["IF: Images included?"]
    E["Publish Text"]
    F["Update Canonical Link"]
    G["Log Republish"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| RSS Trigger | New post |
| HTTP Request | Article fetch |
| IF | Image check |
| Medium API | Publish |
| Code | Canonical link |
| SQLite | Republish log |

## Dockerfile

Dockerfile: [usecases/157-medium-article-republisher/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/157-medium-article-republisher/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `MEDIUM_WEBHOOK_PATH=medium-pub`

## Build & Run

```bash
cd usecases/157-medium-article-republisher

# Build the image
docker build -t n8n-usecase-157 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-157 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-157

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-157:
    image: n8n-usecase-157
    container_name: n8n-usecase-157
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_157_data:/home/node/.n8n"]

volumes:
  n8n_usecase_157_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
