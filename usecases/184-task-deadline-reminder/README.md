# 184 - Task Deadline Reminder

> **Category:** Monitoring & Alerts

Reminds teams about upcoming task deadlines. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Daily)"]
    B["Fetch Due Tasks"]
    C["Send Reminder"]
    D["IF: Due within 24h?"]
    E["Log Deadlines"]
    F["Escalate if Late"]
    G["Notify Task Owner"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Deadline scan |
| SQLite | Task store |
| IF | Window check |
| Email | Reminder send |
| Slack | Escalation |
| Google Sheets | Deadline log |

## Dockerfile

Dockerfile: [usecases/184-task-deadline-reminder/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/184-task-deadline-reminder/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `DEADLINE_CRON=0 8 * * *`
- `REMIND_WINDOW_H=24`

## Build & Run

```bash
cd usecases/184-task-deadline-reminder

# Build the image
docker build -t n8n-usecase-184 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-184 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-184

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-184:
    image: n8n-usecase-184
    container_name: n8n-usecase-184
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_184_data:/home/node/.n8n"]

volumes:
  n8n_usecase_184_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
