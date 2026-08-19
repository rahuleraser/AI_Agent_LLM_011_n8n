# 150 - Employee Anniversary Greeting

> **Category:** HR & Internal Ops

Automatically greets employees on work anniversaries. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Daily)"]
    B["Check Anniversary Dates"]
    C["Send Greeting"]
    D["IF: Anniversary today?"]
    E["Skip Day"]
    F["Post to Team Channel"]
    G["Log Greetings"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Daily check |
| SQLite | Employee records |
| IF | Date match |
| Email | Greeting send |
| Slack | Team channel post |
| SQLite | Greeting log |

## Dockerfile

Dockerfile: [usecases/150-employee-anniversary-greeting/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/150-employee-anniversary-greeting/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `ANNIVERSARY_CRON=0 9 * * *`

## Build & Run

```bash
cd usecases/150-employee-anniversary-greeting

# Build the image
docker build -t n8n-usecase-150 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-150 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-150

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-150:
    image: n8n-usecase-150
    container_name: n8n-usecase-150
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_150_data:/home/node/.n8n"]

volumes:
  n8n_usecase_150_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
