# 126 - Invoice Generator

> **Category:** Finance & Accounting

Generates invoices from order data and emails them. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Order Webhook"]
    B["Build Invoice Data"]
    C["Add Tax Line"]
    D["IF: Tax applicable?"]
    E["Generate Invoice PDF"]
    F["Email Invoice"]
    G["Log Invoice"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Order event |
| Code | Invoice build |
| IF | Tax check |
| PDF | Generate document |
| Email | Send invoice |
| MongoDB | Invoice archive |

## Dockerfile

Dockerfile: [usecases/126-invoice-generator/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/126-invoice-generator/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | `n8n-nodes-mongodb` |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `INVOICE_WEBHOOK_PATH=invoice`
- `TAX_RATE=0.0`

## Build & Run

```bash
cd usecases/126-invoice-generator

# Build the image
docker build -t n8n-usecase-126 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-126 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-126

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-126:
    image: n8n-usecase-126
    container_name: n8n-usecase-126
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_126_data:/home/node/.n8n"]

volumes:
  n8n_usecase_126_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
