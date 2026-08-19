# 154 - Team Event Planner

> **Category:** HR & Internal Ops

Coordinates team events, polls and logistics. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Event Idea)"]
    B["Create Event Draft"]
    C["Send Invites"]
    D["IF: Date confirmed?"]
    E["Poll for Availability"]
    F["Book Venue / Lunch"]
    G["Update Calendar"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Event idea |
| Google Calendar | Date check |
| IF | Confirmation branch |
| Email | Invite send |
| Poll API | Availability |
| Google Sheets | Event plan |

## Dockerfile

Dockerfile: [usecases/154-team-event-planner/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/154-team-event-planner/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `EVENT_WEBHOOK_PATH=team-event`

## Build & Run

```bash
cd usecases/154-team-event-planner

# Build the image
docker build -t n8n-usecase-154 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-154 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-154

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-154:
    image: n8n-usecase-154
    container_name: n8n-usecase-154
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_154_data:/home/node/.n8n"]

volumes:
  n8n_usecase_154_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
