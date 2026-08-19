# 099 - Error Tracker (Sentry)

> **Category:** Developer & DevOps

Sends Sentry error events to the development channel. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Sentry Trigger (Error)"]
    B["Fetch Error Details"]
    C["Create Slack Alert"]
    D["IF: New issue?"]
    E["Update Issue Count"]
    F["Log Error"]
    G["Notify Dev Lead"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Sentry Trigger | New error |
| HTTP Request | Error data |
| IF | New issue check |
| Slack | Dev alert |
| SQLite | Error log |
| Email | Dev lead note |

## Dockerfile

Dockerfile: [usecases/99-error-tracker-sentry/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/99-error-tracker-sentry/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `SENTRY_WEBHOOK_PATH=sentry-event`

## Build & Run

```bash
cd usecases/99-error-tracker-sentry

# Build the image
docker build -t n8n-usecase-099 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-099 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-099

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-099:
    image: n8n-usecase-099
    container_name: n8n-usecase-099
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_099_data:/home/node/.n8n"]

volumes:
  n8n_usecase_099_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
