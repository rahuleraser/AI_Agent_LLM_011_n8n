# 010 - Calendar Invite Sync

> **Category:** Email & Communication

Reads calendar invites from email and creates matching calendar events. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Gmail Trigger (Calendar Invite)"]
    B["Parse Invite Details"]
    C["Create Calendar Event"]
    D["IF: Conflicts found?"]
    E["Notify Organizer"]
    F["Create Event + Reminder"]
    G["Sync to Sheet"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Gmail Trigger | Invite email |
| Code | Parses .ics |
| Google Calendar | Creates event |
| IF | Conflict check |
| Email | Notifies organizer |
| Google Sheets | Sync log |

## Dockerfile

Dockerfile: [usecases/10-calendar-invite-sync/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/10-calendar-invite-sync/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `WEBHOOK_PATH=cal-invite`
- `REMINDER_MINUTES=15`

## Build & Run

```bash
cd usecases/10-calendar-invite-sync

# Build the image
docker build -t n8n-usecase-010 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-010 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-010

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-010:
    image: n8n-usecase-010
    container_name: n8n-usecase-010
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_010_data:/home/node/.n8n"]

volumes:
  n8n_usecase_010_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
