# 151 - Equipment Request Tracker

> **Category:** HR & Internal Ops

Tracks hardware and equipment requests from intake to delivery. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Equipment Request)"]
    B["Log Request Details"]
    C["Create Dispatch Task"]
    D["IF: Stock available?"]
    E["Add to Waitlist"]
    F["Notify Requester"]
    G["Update Inventory"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Request in |
| Google Sheets | Request log |
| IF | Stock check |
| Slack | Dispatch task |
| Email | Requester notify |
| SQLite | Inventory update |

## Dockerfile

Dockerfile: [usecases/151-equipment-request-tracker/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/151-equipment-request-tracker/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `EQUIPMENT_WEBHOOK_PATH=equipment`

## Build & Run

```bash
cd usecases/151-equipment-request-tracker

# Build the image
docker build -t n8n-usecase-151 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-151 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-151

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-151:
    image: n8n-usecase-151
    container_name: n8n-usecase-151
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_151_data:/home/node/.n8n"]

volumes:
  n8n_usecase_151_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
