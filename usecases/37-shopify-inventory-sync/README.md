# 037 - Shopify Inventory Sync

> **Category:** E-commerce & Retail

Syncs inventory levels between Shopify and a local database. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Hourly)"]
    B["Fetch Product Inventory"]
    C["Update Database"]
    D["IF: Stock changed?"]
    E["Skip Product"]
    F["Alert Low Stock"]
    G["Log Sync"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Polling |
| Shopify | Inventory API |
| IF | Change detection |
| SQLite | Stock store |
| IF | Low stock check |
| Slack | Inventory alert |

## Dockerfile

Dockerfile: [usecases/37-shopify-inventory-sync/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/37-shopify-inventory-sync/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | `n8n-nodes-sqlite` |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `INV_CRON=0 * * * *`
- `LOW_STOCK_THRESHOLD=5`

## Build & Run

```bash
cd usecases/37-shopify-inventory-sync

# Build the image
docker build -t n8n-usecase-037 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-037 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-037

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-037:
    image: n8n-usecase-037
    container_name: n8n-usecase-037
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_037_data:/home/node/.n8n"]

volumes:
  n8n_usecase_037_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
