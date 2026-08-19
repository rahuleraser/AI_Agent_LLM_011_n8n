# 011 - Slack Message Relay

> **Category:** Email & Communication

Relays messages between email and Slack channels automatically. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Slack Trigger (Channel)"]
    B["Detect Email Request"]
    C["Send Email via SMTP"]
    D["IF: Action required?"]
    E["Post to Support Channel"]
    F["Acknowledge to Slack"]
    G["Log Relay"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Slack Trigger | Channel events |
| Code | Detects intent |
| Email Send | Outbound mail |
| IF | Routes to channel |
| Slack | Sends message |
| Spreadsheet | Relay log |

## Dockerfile

Dockerfile: [usecases/11-slack-message-relay/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/11-slack-message-relay/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `WEBHOOK_PATH=slack-relay`
- `SLACK_CHANNEL=general`

## Build & Run

```bash
cd usecases/11-slack-message-relay

# Build the image
docker build -t n8n-usecase-011 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-011 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-011

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-011:
    image: n8n-usecase-011
    container_name: n8n-usecase-011
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_011_data:/home/node/.n8n"]

volumes:
  n8n_usecase_011_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
