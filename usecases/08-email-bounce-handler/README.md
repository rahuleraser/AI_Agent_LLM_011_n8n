# 008 - Email Bounce Handler

> **Category:** Email & Communication

Processes hard bounces and auto-removes invalid addresses from lists. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Email Webhook (Bounce)"]
    B["Classify Bounce Type"]
    C["Remove Address from List"]
    D["IF: Hard or Soft?"]
    E["Retry with Backoff"]
    F["Update List Status"]
    G["Notify List Owner"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Bounce event |
| Code | Classifies bounce |
| IF | Hard vs soft |
| Email Send | Retry logic |
| Spreadsheet | List updates |
| SQLite | Bounce history |

## Dockerfile

Dockerfile: [usecases/08-email-bounce-handler/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/08-email-bounce-handler/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | `n8n-nodes-sqlite` |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `WEBHOOK_PATH=bounce`
- `RETRY_BACKOFF_HOURS=24`

## Build & Run

```bash
cd usecases/08-email-bounce-handler

# Build the image
docker build -t n8n-usecase-008 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-008 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-008

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-008:
    image: n8n-usecase-008
    container_name: n8n-usecase-008
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_008_data:/home/node/.n8n"]

volumes:
  n8n_usecase_008_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
