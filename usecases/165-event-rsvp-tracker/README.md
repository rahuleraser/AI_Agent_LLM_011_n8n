# 165 - Event RSVP Tracker

> **Category:** Content & Publishing

Tracks RSVPs and sends event updates. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (RSVP)"]
    B["Update RSVP Count"]
    C["Notify Organizer"]
    D["IF: Capacity reached?"]
    E["Send Confirmation"]
    F["Add to Guest List"]
    G["Send Day-of Reminder"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | RSVP event |
| Google Sheets | Guest list |
| IF | Capacity check |
| Email | Confirmation |
| Slack | Organizer alert |
| Email | Reminder send |

## Dockerfile

Dockerfile: [usecases/165-event-rsvp-tracker/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/165-event-rsvp-tracker/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `RSVP_WEBHOOK_PATH=rsvp`
- `MAX_CAPACITY=100`

## Build & Run

```bash
cd usecases/165-event-rsvp-tracker

# Build the image
docker build -t n8n-usecase-165 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-165 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-165

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-165:
    image: n8n-usecase-165
    container_name: n8n-usecase-165
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_165_data:/home/node/.n8n"]

volumes:
  n8n_usecase_165_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
