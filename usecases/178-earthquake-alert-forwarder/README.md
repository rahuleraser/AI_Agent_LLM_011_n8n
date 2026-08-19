# 178 - Earthquake Alert Forwarder

> **Category:** IoT & Smart Home

Forwards earthquake alerts to affected regions. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Seismic Event)"]
    B["Fetch Event Details"]
    C["Send Critical Alert"]
    D["IF: Magnitude over 5?"]
    E["Log Event"]
    F["Update Map"]
    G["Notify Authorities"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Seismic event |
| HTTP Request | Event data |
| IF | Magnitude check |
| Telegram | Critical alert |
| Google Sheets | Event map |
| Email | Authorities notify |

## Dockerfile

Dockerfile: [usecases/178-earthquake-alert-forwarder/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/178-earthquake-alert-forwarder/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `EARTHQUAKE_WEBHOOK_PATH=seismic`

## Build & Run

```bash
cd usecases/178-earthquake-alert-forwarder

# Build the image
docker build -t n8n-usecase-178 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-178 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-178

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-178:
    image: n8n-usecase-178
    container_name: n8n-usecase-178
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_178_data:/home/node/.n8n"]

volumes:
  n8n_usecase_178_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
