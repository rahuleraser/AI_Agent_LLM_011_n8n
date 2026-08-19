# 054 - Zoho CRM Enrichment

> **Category:** CRM & Sales

Enriches Zoho CRM records with company information automatically. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Zoho Trigger (Record)"]
    B["Fetch Company Domain"]
    C["Enrich Company Info"]
    D["IF: Data incomplete?"]
    E["Update Record"]
    F["Log Enrichment"]
    G["Notify Owner"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Zoho Trigger | Record event |
| HTTP Request | Company API |
| IF | Completeness check |
| Zoho | Update record |
| SQLite | Enrichment log |
| Email | Owner notify |

## Dockerfile

Dockerfile: [usecases/54-zoho-crm-enrichment/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/54-zoho-crm-enrichment/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `ZOHO_WEBHOOK_PATH=zoho-enrich`

## Build & Run

```bash
cd usecases/54-zoho-crm-enrichment

# Build the image
docker build -t n8n-usecase-054 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-054 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-054

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-054:
    image: n8n-usecase-054
    container_name: n8n-usecase-054
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_054_data:/home/node/.n8n"]

volumes:
  n8n_usecase_054_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
