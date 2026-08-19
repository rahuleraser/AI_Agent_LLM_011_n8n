# 185 - Daily Standup Summary

> **Category:** Monitoring & Alerts

Collects standup updates and posts a team summary. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Daily)"]
    B["Collect Updates"]
    C["Compile Summary"]
    D["IF: Blockers reported?"]
    E["Flag Blockers"]
    F["Post Summary"]
    G["Archive Updates"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | End of day |
| Slack | Update collect |
| Code | Summary build |
| IF | Blocker check |
| Slack | Summary post |
| Google Sheets | Archive |

## Dockerfile

Dockerfile: [usecases/185-daily-standup-summary/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/185-daily-standup-summary/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `STANDUP_SUMMARY_CRON=0 18 * * *`

## Build & Run

```bash
cd usecases/185-daily-standup-summary

# Build the image
docker build -t n8n-usecase-185 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-185 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-185

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-185:
    image: n8n-usecase-185
    container_name: n8n-usecase-185
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_185_data:/home/node/.n8n"]

volumes:
  n8n_usecase_185_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
