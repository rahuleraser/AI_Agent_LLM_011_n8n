# 169 - Content Calendar Syncer

> **Category:** Content & Publishing

Syncs content calendars between teams and tools. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Daily)"]
    B["Fetch Calendar Events"]
    C["Update All Calendars"]
    D["IF: Date changed?"]
    E["Log Changes"]
    F["Notify Team"]
    G["Send Daily Digest"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Daily sync |
| Google Calendar | Events |
| IF | Change detection |
| Google Sheets | Calendar store |
| Slack | Team notify |
| Email | Digest send |

## Dockerfile

Dockerfile: [usecases/169-content-calendar-syncer/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/169-content-calendar-syncer/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `CALENDAR_SYNC_CRON=0 6 * * *`

## Build & Run

```bash
cd usecases/169-content-calendar-syncer

# Build the image
docker build -t n8n-usecase-169 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-169 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-169

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-169:
    image: n8n-usecase-169
    container_name: n8n-usecase-169
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_169_data:/home/node/.n8n"]

volumes:
  n8n_usecase_169_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
