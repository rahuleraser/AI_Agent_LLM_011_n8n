# 002 - Gmail Auto-Responder

> **Category:** Email & Communication

Automatically replies to common emails with templates based on detected intent. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Gmail Trigger (Unread)"]
    B["Detect Intent (Keywords)"]
    C["Pick Template by Intent"]
    D["IF: Needs human review?"]
    E["Send Template Reply"]
    F["Forward to Support Team"]
    G["Flag as Handled"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Gmail Trigger | Listens for unread |
| Code | Detects intent |
| Switch | Selects template |
| Gmail Send | Replies automatically |
| Gmail | Forwards edge cases |
| Spreadsheet | Tracks replies |

## Dockerfile

Dockerfile: [usecases/02-gmail-auto-responder/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/02-gmail-auto-responder/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `WEBHOOK_PATH=auto-respond`
- `REPLY_LIMIT_DAILY=50`

## Build & Run

```bash
cd usecases/02-gmail-auto-responder

# Build the image
docker build -t n8n-usecase-002 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-002 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-002

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-002:
    image: n8n-usecase-002
    container_name: n8n-usecase-002
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_002_data:/home/node/.n8n"]

volumes:
  n8n_usecase_002_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
