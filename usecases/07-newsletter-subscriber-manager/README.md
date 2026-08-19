# 007 - Newsletter Subscriber Manager

> **Category:** Email & Communication

Manages newsletter subscribers and sends a weekly issue automatically. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Subscribe Form)"]
    B["Add to Subscriber List"]
    C["Send Welcome Email"]
    D["IF: Unsubscribed?"]
    E["Remove from List"]
    F["Send Weekly Issue"]
    G["Log Stats"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Subscriber signup |
| Email Send | Welcome mail |
| Cron Trigger | Weekly send |
| Email Send | Issue delivery |
| IF | Handles unsubscribes |
| Spreadsheet | Stats log |

## Dockerfile

Dockerfile: [usecases/07-newsletter-subscriber-manager/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/07-newsletter-subscriber-manager/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `WEBHOOK_PATH=subscribe`
- `WEEKLY_CRON=0 9 * * 3`

## Build & Run

```bash
cd usecases/07-newsletter-subscriber-manager

# Build the image
docker build -t n8n-usecase-007 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-007 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-007

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-007:
    image: n8n-usecase-007
    container_name: n8n-usecase-007
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_007_data:/home/node/.n8n"]

volumes:
  n8n_usecase_007_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
