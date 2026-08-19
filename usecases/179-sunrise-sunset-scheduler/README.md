# 179 - Sunrise / Sunset Scheduler

> **Category:** IoT & Smart Home

Triggers actions based on sunrise and sunset times. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Daily)"]
    B["Fetch Sun Times"]
    C["Run Day Actions"]
    D["IF: After sunrise?"]
    E["Run Night Actions"]
    F["Log Runs"]
    G["Notify Owner"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Sun check |
| HTTP Request | Sun API |
| IF | Time branch |
| HTTP Request | Device action |
| SQLite | Run log |
| Telegram | Owner notify |

## Dockerfile

Dockerfile: [usecases/179-sunrise-sunset-scheduler/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/179-sunrise-sunset-scheduler/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `SUN_CRON=0 5 * * *`

## Build & Run

```bash
cd usecases/179-sunrise-sunset-scheduler

# Build the image
docker build -t n8n-usecase-179 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-179 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-179

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-179:
    image: n8n-usecase-179
    container_name: n8n-usecase-179
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_179_data:/home/node/.n8n"]

volumes:
  n8n_usecase_179_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
