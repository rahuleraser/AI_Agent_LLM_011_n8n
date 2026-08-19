# 193 - OAuth Token Refresher

> **Category:** API Integration & Automation

Refreshes OAuth tokens before they expire. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Hourly)"]
    B["Check Token Expiry"]
    C["Refresh Token"]
    D["IF: Expires in 1h?"]
    E["Store New Token"]
    F["Alert on Failure"]
    G["Notify Integration Owner"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Token check |
| SQLite | Token store |
| IF | Expiry window |
| HTTP Request | Refresh call |
| SQLite | Token update |
| Slack | Failure alert |

## Dockerfile

Dockerfile: [usecases/193-oauth-token-refresher/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/193-oauth-token-refresher/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `OAUTH_CRON=0 * * * *`
- `REFRESH_WINDOW_MIN=60`

## Build & Run

```bash
cd usecases/193-oauth-token-refresher

# Build the image
docker build -t n8n-usecase-193 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-193 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-193

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-193:
    image: n8n-usecase-193
    container_name: n8n-usecase-193
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_193_data:/home/node/.n8n"]

volumes:
  n8n_usecase_193_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
