# 092 - GitHub PR Notifier

> **Category:** Developer & DevOps

Notifies the team when pull requests are created or updated. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["GitHub Trigger (PR)"]
    B["Fetch PR Details"]
    C["Notify Draft Queue"]
    D["IF: Draft or Ready?"]
    E["Notify Review Queue"]
    F["Post to Slack"]
    G["Log PR Activity"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| GitHub Trigger | PR event |
| GitHub | PR details |
| IF | Draft check |
| Slack | Draft notify |
| Slack | Review notify |
| SQLite | PR log |

## Dockerfile

Dockerfile: [usecases/92-github-pr-notifier/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/92-github-pr-notifier/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | `n8n-nodes-github` |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `PR_WEBHOOK_PATH=pr-event`

## Build & Run

```bash
cd usecases/92-github-pr-notifier

# Build the image
docker build -t n8n-usecase-092 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-092 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-092

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-092:
    image: n8n-usecase-092
    container_name: n8n-usecase-092
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_092_data:/home/node/.n8n"]

volumes:
  n8n_usecase_092_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
