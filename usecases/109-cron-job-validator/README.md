# 109 - Cron Job Validator

> **Category:** Developer & DevOps

Validates cron schedules and reports upcoming runs. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Daily)"]
    B["Parse Cron Expressions"]
    C["Log Schedule"]
    D["IF: Expression valid?"]
    E["Flag Invalid"]
    F["Send Schedule Report"]
    G["Notify Admins"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Daily check |
| Code | Expression parse |
| IF | Validation branch |
| Google Sheets | Schedule log |
| Email | Report send |
| Slack | Admin notify |

## Dockerfile

Dockerfile: [usecases/109-cron-job-validator/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/109-cron-job-validator/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `CRON_VALIDATOR=0 6 * * *`

## Build & Run

```bash
cd usecases/109-cron-job-validator

# Build the image
docker build -t n8n-usecase-109 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-109 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-109

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-109:
    image: n8n-usecase-109
    container_name: n8n-usecase-109
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_109_data:/home/node/.n8n"]

volumes:
  n8n_usecase_109_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
