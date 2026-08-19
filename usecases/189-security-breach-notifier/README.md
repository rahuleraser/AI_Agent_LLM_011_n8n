# 189 - Security Breach Notifier

> **Category:** Monitoring & Alerts

Notifies on security events from monitoring tools. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Security Webhook"]
    B["Classify Event"]
    C["Page Security Team"]
    D["IF: Critical severity?"]
    E["Log Event"]
    F["Create Investigation Ticket"]
    G["Notify Executives"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Security event |
| Code | Severity classify |
| IF | Critical check |
| PagerDuty | Page team |
| Jira | Investigation ticket |
| Email | Exec notify |

## Dockerfile

Dockerfile: [usecases/189-security-breach-notifier/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/189-security-breach-notifier/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `SECURITY_WEBHOOK_PATH=security`

## Build & Run

```bash
cd usecases/189-security-breach-notifier

# Build the image
docker build -t n8n-usecase-189 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-189 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-189

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-189:
    image: n8n-usecase-189
    container_name: n8n-usecase-189
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_189_data:/home/node/.n8n"]

volumes:
  n8n_usecase_189_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
