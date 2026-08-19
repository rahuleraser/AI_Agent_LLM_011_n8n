# 081 - Data Migration Assistant

> **Category:** Data & Database

Assists with migrating data between database systems. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Migration)"]
    B["Extract Source Data"]
    C["Transform Schema"]
    D["IF: Mapping complete?"]
    E["Load into Target"]
    F["Flag Missing Mappings"]
    G["Log Migration"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Migration start |
| SQLite | Source extract |
| Code | Schema transform |
| IF | Mapping check |
| Postgres | Target load |
| Slack | DBA notify |

## Dockerfile

Dockerfile: [usecases/81-data-migration-assistant/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/81-data-migration-assistant/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `MIGRATION_WEBHOOK_PATH=migrate`

## Build & Run

```bash
cd usecases/81-data-migration-assistant

# Build the image
docker build -t n8n-usecase-081 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-081 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-081

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-081:
    image: n8n-usecase-081
    container_name: n8n-usecase-081
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_081_data:/home/node/.n8n"]

volumes:
  n8n_usecase_081_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
