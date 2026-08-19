# 056 - Lead Deduplication

> **Category:** CRM & Sales

Detects duplicate leads and merges them into a single record. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["CRM Trigger (New Lead)"]
    B["Lookup Existing Leads"]
    C["Merge Records"]
    D["IF: Match found?"]
    E["Create New Lead"]
    F["Log Dedupe"]
    G["Notify Owner"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| CRM Trigger | Lead create |
| SQLite | Lookup index |
| IF | Match detection |
| CRM | Merge action |
| CRM | Create record |
| SQLite | Dedupe log |

## Dockerfile

Dockerfile: [usecases/56-lead-deduplication/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/56-lead-deduplication/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | `n8n-nodes-sqlite` |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `DEDUPE_WEBHOOK_PATH=dedupe`

## Build & Run

```bash
cd usecases/56-lead-deduplication

# Build the image
docker build -t n8n-usecase-056 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-056 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-056

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-056:
    image: n8n-usecase-056
    container_name: n8n-usecase-056
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_056_data:/home/node/.n8n"]

volumes:
  n8n_usecase_056_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
