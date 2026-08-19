# 163 - E-book Lead Magnet Sender

> **Category:** Content & Publishing

Sends e-books to leads who opt in via a form. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Opt-in)"]
    B["Add to List"]
    C["Send E-book Link"]
    D["IF: Verified email?"]
    E["Flag Invalid"]
    F["Log Downloads"]
    G["Notify Marketing"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Opt-in form |
| Code | Email verify |
| IF | Verification branch |
| Email | E-book send |
| Google Sheets | Download log |
| Slack | Marketing notify |

## Dockerfile

Dockerfile: [usecases/163-e-book-lead-magnet-sender/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/163-e-book-lead-magnet-sender/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `EBOOK_WEBHOOK_PATH=ebook`

## Build & Run

```bash
cd usecases/163-e-book-lead-magnet-sender

# Build the image
docker build -t n8n-usecase-163 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-163 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-163

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-163:
    image: n8n-usecase-163
    container_name: n8n-usecase-163
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_163_data:/home/node/.n8n"]

volumes:
  n8n_usecase_163_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
