# 149 - HR Newsletter Sender

> **Category:** HR & Internal Ops

Sends company newsletters to employees on a schedule. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Monthly)"]
    B["Build Newsletter Content"]
    C["Send with Attachments"]
    D["IF: Attachments ready?"]
    E["Send Text Only"]
    F["Update Send Log"]
    G["Track Engagement"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Monthly send |
| Google Docs | Content build |
| IF | Attachment check |
| Email | Newsletter send |
| Spreadsheet | Send log |
| SQLite | Engagement log |

## Dockerfile

Dockerfile: [usecases/149-hr-newsletter-sender/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/149-hr-newsletter-sender/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `HR_NEWS_CRON=0 10 1 * *`

## Build & Run

```bash
cd usecases/149-hr-newsletter-sender

# Build the image
docker build -t n8n-usecase-149 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-149 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-149

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-149:
    image: n8n-usecase-149
    container_name: n8n-usecase-149
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_149_data:/home/node/.n8n"]

volumes:
  n8n_usecase_149_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
