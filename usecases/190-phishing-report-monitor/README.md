# 190 - Phishing Report Monitor

> **Category:** Monitoring & Alerts

Monitors user-reported phishing emails. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Email Trigger (Report)"]
    B["Fetch Reported Email"]
    C["Block Sender"]
    D["IF: Confirmed phishing?"]
    E["Add to Watchlist"]
    F["Log Report"]
    G["Notify Security Team"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Email Trigger | User report |
| Code | Analyze email |
| IF | Confirmed check |
| Email | Block action |
| SQLite | Watchlist |
| Slack | Security notify |

## Dockerfile

Dockerfile: [usecases/190-phishing-report-monitor/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/190-phishing-report-monitor/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `PHISHING_WEBHOOK_PATH=phishing`

## Build & Run

```bash
cd usecases/190-phishing-report-monitor

# Build the image
docker build -t n8n-usecase-190 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-190 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-190

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-190:
    image: n8n-usecase-190
    container_name: n8n-usecase-190
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_190_data:/home/node/.n8n"]

volumes:
  n8n_usecase_190_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
