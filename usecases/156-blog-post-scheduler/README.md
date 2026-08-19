# 156 - Blog Post Scheduler

> **Category:** Content & Publishing

Schedules and publishes blog posts across platforms. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Google Sheets Trigger (Posts)"]
    B["Fetch Post Content"]
    C["Publish to CMS"]
    D["IF: Date reached?"]
    E["Queue for Later"]
    F["Notify Editor"]
    G["Update Status"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Google Sheets | Post queue |
| Code | Date check |
| IF | Publish branch |
| HTTP Request | CMS API |
| Email | Editor notify |
| Spreadsheet | Status update |

## Dockerfile

Dockerfile: [usecases/156-blog-post-scheduler/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/156-blog-post-scheduler/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `BLOG_CRON=0 11 * * *`

## Build & Run

```bash
cd usecases/156-blog-post-scheduler

# Build the image
docker build -t n8n-usecase-156 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-156 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-156

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-156:
    image: n8n-usecase-156
    container_name: n8n-usecase-156
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_156_data:/home/node/.n8n"]

volumes:
  n8n_usecase_156_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
