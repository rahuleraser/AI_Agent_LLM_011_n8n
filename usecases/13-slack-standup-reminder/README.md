# 013 - Slack Standup Reminder

> **Category:** Email & Communication

Posts daily standup prompts and collects team updates in one thread. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Daily 9am)"]
    B["Build Standup Prompt"]
    C["Post to Slack Thread"]
    D["IF: Replies collected?"]
    E["Compile Update Summary"]
    F["Remind Again"]
    G["Save to Sheet"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Daily prompt |
| Slack | Posts prompt |
| Wait | Collects replies |
| Code | Compiles summary |
| IF | Completion check |
| Google Sheets | Stores updates |

## Dockerfile

Dockerfile: [usecases/13-slack-standup-reminder/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/13-slack-standup-reminder/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `STANDUP_CRON=0 9 * * 1-5`
- `STANDUP_CHANNEL=team`

## Build & Run

```bash
cd usecases/13-slack-standup-reminder

# Build the image
docker build -t n8n-usecase-013 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-013 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-013

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-013:
    image: n8n-usecase-013
    container_name: n8n-usecase-013
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_013_data:/home/node/.n8n"]

volumes:
  n8n_usecase_013_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
