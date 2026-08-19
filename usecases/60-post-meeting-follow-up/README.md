# 060 - Post-Meeting Follow-up

> **Category:** CRM & Sales

Sends follow-up emails with notes and action items after meetings. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Calendar Trigger (Ended)"]
    B["Fetch Meeting Notes"]
    C["Build Follow-up Email"]
    D["IF: Action items?"]
    E["List Action Items"]
    F["Send Summary Only"]
    G["Update CRM Deal"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Calendar Trigger | Meeting end |
| Code | Notes parsing |
| IF | Action check |
| Email | Follow-up send |
| CRM | Deal update |
| Spreadsheet | Notes store |

## Dockerfile

Dockerfile: [usecases/60-post-meeting-follow-up/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/60-post-meeting-follow-up/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `FOLLOWUP_WEBHOOK_PATH=meeting-followup`

## Build & Run

```bash
cd usecases/60-post-meeting-follow-up

# Build the image
docker build -t n8n-usecase-060 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-060 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-060

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-060:
    image: n8n-usecase-060
    container_name: n8n-usecase-060
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_060_data:/home/node/.n8n"]

volumes:
  n8n_usecase_060_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
