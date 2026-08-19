# 059 - Meeting Reminder

> **Category:** CRM & Sales

Sends meeting reminders to attendees before the start time. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Hourly)"]
    B["Find Meetings in 1h"]
    C["Skip Meeting"]
    D["IF: Reminder sent?"]
    E["Send Reminder Email"]
    F["Notify Organizer"]
    G["Log Reminders"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Scan calendar |
| Google Calendar | Events |
| IF | Reminder check |
| Email | Reminder send |
| Slack | Organizer note |
| SQLite | Reminder log |

## Dockerfile

Dockerfile: [usecases/59-meeting-reminder/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/59-meeting-reminder/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `MEETING_CRON=0 * * * *`
- `REMIND_BEFORE_MIN=60`

## Build & Run

```bash
cd usecases/59-meeting-reminder

# Build the image
docker build -t n8n-usecase-059 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-059 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-059

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-059:
    image: n8n-usecase-059
    container_name: n8n-usecase-059
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_059_data:/home/node/.n8n"]

volumes:
  n8n_usecase_059_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
