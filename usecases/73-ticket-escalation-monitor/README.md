# 073 - Ticket Escalation Monitor

> **Category:** Support & Customer Service

Monitors SLA and escalates tickets that are about to breach. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (30 min)"]
    B["Check Ticket Ages"]
    C["Escalate to Manager"]
    D["IF: Breach risk?"]
    E["Update SLA Status"]
    F["Notify Support Lead"]
    G["Log Escalations"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Age scan |
| Zendesk | Ticket fetch |
| IF | Breach risk |
| Email | Manager escalate |
| Zendesk | Status update |
| SQLite | Escalation log |

## Dockerfile

Dockerfile: [usecases/73-ticket-escalation-monitor/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/73-ticket-escalation-monitor/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `SLA_CRON=*/30 * * * *`
- `SLA_HOURS=4`

## Build & Run

```bash
cd usecases/73-ticket-escalation-monitor

# Build the image
docker build -t n8n-usecase-073 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-073 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-073

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-073:
    image: n8n-usecase-073
    container_name: n8n-usecase-073
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_073_data:/home/node/.n8n"]

volumes:
  n8n_usecase_073_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
