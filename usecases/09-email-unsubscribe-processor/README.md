# 009 - Email Unsubscribe Processor

> **Category:** Email & Communication

Processes unsubscribe requests and confirms removal across all lists. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Email Trigger (Unsubscribe)"]
    B["Extract Email Address"]
    C["Remove from All Lists"]
    D["IF: Confirmation needed?"]
    E["Send Confirmation Email"]
    F["Update Records"]
    G["Log Unsubscribe"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Email Trigger | Detects request |
| Code | Extracts address |
| Email Send | Confirms removal |
| Spreadsheet | Updates lists |
| IF | Confirmation flow |
| SQLite | Unsubscribe log |

## Dockerfile

Dockerfile: [usecases/09-email-unsubscribe-processor/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/09-email-unsubscribe-processor/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `WEBHOOK_PATH=unsubscribe`
- `LISTS=newsletter,alerts`

## Build & Run

```bash
cd usecases/09-email-unsubscribe-processor

# Build the image
docker build -t n8n-usecase-009 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-009 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-009

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-009:
    image: n8n-usecase-009
    container_name: n8n-usecase-009
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_009_data:/home/node/.n8n"]

volumes:
  n8n_usecase_009_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
