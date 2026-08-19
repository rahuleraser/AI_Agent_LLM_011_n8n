# 069 - Slack Support Channel

> **Category:** Support & Customer Service

Posts new support tickets to a Slack channel for awareness. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Zendesk Trigger (Ticket)"]
    B["Build Ticket Summary"]
    C["Post to Support Channel"]
    D["IF: VIP customer?"]
    E["Mention Support Lead"]
    F["Post Standard Alert"]
    G["Log Posted Tickets"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Zendesk Trigger | Ticket event |
| Code | Summary build |
| Slack | Channel post |
| IF | VIP branch |
| Slack | Lead mention |
| SQLite | Post log |

## Dockerfile

Dockerfile: [usecases/69-slack-support-channel/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/69-slack-support-channel/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `SUPPORT_CHANNEL=support`

## Build & Run

```bash
cd usecases/69-slack-support-channel

# Build the image
docker build -t n8n-usecase-069 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-069 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-069

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-069:
    image: n8n-usecase-069
    container_name: n8n-usecase-069
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_069_data:/home/node/.n8n"]

volumes:
  n8n_usecase_069_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
