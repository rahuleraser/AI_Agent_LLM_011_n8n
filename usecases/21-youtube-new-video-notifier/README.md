# 021 - YouTube New Video Notifier

> **Category:** Social Media & Marketing

Detects new YouTube uploads and notifies the community. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["YouTube Trigger (New Video)"]
    B["Fetch Video Details"]
    C["Build Notification"]
    D["IF: Category matches?"]
    E["Post to Discord"]
    F["Post to Telegram"]
    G["Log Notifications"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| YouTube Trigger | New upload |
| HTTP Request | Video metadata |
| Discord | Channel post |
| Telegram | Direct message |
| IF | Category filter |
| SQLite | Notification log |

## Dockerfile

Dockerfile: [usecases/21-youtube-new-video-notifier/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/21-youtube-new-video-notifier/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | `n8n-nodes-telegram`, `n8n-nodes-discord` |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `YOUTUBE_CHANNEL=your-channel`

## Build & Run

```bash
cd usecases/21-youtube-new-video-notifier

# Build the image
docker build -t n8n-usecase-021 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-021 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-021

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-021:
    image: n8n-usecase-021
    container_name: n8n-usecase-021
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_021_data:/home/node/.n8n"]

volumes:
  n8n_usecase_021_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
