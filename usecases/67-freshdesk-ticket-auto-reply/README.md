# 067 - Freshdesk Ticket Auto-Reply

> **Category:** Support & Customer Service

Sends instant acknowledgements to Freshdesk tickets. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Freshdesk Trigger (Ticket)"]
    B["Fetch Ticket Content"]
    C["Send Quick Answer"]
    D["IF: Needs immediate reply?"]
    E["Send Ack Message"]
    F["Add Internal Note"]
    G["Log Auto-replies"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Freshdesk Trigger | New ticket |
| Code | Content analysis |
| IF | Auto-reply check |
| Freshdesk | Reply post |
| Freshdesk | Internal note |
| SQLite | Reply log |

## Dockerfile

Dockerfile: [usecases/67-freshdesk-ticket-auto-reply/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/67-freshdesk-ticket-auto-reply/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `FRESHDESK_WEBHOOK_PATH=fd-ticket`

## Build & Run

```bash
cd usecases/67-freshdesk-ticket-auto-reply

# Build the image
docker build -t n8n-usecase-067 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-067 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-067

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-067:
    image: n8n-usecase-067
    container_name: n8n-usecase-067
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_067_data:/home/node/.n8n"]

volumes:
  n8n_usecase_067_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
