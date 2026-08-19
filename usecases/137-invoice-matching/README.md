# 137 - Invoice Matching

> **Category:** Finance & Accounting

Matches invoices against purchase orders automatically. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Invoice)"]
    B["Fetch Purchase Order"]
    C["Approve for Payment"]
    D["IF: Amount matches?"]
    E["Flag Mismatch"]
    F["Log Matching"]
    G["Notify AP Team"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Invoice in |
| HTTP Request | PO lookup |
| IF | Amount check |
| Google Sheets | Approval log |
| Slack | AP alert |
| SQLite | Match log |

## Dockerfile

Dockerfile: [usecases/137-invoice-matching/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/137-invoice-matching/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `MATCH_WEBHOOK_PATH=invoice-match`

## Build & Run

```bash
cd usecases/137-invoice-matching

# Build the image
docker build -t n8n-usecase-137 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-137 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-137

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-137:
    image: n8n-usecase-137
    container_name: n8n-usecase-137
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_137_data:/home/node/.n8n"]

volumes:
  n8n_usecase_137_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
