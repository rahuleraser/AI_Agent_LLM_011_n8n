# 097 - Kubernetes Alert Relay

> **Category:** Developer & DevOps

Relays Kubernetes cluster alerts to the operations team. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (K8s Alert)"]
    B["Parse Alert Payload"]
    C["Page On-call"]
    D["IF: Critical severity?"]
    E["Log Warning"]
    F["Post to Ops Channel"]
    G["Create Incident Ticket"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | K8s alert |
| Code | Severity parse |
| IF | Critical branch |
| PagerDuty | Page on-call |
| Slack | Ops post |
| Jira | Incident ticket |

## Dockerfile

Dockerfile: [usecases/97-kubernetes-alert-relay/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/97-kubernetes-alert-relay/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `K8S_WEBHOOK_PATH=k8s-alert`

## Build & Run

```bash
cd usecases/97-kubernetes-alert-relay

# Build the image
docker build -t n8n-usecase-097 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-097 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-097

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-097:
    image: n8n-usecase-097
    container_name: n8n-usecase-097
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_097_data:/home/node/.n8n"]

volumes:
  n8n_usecase_097_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
