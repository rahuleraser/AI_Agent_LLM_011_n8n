# 012 - Slack Channel Moderator

> **Category:** Email & Communication

Monitors Slack channels and alerts moderators about flagged messages. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Slack Trigger (New Message)"]
    B["Scan for Flags"]
    C["Post Alert to Moderators"]
    D["IF: Contains spam?"]
    E["Ignore Message"]
    F["Remove Message"]
    G["Notify Sender"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Slack Trigger | New message |
| Code | Flag scan |
| IF | Spam decision |
| Slack | Moderator alert |
| Slack | Removes message |
| SQLite | Flag history |

## Dockerfile

Dockerfile: [usecases/12-slack-channel-moderator/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/12-slack-channel-moderator/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `FLAG_KEYWORDS=spam,scam,urgent`

## Build & Run

```bash
cd usecases/12-slack-channel-moderator

# Build the image
docker build -t n8n-usecase-012 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-012 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-012

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-012:
    image: n8n-usecase-012
    container_name: n8n-usecase-012
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_012_data:/home/node/.n8n"]

volumes:
  n8n_usecase_012_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
