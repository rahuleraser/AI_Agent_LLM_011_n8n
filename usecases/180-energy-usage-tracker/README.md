# 180 - Energy Usage Tracker

> **Category:** IoT & Smart Home

Tracks home energy usage and sends weekly reports. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Hourly)"]
    B["Read Energy Meter"]
    C["Send Spike Alert"]
    D["IF: Usage spike?"]
    E["Store Reading"]
    F["Compute Weekly Use"]
    G["Email Weekly Report"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Meter read |
| HTTP Request | Energy API |
| IF | Spike check |
| SQLite | Usage store |
| Code | Weekly compute |
| Email | Report send |

## Dockerfile

Dockerfile: [usecases/180-energy-usage-tracker/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/180-energy-usage-tracker/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `ENERGY_CRON=0 * * * *`
- `SPIKE_WATT=3000`

## Build & Run

```bash
cd usecases/180-energy-usage-tracker

# Build the image
docker build -t n8n-usecase-180 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-180 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-180

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-180:
    image: n8n-usecase-180
    container_name: n8n-usecase-180
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_180_data:/home/node/.n8n"]

volumes:
  n8n_usecase_180_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
