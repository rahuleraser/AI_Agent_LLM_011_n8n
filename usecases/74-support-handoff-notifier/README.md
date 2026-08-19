# 074 - Support Handoff Notifier

> **Category:** Support & Customer Service

Notifies the right team when a ticket changes ownership. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Ticket Trigger (Assignee)"]
    B["Fetch New Assignee"]
    C["Notify New Team"]
    D["IF: Different team?"]
    E["Log Handoff"]
    F["Add Handoff Note"]
    G["Update Ticket History"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Ticket Trigger | Assignee change |
| Code | Team detect |
| IF | Team change |
| Slack | Team notify |
| Zendesk | Internal note |
| SQLite | Handoff log |

## Dockerfile

Dockerfile: [usecases/74-support-handoff-notifier/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/74-support-handoff-notifier/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `HANDOFF_WEBHOOK_PATH=handoff`

## Build & Run

```bash
cd usecases/74-support-handoff-notifier

# Build the image
docker build -t n8n-usecase-074 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-074 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-074

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-074:
    image: n8n-usecase-074
    container_name: n8n-usecase-074
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_074_data:/home/node/.n8n"]

volumes:
  n8n_usecase_074_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
