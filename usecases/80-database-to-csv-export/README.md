# 080 - Database to CSV Export

> **Category:** Data & Database

Exports database tables to CSV and stores them on schedule. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Weekly)"]
    B["Query Export Data"]
    C["Build CSV File"]
    D["IF: Data present?"]
    E["Save to Drive"]
    F["Log Empty Export"]
    G["Email Download Link"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Weekly export |
| Postgres | Query data |
| Code | CSV build |
| IF | Data check |
| Google Drive | Save file |
| Email | Link send |

## Dockerfile

Dockerfile: [usecases/80-database-to-csv-export/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/80-database-to-csv-export/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `EXPORT_CRON=0 3 * * 1`

## Build & Run

```bash
cd usecases/80-database-to-csv-export

# Build the image
docker build -t n8n-usecase-080 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-080 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-080

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-080:
    image: n8n-usecase-080
    container_name: n8n-usecase-080
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_080_data:/home/node/.n8n"]

volumes:
  n8n_usecase_080_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
