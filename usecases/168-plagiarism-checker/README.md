# 168 - Plagiarism Checker

> **Category:** Content & Publishing

Checks blog content for plagiarism before publishing. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Content)"]
    B["Send to Checker"]
    C["Flag for Rewrite"]
    D["IF: Similarity high?"]
    E["Approve Content"]
    F["Log Checks"]
    G["Notify Editor"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Content submit |
| HTTP Request | Plagiarism API |
| IF | Similarity check |
| Google Docs | Flag copy |
| Slack | Editor notify |
| SQLite | Check log |

## Dockerfile

Dockerfile: [usecases/168-plagiarism-checker/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/168-plagiarism-checker/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `PLAGIARISM_WEBHOOK_PATH=plagiarism`

## Build & Run

```bash
cd usecases/168-plagiarism-checker

# Build the image
docker build -t n8n-usecase-168 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-168 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-168

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-168:
    image: n8n-usecase-168
    container_name: n8n-usecase-168
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_168_data:/home/node/.n8n"]

volumes:
  n8n_usecase_168_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
