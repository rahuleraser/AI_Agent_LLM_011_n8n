# 125 - AI Code Reviewer

> **Category:** AI & LLM

Reviews pull requests and posts AI code feedback. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["GitHub Trigger (PR)"]
    B["Fetch PR Diff"]
    C["Generate Review"]
    D["IF: Changed files?"]
    E["Post Review Comment"]
    F["Log Review"]
    G["Notify Author"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| GitHub Trigger | PR open |
| GitHub | Diff fetch |
| AI LLM | Review generate |
| IF | Diff check |
| GitHub | Comment post |
| SQLite | Review log |

## Dockerfile

Dockerfile: [usecases/125-ai-code-reviewer/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/125-ai-code-reviewer/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | `n8n-nodes-github`, `n8n-nodes-mcp` |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `AI_REVIEW_WEBHOOK_PATH=code-review`

## Build & Run

```bash
cd usecases/125-ai-code-reviewer

# Build the image
docker build -t n8n-usecase-125 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-125 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-125

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-125:
    image: n8n-usecase-125
    container_name: n8n-usecase-125
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_125_data:/home/node/.n8n"]

volumes:
  n8n_usecase_125_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
