# 199 - iPaaS Style Data Router

> **Category:** API Integration & Automation

Routes data between systems like an integration platform. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Record)"]
    B["Detect Target System"]
    C["Transform and Send"]
    D["IF: Mapping exists?"]
    E["Flag Missing Mapping"]
    F["Log Route"]
    G["Notify Integration Team"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Record inbound |
| Code | Target detect |
| IF | Mapping check |
| HTTP Request | Send target |
| Google Sheets | Missing log |
| Slack | Integration alert |

## Dockerfile

Dockerfile: [usecases/199-ipaas-style-data-router/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/199-ipaas-style-data-router/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `ROUTER_WEBHOOK_PATH=router`

## Build & Run

```bash
cd usecases/199-ipaas-style-data-router

# Build the image
docker build -t n8n-usecase-199 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-199 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-199

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-199:
    image: n8n-usecase-199
    container_name: n8n-usecase-199
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_199_data:/home/node/.n8n"]

volumes:
  n8n_usecase_199_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
