# 016 - Twitter Auto-Reply

> **Category:** Social Media & Marketing

Replies to Twitter mentions automatically with helpful answers. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Twitter Trigger (Mention)"]
    B["Analyze Tweet Intent"]
    C["Build Reply Text"]
    D["IF: Needs escalation?"]
    E["DM Support Team"]
    F["Post Public Reply"]
    G["Log Interactions"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Twitter Trigger | Mentions |
| Code | Intent analysis |
| Twitter | Public reply |
| IF | Escalation branch |
| Slack | Alerts support |
| SQLite | Interaction log |

## Dockerfile

Dockerfile: [usecases/16-twitter-auto-reply/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/16-twitter-auto-reply/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `TWITTER_WEBHOOK_PATH=tw-reply`

## Build & Run

```bash
cd usecases/16-twitter-auto-reply

# Build the image
docker build -t n8n-usecase-016 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-016 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-016

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-016:
    image: n8n-usecase-016
    container_name: n8n-usecase-016
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_016_data:/home/node/.n8n"]

volumes:
  n8n_usecase_016_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
