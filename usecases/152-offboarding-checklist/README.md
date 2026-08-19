# 152 - Offboarding Checklist

> **Category:** HR & Internal Ops

Runs the offboarding checklist when employees leave. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["HR Trigger (Offboarding)"]
    B["Create Checklist"]
    C["Collect Assets"]
    D["IF: Has company assets?"]
    E["Revoke Access"]
    F["Send Exit Survey"]
    G["Notify IT"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| HR Trigger | Departure |
| Google Sheets | Checklist |
| IF | Asset check |
| Email | Asset return |
| IT | Access revoke |
| Email | Exit survey |

## Dockerfile

Dockerfile: [usecases/152-offboarding-checklist/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/152-offboarding-checklist/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `OFFBOARD_WEBHOOK_PATH=offboard`

## Build & Run

```bash
cd usecases/152-offboarding-checklist

# Build the image
docker build -t n8n-usecase-152 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-152 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-152

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-152:
    image: n8n-usecase-152
    container_name: n8n-usecase-152
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_152_data:/home/node/.n8n"]

volumes:
  n8n_usecase_152_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
