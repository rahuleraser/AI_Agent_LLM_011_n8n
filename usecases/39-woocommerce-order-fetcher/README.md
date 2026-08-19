# 039 - WooCommerce Order Fetcher

> **Category:** E-commerce & Retail

Imports new WooCommerce orders into a central spreadsheet. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["WooCommerce Trigger (Order)"]
    B["Fetch Order Items"]
    C["Normalize Fields"]
    D["IF: Duplicate order?"]
    E["Skip Import"]
    F["Append to Sheet"]
    G["Notify Team"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| WooCommerce Trigger | New order |
| HTTP Request | Order data |
| Code | Normalizes fields |
| IF | Duplicate check |
| Google Sheets | Order ledger |
| Slack | Team notice |

## Dockerfile

Dockerfile: [usecases/39-woocommerce-order-fetcher/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/39-woocommerce-order-fetcher/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `WOO_WEBHOOK_PATH=woo-order`

## Build & Run

```bash
cd usecases/39-woocommerce-order-fetcher

# Build the image
docker build -t n8n-usecase-039 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-039 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-039

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-039:
    image: n8n-usecase-039
    container_name: n8n-usecase-039
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_039_data:/home/node/.n8n"]

volumes:
  n8n_usecase_039_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
