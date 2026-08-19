# 072 - CSAT Survey Sender

> **Category:** Support & Customer Service

Sends customer satisfaction surveys after ticket resolution. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Ticket Trigger (Resolved)"]
    B["Build CSAT Survey"]
    C["Send Survey Email"]
    D["IF: Eligible contact?"]
    E["Skip Contact"]
    F["Wait for Response"]
    G["Store CSAT Score"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Ticket Trigger | Resolution |
| Code | Eligibility check |
| IF | Survey branch |
| Email | Survey send |
| Wait | Response window |
| Google Sheets | CSAT store |

## Dockerfile

Dockerfile: [usecases/72-csat-survey-sender/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/72-csat-survey-sender/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `CSAT_WEBHOOK_PATH=csat`
- `SURVEY_WAIT_DAYS=1`

## Build & Run

```bash
cd usecases/72-csat-survey-sender

# Build the image
docker build -t n8n-usecase-072 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-072 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-072

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-072:
    image: n8n-usecase-072
    container_name: n8n-usecase-072
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_072_data:/home/node/.n8n"]

volumes:
  n8n_usecase_072_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
