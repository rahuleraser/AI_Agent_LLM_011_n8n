# 120 - AI Meeting Note Taker

> **Category:** AI & LLM

Transcribes meetings and extracts action items. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Calendar Trigger (Meeting)"]
    B["Fetch Recording / Transcript"]
    C["Extract Action Items"]
    D["IF: Transcript exists?"]
    E["Request Transcript"]
    F["Send Summary Email"]
    G["Archive Notes"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Calendar Trigger | Meeting end |
| HTTP Request | Transcript |
| AI LLM | Action extract |
| IF | Transcript check |
| Email | Summary send |
| Google Docs | Notes archive |

## Dockerfile

Dockerfile: [usecases/120-ai-meeting-note-taker/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/120-ai-meeting-note-taker/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `NOTES_WEBHOOK_PATH=meeting-notes`

## Build & Run

```bash
cd usecases/120-ai-meeting-note-taker

# Build the image
docker build -t n8n-usecase-120 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-120 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-120

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-120:
    image: n8n-usecase-120
    container_name: n8n-usecase-120
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_120_data:/home/node/.n8n"]

volumes:
  n8n_usecase_120_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
