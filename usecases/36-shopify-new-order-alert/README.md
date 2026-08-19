# 036 - Shopify New Order Alert

> **Category:** E-commerce & Retail

Alerts the team instantly when a new Shopify order is placed. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Shopify Trigger (New Order)"]
    B["Fetch Order Details"]
    C["Build Alert Message"]
    D["IF: High value order?"]
    E["VIP Channel Alert"]
    F["Standard Channel Alert"]
    G["Log Order Event"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Shopify Trigger | New order |
| HTTP Request | Order details |
| Code | Alert formatting |
| IF | VIP threshold |
| Slack | Channel alerts |
| Spreadsheet | Order log |

## Dockerfile

Dockerfile: [usecases/36-shopify-new-order-alert/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/36-shopify-new-order-alert/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `SHOPIFY_WEBHOOK_PATH=shopify-order`
- `VIP_ORDER_VALUE=500`

## Build & Run

```bash
cd usecases/36-shopify-new-order-alert

# Build the image
docker build -t n8n-usecase-036 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-036 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-036

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-036:
    image: n8n-usecase-036
    container_name: n8n-usecase-036
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_036_data:/home/node/.n8n"]

volumes:
  n8n_usecase_036_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
