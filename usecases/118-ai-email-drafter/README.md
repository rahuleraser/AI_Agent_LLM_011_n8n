# 118 - AI Email Drafter

> **Category:** AI & LLM

Drafts email responses for support agents to review. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Email Trigger (Support)"]
    B["Summarize Thread"]
    C["Generate Draft Reply"]
    D["IF: Approved?"]
    E["Send Draft"]
    F["Save for Edit"]
    G["Log Drafts"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Email Trigger | Inbound thread |
| AI LLM | Draft generate |
| IF | Approval branch |
| Email Send | Send reply |
| Google Docs | Draft store |
| SQLite | Draft log |

## Dockerfile

Dockerfile: [usecases/118-ai-email-drafter/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/118-ai-email-drafter/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `DRAFT_WEBHOOK_PATH=email-draft`

## Build & Run

```bash
cd usecases/118-ai-email-drafter

# Build the image
docker build -t n8n-usecase-118 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-118 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-118

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-118:
    image: n8n-usecase-118
    container_name: n8n-usecase-118
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_118_data:/home/node/.n8n"]

volumes:
  n8n_usecase_118_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
