# 065 - Sales Lead Reassignment

> **Category:** CRM & Sales

Reassigns stale leads to a new owner automatically. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Weekly)"]
    B["Find Stale Leads"]
    C["Reassign to Round-robin"]
    D["IF: Stale > 14 days?"]
    E["Keep Lead"]
    F["Notify New Owner"]
    G["Log Reassignment"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Weekly scan |
| CRM API | Lead age |
| IF | Stale threshold |
| CRM | Owner change |
| Email | New owner alert |
| SQLite | Reassign log |

## Dockerfile

Dockerfile: [usecases/65-sales-lead-reassignment/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/65-sales-lead-reassignment/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `REASSIGN_CRON=0 6 * * 1`
- `STALE_DAYS=14`

## Build & Run

```bash
cd usecases/65-sales-lead-reassignment

# Build the image
docker build -t n8n-usecase-065 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-065 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-065

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-065:
    image: n8n-usecase-065
    container_name: n8n-usecase-065
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_065_data:/home/node/.n8n"]

volumes:
  n8n_usecase_065_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
