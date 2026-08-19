# 003 - Email Digest Builder

> **Category:** Email & Communication

Aggregates daily emails and compiles a single morning summary digest. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Daily 8am)"]
    B["Fetch Unread Emails"]
    C["Rank by Importance"]
    D["IF: Contains action item?"]
    E["Add to Action List"]
    F["Add to Read-Only List"]
    G["Send Digest Email"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Scheduled daily run |
| Gmail | Fetches emails |
| Code | Scores importance |
| IF | Splits action items |
| Email Send | Delivers digest |
| Spreadsheet | Stores digest log |

## Dockerfile

Dockerfile: [usecases/03-email-digest-builder/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/03-email-digest-builder/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `CRON_SCHEDULE=0 8 * * 1-5`
- `DIGEST_MAX_EMAILS=20`

## Build & Run

```bash
cd usecases/03-email-digest-builder

# Build the image
docker build -t n8n-usecase-003 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-003 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-003

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-003:
    image: n8n-usecase-003
    container_name: n8n-usecase-003
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_003_data:/home/node/.n8n"]

volumes:
  n8n_usecase_003_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
