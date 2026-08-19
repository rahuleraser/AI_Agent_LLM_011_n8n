# 051 - HubSpot Lead Capture

> **Category:** CRM & Sales

Captures new HubSpot leads from web forms and enriches them. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["HubSpot Trigger (Contact)"]
    B["Fetch Lead Data"]
    C["Enrich via API"]
    D["IF: Enrichment needed?"]
    E["Save Lead"]
    F["Assign to Owner"]
    G["Notify Sales Rep"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| HubSpot Trigger | New contact |
| HTTP Request | Enrichment API |
| IF | Enrichment check |
| HubSpot | Create contact |
| HubSpot | Owner assignment |
| Slack | Sales alert |

## Dockerfile

Dockerfile: [usecases/51-hubspot-lead-capture/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/51-hubspot-lead-capture/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `HUBSPOT_WEBHOOK_PATH=hubspot-lead`

## Build & Run

```bash
cd usecases/51-hubspot-lead-capture

# Build the image
docker build -t n8n-usecase-051 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-051 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-051

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-051:
    image: n8n-usecase-051
    container_name: n8n-usecase-051
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_051_data:/home/node/.n8n"]

volumes:
  n8n_usecase_051_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
