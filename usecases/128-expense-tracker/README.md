# 128 - Expense Tracker

> **Category:** Finance & Accounting

Tracks expenses from receipts and categorizes them. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Email Trigger (Receipt)"]
    B["Extract Receipt Data"]
    C["Categorize Expense"]
    D["IF: Amount valid?"]
    E["Flag Receipt"]
    F["Append to Ledger"]
    G["Notify Approver"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Email Trigger | Receipt mail |
| AI LLM | Receipt parse |
| IF | Amount check |
| Google Sheets | Ledger append |
| Slack | Approver notify |
| SQLite | Expense log |

## Dockerfile

Dockerfile: [usecases/128-expense-tracker/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/128-expense-tracker/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `EXPENSE_WEBHOOK_PATH=expense`

## Build & Run

```bash
cd usecases/128-expense-tracker

# Build the image
docker build -t n8n-usecase-128 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-128 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-128

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-128:
    image: n8n-usecase-128
    container_name: n8n-usecase-128
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_128_data:/home/node/.n8n"]

volumes:
  n8n_usecase_128_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
