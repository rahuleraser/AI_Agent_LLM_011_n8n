# 058 - Appointment Scheduler (Calendly)

> **Category:** CRM & Sales

Schedules appointments via Calendly and syncs to CRM. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Calendly Trigger (Booking)"]
    B["Fetch Booking Details"]
    C["Create CRM Task"]
    D["IF: Slot confirmed?"]
    E["Notify Booker"]
    F["Add to Calendar"]
    G["Send Confirmation"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Calendly Trigger | New booking |
| HTTP Request | Booking data |
| IF | Confirmation check |
| Google Calendar | Add event |
| CRM | Create task |
| Email | Confirmation |

## Dockerfile

Dockerfile: [usecases/58-appointment-scheduler-calendly/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/58-appointment-scheduler-calendly/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `CALENDLY_WEBHOOK_PATH=booking`

## Build & Run

```bash
cd usecases/58-appointment-scheduler-calendly

# Build the image
docker build -t n8n-usecase-058 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-058 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-058

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-058:
    image: n8n-usecase-058
    container_name: n8n-usecase-058
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_058_data:/home/node/.n8n"]

volumes:
  n8n_usecase_058_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
