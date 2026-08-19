# 083 - Data Validation Pipeline

> **Category:** Data & Database

Validates incoming data against business rules before storing. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Data)"]
    B["Apply Validation Rules"]
    C["Store in Database"]
    D["IF: Data valid?"]
    E["Reject with Reason"]
    F["Notify Data Owner"]
    G["Log Validation"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Data inbound |
| Code | Rule checks |
| IF | Valid branch |
| Postgres | Store record |
| Email | Rejection notice |
| SQLite | Validation log |

## Dockerfile

Dockerfile: [usecases/83-data-validation-pipeline/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/83-data-validation-pipeline/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `VALIDATION_WEBHOOK_PATH=validate`

## Build & Run

```bash
cd usecases/83-data-validation-pipeline

# Build the image
docker build -t n8n-usecase-083 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-083 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-083

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-083:
    image: n8n-usecase-083
    container_name: n8n-usecase-083
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_083_data:/home/node/.n8n"]

volumes:
  n8n_usecase_083_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
