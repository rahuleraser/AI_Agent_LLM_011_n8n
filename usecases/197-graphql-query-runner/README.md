# 197 - GraphQL Query Runner

> **Category:** API Integration & Automation

Runs GraphQL queries and posts results. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Query)"]
    B["Validate Query"]
    C["Execute GraphQL"]
    D["IF: Query allowed?"]
    E["Reject Query"]
    F["Format Results"]
    G["Notify Consumer"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Query inbound |
| Code | Validation |
| IF | Allow check |
| HTTP Request | GraphQL call |
| Code | Result format |
| SQLite | Query log |

## Dockerfile

Dockerfile: [usecases/197-graphql-query-runner/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/197-graphql-query-runner/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `GRAPHQL_WEBHOOK_PATH=graphql`

## Build & Run

```bash
cd usecases/197-graphql-query-runner

# Build the image
docker build -t n8n-usecase-197 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-197 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-197

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-197:
    image: n8n-usecase-197
    container_name: n8n-usecase-197
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_197_data:/home/node/.n8n"]

volumes:
  n8n_usecase_197_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
