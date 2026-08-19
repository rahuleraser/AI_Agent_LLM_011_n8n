# 175 - Plant Watering Reminder

> **Category:** IoT & Smart Home

Sends reminders when plants need water based on sensor data. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Daily)"]
    B["Read Moisture Sensors"]
    C["Send Watering Reminder"]
    D["IF: Soil dry?"]
    E["Log Moisture"]
    F["Update Plant Status"]
    G["Notify Owner"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Daily read |
| HTTP Request | Sensor API |
| IF | Dry check |
| Telegram | Reminder send |
| SQLite | Moisture log |
| Google Sheets | Plant status |

## Dockerfile

Dockerfile: [usecases/175-plant-watering-reminder/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/175-plant-watering-reminder/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `PLANT_CRON=0 9 * * *`
- `MOISTURE_WARN=30`

## Build & Run

```bash
cd usecases/175-plant-watering-reminder

# Build the image
docker build -t n8n-usecase-175 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-175 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-175

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-175:
    image: n8n-usecase-175
    container_name: n8n-usecase-175
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_175_data:/home/node/.n8n"]

volumes:
  n8n_usecase_175_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
