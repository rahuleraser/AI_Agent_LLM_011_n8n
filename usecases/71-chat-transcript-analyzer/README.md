# 071 - Chat Transcript Analyzer

> **Category:** Support & Customer Service

Analyzes chat transcripts for quality and escalations. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Chat Trigger (Transcript)"]
    B["Fetch Transcript"]
    C["Flag for Review"]
    D["IF: Negative sentiment?"]
    E["Log Transcript"]
    F["Score Quality"]
    G["Email Summary"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Chat Trigger | Transcript end |
| AI | Sentiment analysis |
| IF | Negative flag |
| Slack | Review flag |
| SQLite | Transcript store |
| Email | Quality report |

## Dockerfile

Dockerfile: [usecases/71-chat-transcript-analyzer/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/71-chat-transcript-analyzer/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `CHAT_WEBHOOK_PATH=transcript`

## Build & Run

```bash
cd usecases/71-chat-transcript-analyzer

# Build the image
docker build -t n8n-usecase-071 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-071 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-071

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-071:
    image: n8n-usecase-071
    container_name: n8n-usecase-071
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_071_data:/home/node/.n8n"]

volumes:
  n8n_usecase_071_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
