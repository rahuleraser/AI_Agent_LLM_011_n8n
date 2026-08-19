# 115 - AI Lead Enrichment

> **Category:** AI & LLM

Enriches leads with AI-generated company summaries. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["CRM Trigger (Lead)"]
    B["Fetch Company Data"]
    C["Skip Enrichment"]
    D["IF: Existing summary?"]
    E["Generate AI Summary"]
    F["Update Lead Field"]
    G["Notify Sales"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| CRM Trigger | New lead |
| HTTP Request | Company data |
| IF | Dup check |
| AI LLM | Summary generate |
| CRM | Field update |
| Slack | Sales notify |

## Dockerfile

Dockerfile: [usecases/115-ai-lead-enrichment/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/115-ai-lead-enrichment/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `AI_ENRICH_WEBHOOK_PATH=enrich`

## Build & Run

```bash
cd usecases/115-ai-lead-enrichment

# Build the image
docker build -t n8n-usecase-115 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-115 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-115

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-115:
    image: n8n-usecase-115
    container_name: n8n-usecase-115
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_115_data:/home/node/.n8n"]

volumes:
  n8n_usecase_115_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
