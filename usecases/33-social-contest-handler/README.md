# 033 - Social Contest Handler

> **Category:** Social Media & Marketing

Runs giveaways, picks winners and notifies participants automatically. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Entry)"]
    B["Collect Entries"]
    C["Pick Random Winner"]
    D["IF: Contest ended?"]
    E["Store Entry"]
    F["Notify Winner"]
    G["Log Contest Results"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Entry capture |
| Code | Entry store |
| Cron Trigger | End date |
| Code | Random pick |
| Social API | Winner DM |
| Spreadsheet | Results log |

## Dockerfile

Dockerfile: [usecases/33-social-contest-handler/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/33-social-contest-handler/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `CONTEST_WEBHOOK_PATH=contest-entry`

## Build & Run

```bash
cd usecases/33-social-contest-handler

# Build the image
docker build -t n8n-usecase-033 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-033 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-033

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-033:
    image: n8n-usecase-033
    container_name: n8n-usecase-033
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_033_data:/home/node/.n8n"]

volumes:
  n8n_usecase_033_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
