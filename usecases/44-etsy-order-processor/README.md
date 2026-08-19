# 044 - Etsy Order Processor

> **Category:** E-commerce & Retail

Processes Etsy orders and sends confirmation emails automatically. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Etsy Trigger (New Order)"]
    B["Fetch Order Details"]
    C["Generate Confirmation"]
    D["IF: Digital item?"]
    E["Send Digital Link"]
    F["Send Shipping Update"]
    G["Log Order"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Etsy Trigger | New order |
| HTTP Request | Order details |
| Email | Confirmation |
| IF | Item type branch |
| Email | Digital delivery |
| Spreadsheet | Order log |

## Dockerfile

Dockerfile: [usecases/44-etsy-order-processor/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/44-etsy-order-processor/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `ETSY_WEBHOOK_PATH=etsy-order`

## Build & Run

```bash
cd usecases/44-etsy-order-processor

# Build the image
docker build -t n8n-usecase-044 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-044 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-044

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-044:
    image: n8n-usecase-044
    container_name: n8n-usecase-044
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_044_data:/home/node/.n8n"]

volumes:
  n8n_usecase_044_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
