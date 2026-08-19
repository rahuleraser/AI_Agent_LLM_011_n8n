# 038 - Shopify Refund Processor

> **Category:** E-commerce & Retail

Automates refund workflows and logs refund status to finance. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Shopify Trigger (Refund)"]
    B["Fetch Refund Details"]
    C["Process Refund"]
    D["IF: Refund valid?"]
    E["Flag for Review"]
    F["Update Finance Sheet"]
    G["Notify Customer"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Shopify Trigger | Refund event |
| Code | Validates refund |
| Stripe | Processes refund |
| IF | Validation branch |
| Google Sheets | Finance log |
| Email | Customer notice |

## Dockerfile

Dockerfile: [usecases/38-shopify-refund-processor/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/38-shopify-refund-processor/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | `n8n-nodes-stripe` |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `REFUND_WEBHOOK_PATH=refund`

## Build & Run

```bash
cd usecases/38-shopify-refund-processor

# Build the image
docker build -t n8n-usecase-038 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-038 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-038

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-038:
    image: n8n-usecase-038
    container_name: n8n-usecase-038
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_038_data:/home/node/.n8n"]

volumes:
  n8n_usecase_038_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
