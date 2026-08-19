# 176 - IoT Sensor Data Logger

> **Category:** IoT & Smart Home

Logs sensor data from IoT devices into a database. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Sensor)"]
    B["Normalize Reading"]
    C["Store in Database"]
    D["IF: Reading valid?"]
    E["Flag Anomaly"]
    F["Update Dashboard"]
    G["Alert on Extreme"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Sensor reading |
| Code | Normalize |
| IF | Valid check |
| MongoDB | Store reading |
| Google Sheets | Dashboard |
| Slack | Extreme alert |

## Dockerfile

Dockerfile: [usecases/176-iot-sensor-data-logger/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/176-iot-sensor-data-logger/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | `n8n-nodes-mongodb` |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `SENSOR_WEBHOOK_PATH=sensor`

## Build & Run

```bash
cd usecases/176-iot-sensor-data-logger

# Build the image
docker build -t n8n-usecase-176 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-176 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-176

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-176:
    image: n8n-usecase-176
    container_name: n8n-usecase-176
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_176_data:/home/node/.n8n"]

volumes:
  n8n_usecase_176_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
