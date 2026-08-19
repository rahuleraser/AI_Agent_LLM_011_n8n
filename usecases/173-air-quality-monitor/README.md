# 173 - Air Quality Monitor

> **Category:** IoT & Smart Home

Monitors air quality and alerts on pollution spikes. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Hourly)"]
    B["Fetch Air Quality"]
    C["Send Health Alert"]
    D["IF: AQI over 100?"]
    E["Log AQI"]
    F["Update Dashboard"]
    G["Notify Subscribers"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | AQI poll |
| HTTP Request | AQI API |
| IF | Threshold check |
| Telegram | Health alert |
| SQLite | AQI log |
| Google Sheets | Dashboard |

## Dockerfile

Dockerfile: [usecases/173-air-quality-monitor/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/173-air-quality-monitor/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `AQI_CRON=0 * * * *`
- `AQI_WARN=100`

## Build & Run

```bash
cd usecases/173-air-quality-monitor

# Build the image
docker build -t n8n-usecase-173 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-173 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-173

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-173:
    image: n8n-usecase-173
    container_name: n8n-usecase-173
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_173_data:/home/node/.n8n"]

volumes:
  n8n_usecase_173_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
