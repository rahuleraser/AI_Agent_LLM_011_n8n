# 138 - Revenue Reconciler

> **Category:** Finance & Accounting

Reconciles revenue between payment processors and books. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Daily)"]
    B["Fetch Payment Totals"]
    C["Fetch Book Totals"]
    D["IF: Difference?"]
    E["Create Adjustments"]
    F["Mark Reconciled"]
    G["Email Reconciliation Report"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Daily reconcile |
| Stripe | Payment totals |
| HTTP Request | Book totals |
| IF | Diff check |
| Google Sheets | Adjustments |
| Email | Report send |

## Dockerfile

Dockerfile: [usecases/138-revenue-reconciler/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/138-revenue-reconciler/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | `n8n-nodes-stripe` |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `RECON_CRON=0 4 * * *`

## Build & Run

```bash
cd usecases/138-revenue-reconciler

# Build the image
docker build -t n8n-usecase-138 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-138 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-138

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-138:
    image: n8n-usecase-138
    container_name: n8n-usecase-138
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_138_data:/home/node/.n8n"]

volumes:
  n8n_usecase_138_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
