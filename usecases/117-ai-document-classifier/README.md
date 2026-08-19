# 117 - AI Document Classifier

> **Category:** AI & LLM

Classifies uploaded documents into categories. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Document)"]
    B["Extract Document Text"]
    C["Assign Category"]
    D["IF: Confidence high?"]
    E["Flag for Review"]
    F["Update Record"]
    G["Notify Owner"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | File upload |
| Code | Text extract |
| AI LLM | Category classify |
| IF | Confidence check |
| Google Sheets | Category store |
| Slack | Review flag |

## Dockerfile

Dockerfile: [usecases/117-ai-document-classifier/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/117-ai-document-classifier/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `CLASSIFY_WEBHOOK_PATH=classify`

## Build & Run

```bash
cd usecases/117-ai-document-classifier

# Build the image
docker build -t n8n-usecase-117 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-117 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-117

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-117:
    image: n8n-usecase-117
    container_name: n8n-usecase-117
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_117_data:/home/node/.n8n"]

volumes:
  n8n_usecase_117_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
