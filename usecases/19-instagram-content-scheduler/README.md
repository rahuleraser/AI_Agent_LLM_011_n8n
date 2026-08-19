# 019 - Instagram Content Scheduler

> **Category:** Social Media & Marketing

Schedules Instagram posts with images and captions. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Spreadsheet Trigger (Content)"]
    B["Prepare Image + Caption"]
    C["Schedule via Graph API"]
    D["IF: Business account?"]
    E["Flag Account Type"]
    F["Publish Post"]
    G["Log Schedule"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Spreadsheet File | Content plan |
| Code | Prepares media |
| Instagram | Publishes post |
| IF | Account check |
| Spreadsheet | Schedule log |
| Code | Caption format |

## Dockerfile

Dockerfile: [usecases/19-instagram-content-scheduler/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/19-instagram-content-scheduler/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `INSTAGRAM_WEBHOOK_PATH=ig-post`

## Build & Run

```bash
cd usecases/19-instagram-content-scheduler

# Build the image
docker build -t n8n-usecase-019 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-019 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-019

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-019:
    image: n8n-usecase-019
    container_name: n8n-usecase-019
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_019_data:/home/node/.n8n"]

volumes:
  n8n_usecase_019_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
