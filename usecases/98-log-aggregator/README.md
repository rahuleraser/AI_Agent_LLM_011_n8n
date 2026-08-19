# 098 - Log Aggregator

> **Category:** Developer & DevOps

Aggregates logs from multiple sources and indexes them. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Logs)"]
    B["Normalize Log Lines"]
    C["Flag for Search"]
    D["IF: Error detected?"]
    E["Index Logs"]
    F["Trigger Search Alert"]
    G["Store in Database"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Log ingest |
| Code | Normalization |
| IF | Error detect |
| MongoDB | Index logs |
| Slack | Error alert |
| Google Sheets | Log stats |

## Dockerfile

Dockerfile: [usecases/98-log-aggregator/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/98-log-aggregator/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | `n8n-nodes-mongodb` |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `LOG_WEBHOOK_PATH=log-ingest`

## Build & Run

```bash
cd usecases/98-log-aggregator

# Build the image
docker build -t n8n-usecase-098 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-098 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-098

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-098:
    image: n8n-usecase-098
    container_name: n8n-usecase-098
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_098_data:/home/node/.n8n"]

volumes:
  n8n_usecase_098_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
