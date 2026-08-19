# 127 - Payment Reminder Bot

> **Category:** Finance & Accounting

Reminds customers about overdue payments. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Daily)"]
    B["Find Overdue Invoices"]
    C["Send Strong Reminder"]
    D["IF: Overdue days > 7?"]
    E["Send Soft Reminder"]
    F["Update Reminder Log"]
    G["Notify Finance"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Daily scan |
| SQLite | Invoice store |
| IF | Overdue level |
| Email | Reminder send |
| Stripe | Payment check |
| Google Sheets | Reminder log |

## Dockerfile

Dockerfile: [usecases/127-payment-reminder-bot/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/127-payment-reminder-bot/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | `n8n-nodes-stripe`, `n8n-nodes-sqlite` |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `REMIND_CRON=0 9 * * *`
- `REMINDER_LEVELS=soft,strong`

## Build & Run

```bash
cd usecases/127-payment-reminder-bot

# Build the image
docker build -t n8n-usecase-127 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-127 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-127

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-127:
    image: n8n-usecase-127
    container_name: n8n-usecase-127
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_127_data:/home/node/.n8n"]

volumes:
  n8n_usecase_127_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
