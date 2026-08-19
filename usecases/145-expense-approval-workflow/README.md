# 145 - Expense Approval Workflow

> **Category:** HR & Internal Ops

Routes expense claims through an approval chain. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["HR Trigger (Expense)"]
    B["Validate Receipt"]
    C["Auto-approve"]
    D["IF: Under 100?"]
    E["Forward to Manager"]
    F["Update Ledger"]
    G["Notify Employee"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| HR Trigger | Expense claim |
| Code | Receipt check |
| IF | Amount branch |
| Email | Approval request |
| Google Sheets | Ledger |
| Slack | Employee notify |

## Dockerfile

Dockerfile: [usecases/145-expense-approval-workflow/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/145-expense-approval-workflow/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `EXPENSE_APPROVE_WEBHOOK_PATH=expense-approve`
- `AUTO_APPROVE_LIMIT=100`

## Build & Run

```bash
cd usecases/145-expense-approval-workflow

# Build the image
docker build -t n8n-usecase-145 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-145 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-145

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-145:
    image: n8n-usecase-145
    container_name: n8n-usecase-145
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_145_data:/home/node/.n8n"]

volumes:
  n8n_usecase_145_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
