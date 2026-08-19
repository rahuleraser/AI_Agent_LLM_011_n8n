# 142 - Employee Welcome Kit

> **Category:** HR & Internal Ops

Sends a digital welcome kit to new employees. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["HR Trigger (Hire)"]
    B["Build Welcome Kit"]
    C["Send PDF Kit"]
    D["IF: PDF version?"]
    E["Send Online Kit"]
    F["Add to Wiki"]
    G["Notify Buddy"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| HR Trigger | New hire |
| Code | Kit build |
| IF | Format branch |
| Email | Kit send |
| Google Drive | Wiki add |
| Slack | Buddy notify |

## Dockerfile

Dockerfile: [usecases/142-employee-welcome-kit/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/142-employee-welcome-kit/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `WELCOME_WEBHOOK_PATH=welcome-kit`

## Build & Run

```bash
cd usecases/142-employee-welcome-kit

# Build the image
docker build -t n8n-usecase-142 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-142 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-142

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-142:
    image: n8n-usecase-142
    container_name: n8n-usecase-142
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_142_data:/home/node/.n8n"]

volumes:
  n8n_usecase_142_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
