# 055 - Lead Scoring Engine

> **Category:** CRM & Sales

Scores every inbound lead using behavior and profile signals. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Lead)"]
    B["Fetch Lead Signals"]
    C["Compute Score"]
    D["IF: Score over 80?"]
    E["Mark as Hot Lead"]
    F["Mark as Nurture"]
    G["Update Score Field"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Lead inbound |
| HTTP Request | Behavior data |
| Code | Score formula |
| IF | Hot threshold |
| CRM | Score field |
| Slack | Hot lead alert |

## Dockerfile

Dockerfile: [usecases/55-lead-scoring-engine/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/55-lead-scoring-engine/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `LEAD_WEBHOOK_PATH=score`
- `HOT_SCORE=80`

## Build & Run

```bash
cd usecases/55-lead-scoring-engine

# Build the image
docker build -t n8n-usecase-055 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-055 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-055

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-055:
    image: n8n-usecase-055
    container_name: n8n-usecase-055
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_055_data:/home/node/.n8n"]

volumes:
  n8n_usecase_055_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
