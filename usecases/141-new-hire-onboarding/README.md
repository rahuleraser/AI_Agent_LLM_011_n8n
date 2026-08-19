# 141 - New Hire Onboarding

> **Category:** HR & Internal Ops

Automates the new hire onboarding checklist and welcome emails. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["HR Trigger (Hire)"]
    B["Create Onboarding Tasks"]
    C["Order Equipment"]
    D["IF: Role has equipment?"]
    E["Send Welcome Email"]
    F["Grant Access"]
    G["Notify Manager"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| HR Trigger | New hire |
| Google Sheets | Task list |
| IF | Equipment check |
| Email | Access requests |
| Email | Welcome send |
| Slack | Manager notify |

## Dockerfile

Dockerfile: [usecases/141-new-hire-onboarding/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/141-new-hire-onboarding/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `ONBOARD_WEBHOOK_PATH=onboard`

## Build & Run

```bash
cd usecases/141-new-hire-onboarding

# Build the image
docker build -t n8n-usecase-141 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-141 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-141

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-141:
    image: n8n-usecase-141
    container_name: n8n-usecase-141
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_141_data:/home/node/.n8n"]

volumes:
  n8n_usecase_141_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
