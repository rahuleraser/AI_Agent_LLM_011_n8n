# 196 - Public REST API Wrapper

> **Category:** API Integration & Automation

Wraps a public REST API behind a normalized endpoint. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Request)"]
    B["Map Request Params"]
    C["Fetch Token"]
    D["IF: Auth required?"]
    E["Call External API"]
    F["Transform Response"]
    G["Return JSON"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Client request |
| Code | Param mapping |
| IF | Auth check |
| HTTP Request | API call |
| Code | Response transform |
| Webhook | JSON return |

## Dockerfile

Dockerfile: [usecases/196-public-rest-api-wrapper/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/196-public-rest-api-wrapper/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `REST_WRAPPER_WEBHOOK_PATH=api`

## Build & Run

```bash
cd usecases/196-public-rest-api-wrapper

# Build the image
docker build -t n8n-usecase-196 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-196 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-196

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-196:
    image: n8n-usecase-196
    container_name: n8n-usecase-196
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_196_data:/home/node/.n8n"]

volumes:
  n8n_usecase_196_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
