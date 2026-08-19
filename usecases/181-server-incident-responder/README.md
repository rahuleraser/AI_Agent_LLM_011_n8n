# 181 - Server Incident Responder

> **Category:** Monitoring & Alerts

Responds to server incidents with automated runbooks. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Alert Webhook"]
    B["Classify Incident"]
    C["Run Fix Runbook"]
    D["IF: Known issue?"]
    E["Create Incident Ticket"]
    F["Notify On-call"]
    G["Log Resolution"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Alert inbound |
| AI | Incident classify |
| IF | Known issue |
| Code | Runbook run |
| Jira | Ticket create |
| Slack | On-call alert |

## Dockerfile

Dockerfile: [usecases/181-server-incident-responder/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/181-server-incident-responder/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `INCIDENT_WEBHOOK_PATH=incident`

## Build & Run

```bash
cd usecases/181-server-incident-responder

# Build the image
docker build -t n8n-usecase-181 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-181 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-181

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-181:
    image: n8n-usecase-181
    container_name: n8n-usecase-181
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_181_data:/home/node/.n8n"]

volumes:
  n8n_usecase_181_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
