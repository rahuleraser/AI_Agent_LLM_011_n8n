# 061 - CRM Task Auto-creator

> **Category:** CRM & Sales

Automatically creates follow-up tasks in CRM from email mentions. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Email Trigger (Mention)"]
    B["Extract Actionable Text"]
    C["Create CRM Task"]
    D["IF: Action required?"]
    E["Ignore Email"]
    F["Assign Task Owner"]
    G["Notify Assignee"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Email Trigger | Inbound mail |
| AI | Action extraction |
| IF | Action detection |
| CRM | Create task |
| CRM | Assign owner |
| Slack | Assignee alert |

## Dockerfile

Dockerfile: [usecases/61-crm-task-auto-creator/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/61-crm-task-auto-creator/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `TASK_WEBHOOK_PATH=crm-task`

## Build & Run

```bash
cd usecases/61-crm-task-auto-creator

# Build the image
docker build -t n8n-usecase-061 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-061 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-061

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-061:
    image: n8n-usecase-061
    container_name: n8n-usecase-061
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_061_data:/home/node/.n8n"]

volumes:
  n8n_usecase_061_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
