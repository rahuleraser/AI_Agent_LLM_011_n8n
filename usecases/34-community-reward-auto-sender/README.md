# 034 - Community Reward Auto-sender

> **Category:** Social Media & Marketing

Automatically sends rewards to community members who complete actions. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Action Completed)"]
    B["Verify Action"]
    C["Send Reward Code"]
    D["IF: Reward eligible?"]
    E["Log Attempt"]
    F["Notify Member"]
    G["Update Points Ledger"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Action event |
| Code | Verifies action |
| IF | Eligibility check |
| Email | Sends reward |
| SQLite | Ledger |
| Slack | Admin log |

## Dockerfile

Dockerfile: [usecases/34-community-reward-auto-sender/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/34-community-reward-auto-sender/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | `n8n-nodes-sqlite` |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `REWARD_WEBHOOK_PATH=reward`

## Build & Run

```bash
cd usecases/34-community-reward-auto-sender

# Build the image
docker build -t n8n-usecase-034 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-034 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-034

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-034:
    image: n8n-usecase-034
    container_name: n8n-usecase-034
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_034_data:/home/node/.n8n"]

volumes:
  n8n_usecase_034_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
