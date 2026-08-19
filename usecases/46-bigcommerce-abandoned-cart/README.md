# 046 - BigCommerce Abandoned Cart

> **Category:** E-commerce & Retail

Recovers abandoned carts with automated email nudges. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["BigCommerce Trigger (Cart)"]
    B["Fetch Cart Contents"]
    C["Send Recovery Email"]
    D["IF: Cart abandoned?"]
    E["Ignore Active Cart"]
    F["Apply Discount Code"]
    G["Log Recovery"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| BigCommerce Trigger | Cart event |
| HTTP Request | Cart data |
| IF | Abandon check |
| Email | Recovery email |
| Code | Discount code |
| Spreadsheet | Recovery log |

## Dockerfile

Dockerfile: [usecases/46-bigcommerce-abandoned-cart/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/46-bigcommerce-abandoned-cart/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `BIGCART_WEBHOOK_PATH=cart-abandon`
- `ABANDON_WAIT_HOURS=24`

## Build & Run

```bash
cd usecases/46-bigcommerce-abandoned-cart

# Build the image
docker build -t n8n-usecase-046 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-046 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-046

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-046:
    image: n8n-usecase-046
    container_name: n8n-usecase-046
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_046_data:/home/node/.n8n"]

volumes:
  n8n_usecase_046_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
