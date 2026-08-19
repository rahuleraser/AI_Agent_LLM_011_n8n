# 121 - AI Image Generator

> **Category:** AI & LLM

Generates images from text prompts for content creation. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Prompt)"]
    B["Build Image Prompt"]
    C["Generate Artwork"]
    D["IF: Style specified?"]
    E["Use Default Style"]
    F["Save Image"]
    G["Notify Creator"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Prompt inbound |
| AI LLM | Prompt build |
| IF | Style branch |
| HTTP Request | Image API |
| Google Drive | Save image |
| Slack | Creator notify |

## Dockerfile

Dockerfile: [usecases/121-ai-image-generator/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/121-ai-image-generator/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | `n8n-nodes-mcp` |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `IMAGE_WEBHOOK_PATH=image-gen`

## Build & Run

```bash
cd usecases/121-ai-image-generator

# Build the image
docker build -t n8n-usecase-121 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-121 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-121

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-121:
    image: n8n-usecase-121
    container_name: n8n-usecase-121
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_121_data:/home/node/.n8n"]

volumes:
  n8n_usecase_121_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
