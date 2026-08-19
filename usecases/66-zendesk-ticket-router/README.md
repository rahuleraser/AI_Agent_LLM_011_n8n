# 066 - Zendesk Ticket Router

> **Category:** Support & Customer Service

Routes Zendesk tickets to teams by category and priority. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Zendesk Trigger (Ticket)"]
    B["Classify Ticket Category"]
    C["Assign Urgent Queue"]
    D["IF: Urgent priority?"]
    E["Assign Standard Queue"]
    F["Set Ticket Fields"]
    G["Notify Agent"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Zendesk Trigger | New ticket |
| Code | Category detect |
| IF | Priority branch |
| Zendesk | Queue assign |
| Zendesk | Field update |
| Discord | Agent notify |

## Dockerfile

Dockerfile: [usecases/66-zendesk-ticket-router/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/66-zendesk-ticket-router/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | `n8n-nodes-discord` |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `TICKET_WEBHOOK_PATH=ticket-route`

## Build & Run

```bash
cd usecases/66-zendesk-ticket-router

# Build the image
docker build -t n8n-usecase-066 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-066 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-066

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-066:
    image: n8n-usecase-066
    container_name: n8n-usecase-066
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_066_data:/home/node/.n8n"]

volumes:
  n8n_usecase_066_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
