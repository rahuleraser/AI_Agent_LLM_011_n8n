# 172 - Smart Home Notifier

> **Category:** IoT & Smart Home

Sends notifications for smart home device events. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Device Event)"]
    B["Parse Event"]
    C["Send Security Alert"]
    D["IF: Security event?"]
    E["Log Routine Event"]
    F["Update Device State"]
    G["Notify Owner"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Device event |
| Code | Event parse |
| IF | Security check |
| Telegram | Security alert |
| SQLite | State store |
| Email | Owner notify |

## Dockerfile

Dockerfile: [usecases/172-smart-home-notifier/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/172-smart-home-notifier/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `SMART_HOME_WEBHOOK_PATH=device-event`

## Build & Run

```bash
cd usecases/172-smart-home-notifier

# Build the image
docker build -t n8n-usecase-172 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-172 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-172

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-172:
    image: n8n-usecase-172
    container_name: n8n-usecase-172
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_172_data:/home/node/.n8n"]

volumes:
  n8n_usecase_172_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
