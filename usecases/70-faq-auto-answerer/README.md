# 070 - FAQ Auto-Answerer

> **Category:** Support & Customer Service

Answers common support questions from a FAQ knowledge base. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Question)"]
    B["Match Question to FAQ"]
    C["Send FAQ Answer"]
    D["IF: Confidence high?"]
    E["Route to Agent"]
    F["Log Unanswered"]
    G["Update FAQ Score"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Question inbound |
| Code | FAQ matching |
| IF | Confidence check |
| Email/Chat | Answer send |
| Slack | Agent route |
| SQLite | Unanswered log |

## Dockerfile

Dockerfile: [usecases/70-faq-auto-answerer/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/70-faq-auto-answerer/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `FAQ_WEBHOOK_PATH=faq-answer`
- `MIN_CONFIDENCE=0.8`

## Build & Run

```bash
cd usecases/70-faq-auto-answerer

# Build the image
docker build -t n8n-usecase-070 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-070 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-070

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-070:
    image: n8n-usecase-070
    container_name: n8n-usecase-070
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_070_data:/home/node/.n8n"]

volumes:
  n8n_usecase_070_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
