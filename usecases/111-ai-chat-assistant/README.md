# 111 - AI Chat Assistant

> **Category:** AI & LLM

Builds an AI chatbot that answers questions from your data. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (User Chat)"]
    B["Load Context Documents"]
    C["Answer with RAG"]
    D["IF: Retrieval ok?"]
    E["Fallback Answer"]
    F["Stream Response"]
    G["Log Conversation"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | User message |
| Vector Store | Context load |
| AI Agent | RAG answer |
| IF | Retrieval check |
| Webhook | Response send |
| SQLite | Conversation log |

## Dockerfile

Dockerfile: [usecases/111-ai-chat-assistant/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/111-ai-chat-assistant/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | `n8n-nodes-mcp` |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `CHAT_WEBHOOK_PATH=chat`
- `LLM_MODEL=your-model`

## Build & Run

```bash
cd usecases/111-ai-chat-assistant

# Build the image
docker build -t n8n-usecase-111 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-111 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-111

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-111:
    image: n8n-usecase-111
    container_name: n8n-usecase-111
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_111_data:/home/node/.n8n"]

volumes:
  n8n_usecase_111_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
