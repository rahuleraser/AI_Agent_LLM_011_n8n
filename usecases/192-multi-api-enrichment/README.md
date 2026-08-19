# 192 - Multi-API Enrichment

> **Category:** API Integration & Automation

Enriches records using multiple external APIs. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["CRM Trigger (Record)"]
    B["Fetch Base Record"]
    C["Call Enrichment APIs"]
    D["IF: Data missing?"]
    E["Keep Record"]
    F["Merge Results"]
    G["Update Record"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| CRM Trigger | Record event |
| HTTP Request | Enrich APIs |
| IF | Missing check |
| Code | Result merge |
| CRM | Record update |
| SQLite | Enrichment log |

## Dockerfile

Dockerfile: [usecases/192-multi-api-enrichment/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/192-multi-api-enrichment/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `ENRICHMENT_WEBHOOK_PATH=enrichment`

## Build & Run

```bash
cd usecases/192-multi-api-enrichment

# Build the image
docker build -t n8n-usecase-192 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-192 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-192

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-192:
    image: n8n-usecase-192
    container_name: n8n-usecase-192
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_192_data:/home/node/.n8n"]

volumes:
  n8n_usecase_192_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
