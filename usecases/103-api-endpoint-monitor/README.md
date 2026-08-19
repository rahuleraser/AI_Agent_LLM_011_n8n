# 103 - API Endpoint Monitor

> **Category:** Developer & DevOps

Monitors API endpoints for latency and availability. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (1 min)"]
    B["Hit API Endpoint"]
    C["Measure Latency"]
    D["IF: Slow or down?"]
    E["Alert API Team"]
    F["Store Metrics"]
    G["Update Dashboard"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Endpoint poll |
| HTTP Request | Request send |
| Code | Latency measure |
| IF | Threshold check |
| Slack | API alert |
| Google Sheets | Metrics |

## Dockerfile

Dockerfile: [usecases/103-api-endpoint-monitor/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/103-api-endpoint-monitor/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `API_MONITOR_CRON=* * * * *`
- `ENDPOINTS=health.json`
- `LATENCY_WARN_MS=1000`

## Build & Run

```bash
cd usecases/103-api-endpoint-monitor

# Build the image
docker build -t n8n-usecase-103 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-103 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-103

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-103:
    image: n8n-usecase-103
    container_name: n8n-usecase-103
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_103_data:/home/node/.n8n"]

volumes:
  n8n_usecase_103_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
