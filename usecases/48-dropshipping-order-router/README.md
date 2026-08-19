# 048 - Dropshipping Order Router

> **Category:** E-commerce & Retail

Routes dropship orders to the correct supplier automatically. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Shopify Trigger (Order)"]
    B["Match Product to Supplier"]
    C["Send Order to Supplier"]
    D["IF: Supplier found?"]
    E["Flag Manual Handling"]
    F["Log Routing"]
    G["Notify Supplier"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Shopify Trigger | New order |
| Code | Supplier match |
| IF | Match check |
| Email | Supplier order |
| Google Sheets | Routing log |
| Slack | Manual flag |

## Dockerfile

Dockerfile: [usecases/48-dropshipping-order-router/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/48-dropshipping-order-router/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `DROPSHIP_WEBHOOK_PATH=dropship-route`

## Build & Run

```bash
cd usecases/48-dropshipping-order-router

# Build the image
docker build -t n8n-usecase-048 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-048 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-048

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-048:
    image: n8n-usecase-048
    container_name: n8n-usecase-048
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_048_data:/home/node/.n8n"]

volumes:
  n8n_usecase_048_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
