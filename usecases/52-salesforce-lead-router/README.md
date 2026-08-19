# 052 - Salesforce Lead Router

> **Category:** CRM & Sales

Routes Salesforce leads to the right sales owner by territory. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Salesforce Trigger (Lead)"]
    B["Read Lead Territory"]
    C["Assign APAC Rep"]
    D["IF: APAC region?"]
    E["Assign EMEA Rep"]
    F["Update Lead Owner"]
    G["Notify Assigned Rep"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Salesforce Trigger | New lead |
| Code | Territory parse |
| IF | Region branch |
| Salesforce | Owner update |
| Salesforce | Lead update |
| Email | Rep notification |

## Dockerfile

Dockerfile: [usecases/52-salesforce-lead-router/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/52-salesforce-lead-router/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `SF_WEBHOOK_PATH=sf-lead-route`

## Build & Run

```bash
cd usecases/52-salesforce-lead-router

# Build the image
docker build -t n8n-usecase-052 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-052 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-052

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-052:
    image: n8n-usecase-052
    container_name: n8n-usecase-052
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_052_data:/home/node/.n8n"]

volumes:
  n8n_usecase_052_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
