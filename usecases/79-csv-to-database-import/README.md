# 079 - CSV to Database Import

> **Category:** Data & Database

Imports CSV files into a database with validation. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["File Trigger (CSV)"]
    B["Parse CSV Rows"]
    C["Insert into Database"]
    D["IF: Rows valid?"]
    E["Log Invalid Rows"]
    F["Send Import Summary"]
    G["Archive File"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| File Trigger | New CSV |
| Code | Row parsing |
| IF | Validation check |
| Postgres | Bulk insert |
| Google Sheets | Error log |
| Email | Import summary |

## Dockerfile

Dockerfile: [usecases/79-csv-to-database-import/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/79-csv-to-database-import/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `CSV_IMPORT_WEBHOOK_PATH=csv-import`

## Build & Run

```bash
cd usecases/79-csv-to-database-import

# Build the image
docker build -t n8n-usecase-079 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-079 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-079

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-079:
    image: n8n-usecase-079
    container_name: n8n-usecase-079
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_079_data:/home/node/.n8n"]

volumes:
  n8n_usecase_079_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
