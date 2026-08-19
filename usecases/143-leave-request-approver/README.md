# 143 - Leave Request Approver

> **Category:** HR & Internal Ops

Routes leave requests to managers for approval. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["HR Trigger (Leave Request)"]
    B["Fetch Request Details"]
    C["Notify Manager"]
    D["IF: Available balance?"]
    E["Reject Request"]
    F["Update Leave Calendar"]
    G["Log Decision"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| HR Trigger | Leave request |
| Code | Balance check |
| IF | Balance branch |
| Email | Manager approval |
| Google Calendar | Leave update |
| SQLite | Decision log |

## Dockerfile

Dockerfile: [usecases/143-leave-request-approver/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/143-leave-request-approver/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `LEAVE_WEBHOOK_PATH=leave`

## Build & Run

```bash
cd usecases/143-leave-request-approver

# Build the image
docker build -t n8n-usecase-143 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-143 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-143

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-143:
    image: n8n-usecase-143
    container_name: n8n-usecase-143
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_143_data:/home/node/.n8n"]

volumes:
  n8n_usecase_143_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
