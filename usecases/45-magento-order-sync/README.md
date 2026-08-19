# 045 - Magento Order Sync

> **Category:** E-commerce & Retail

Syncs Magento orders to accounting and fulfillment tools. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Magento Trigger (Order)"]
    B["Fetch Order Payload"]
    C["Create Fulfillment Task"]
    D["IF: Payment received?"]
    E["Flag Unpaid Order"]
    F["Update Accounting Sheet"]
    G["Notify Ops Team"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Magento Trigger | Order event |
| HTTP Request | Order data |
| IF | Payment check |
| Google Sheets | Fulfillment |
| Google Sheets | Accounting |
| Slack | Ops alert |

## Dockerfile

Dockerfile: [usecases/45-magento-order-sync/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/45-magento-order-sync/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `MAGENTO_WEBHOOK_PATH=magento-order`

## Build & Run

```bash
cd usecases/45-magento-order-sync

# Build the image
docker build -t n8n-usecase-045 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-045 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-045

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-045:
    image: n8n-usecase-045
    container_name: n8n-usecase-045
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_045_data:/home/node/.n8n"]

volumes:
  n8n_usecase_045_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
