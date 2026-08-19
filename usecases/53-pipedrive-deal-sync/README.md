# 053 - Pipedrive Deal Sync

> **Category:** CRM & Sales

Syncs Pipedrive deals to a Google Sheets pipeline tracker. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Pipedrive Trigger (Deal)"]
    B["Fetch Deal Fields"]
    C["Update Sheet Row"]
    D["IF: Deal stage changed?"]
    E["Log Change"]
    F["Notify Manager"]
    G["Sync to Dashboard"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Pipedrive Trigger | Deal event |
| HTTP Request | Deal data |
| IF | Stage change |
| Google Sheets | Tracker update |
| Slack | Manager alert |
| Code | Dashboard sync |

## Dockerfile

Dockerfile: [usecases/53-pipedrive-deal-sync/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/53-pipedrive-deal-sync/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `PIPEDRIVE_WEBHOOK_PATH=deal-sync`

## Build & Run

```bash
cd usecases/53-pipedrive-deal-sync

# Build the image
docker build -t n8n-usecase-053 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-053 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-053

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-053:
    image: n8n-usecase-053
    container_name: n8n-usecase-053
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_053_data:/home/node/.n8n"]

volumes:
  n8n_usecase_053_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
