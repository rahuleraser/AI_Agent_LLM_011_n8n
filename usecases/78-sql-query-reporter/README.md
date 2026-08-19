# 078 - SQL Query Reporter

> **Category:** Data & Database

Runs scheduled SQL queries and emails the results. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Daily)"]
    B["Run SQL Query"]
    C["Format Results"]
    D["IF: Empty results?"]
    E["Send Empty Notice"]
    F["Email Full Report"]
    G["Log Query Run"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Daily run |
| Postgres | Query execute |
| Code | Format table |
| IF | Empty check |
| Email | Report send |
| SQLite | Run log |

## Dockerfile

Dockerfile: [usecases/78-sql-query-reporter/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/78-sql-query-reporter/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `SQL_REPORT_CRON=0 7 * * *`
- `SQL_FILE=reports.sql`

## Build & Run

```bash
cd usecases/78-sql-query-reporter

# Build the image
docker build -t n8n-usecase-078 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-078 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-078

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-078:
    image: n8n-usecase-078
    container_name: n8n-usecase-078
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_078_data:/home/node/.n8n"]

volumes:
  n8n_usecase_078_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
