# 132 - Subscription Cost Analyzer

> **Category:** Finance & Accounting

Analyzes SaaS subscription costs across the company. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Monthly)"]
    B["Collect Subscription Bills"]
    C["Alert Finance"]
    D["IF: Cost over budget?"]
    E["Log Costs"]
    F["Generate Report"]
    G["Notify Stakeholders"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Monthly run |
| HTTP Request | Billing APIs |
| IF | Budget check |
| Slack | Finance alert |
| Google Sheets | Cost log |
| Email | Report send |

## Dockerfile

Dockerfile: [usecases/132-subscription-cost-analyzer/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/132-subscription-cost-analyzer/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `SUB_CRON=0 7 1 * *`
- `SUB_BUDGET=5000`

## Build & Run

```bash
cd usecases/132-subscription-cost-analyzer

# Build the image
docker build -t n8n-usecase-132 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-132 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-132

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-132:
    image: n8n-usecase-132
    container_name: n8n-usecase-132
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_132_data:/home/node/.n8n"]

volumes:
  n8n_usecase_132_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
