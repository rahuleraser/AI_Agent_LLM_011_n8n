# 174 - Fitness Streak Reminder

> **Category:** IoT & Smart Home

Tracks fitness streaks and sends motivation reminders. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Daily)"]
    B["Check Activity Log"]
    C["Send Reboot Message"]
    D["IF: Streak broken?"]
    E["Send Streak Update"]
    F["Update Tracker"]
    G["Notify User"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Daily check |
| HTTP Request | Activity API |
| IF | Streak check |
| Telegram | Motivation |
| Google Sheets | Tracker |
| Email | Daily update |

## Dockerfile

Dockerfile: [usecases/174-fitness-streak-reminder/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/174-fitness-streak-reminder/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `FITNESS_CRON=0 8 * * *`

## Build & Run

```bash
cd usecases/174-fitness-streak-reminder

# Build the image
docker build -t n8n-usecase-174 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-174 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-174

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-174:
    image: n8n-usecase-174
    container_name: n8n-usecase-174
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_174_data:/home/node/.n8n"]

volumes:
  n8n_usecase_174_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
