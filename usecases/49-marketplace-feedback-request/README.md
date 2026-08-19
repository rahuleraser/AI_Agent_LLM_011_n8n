# 049 - Marketplace Feedback Request

> **Category:** E-commerce & Retail

Requests reviews from buyers after successful deliveries. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Order Trigger (Delivered)"]
    B["Build Feedback Request"]
    C["Send Feedback Email"]
    D["IF: Eligible for review?"]
    E["Skip Buyer"]
    F["Wait for Reply"]
    G["Log Requests"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Order Trigger | Delivery event |
| Code | Eligibility check |
| IF | Review eligibility |
| Email | Feedback request |
| Wait | Reply window |
| Spreadsheet | Request log |

## Dockerfile

Dockerfile: [usecases/49-marketplace-feedback-request/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/49-marketplace-feedback-request/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `FEEDBACK_WAIT_DAYS=7`

## Build & Run

```bash
cd usecases/49-marketplace-feedback-request

# Build the image
docker build -t n8n-usecase-049 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-049 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-049

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-049:
    image: n8n-usecase-049
    container_name: n8n-usecase-049
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_049_data:/home/node/.n8n"]

volumes:
  n8n_usecase_049_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
