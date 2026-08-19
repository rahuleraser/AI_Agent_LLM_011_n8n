# 110 - Code Coverage Reporter

> **Category:** Developer & DevOps

Collects code coverage results and posts them after CI runs. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Coverage)"]
    B["Parse Coverage Report"]
    C["Alert Dev Team"]
    D["IF: Coverage dropped?"]
    E["Post Coverage Summary"]
    F["Update Tracker"]
    G["Notify Maintainers"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Coverage event |
| Code | Parse report |
| IF | Drop detection |
| Slack | Dev alert |
| GitHub | PR comment |
| Google Sheets | Coverage tracker |

## Dockerfile

Dockerfile: [usecases/110-code-coverage-reporter/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/110-code-coverage-reporter/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `COVERAGE_WEBHOOK_PATH=coverage`

## Build & Run

```bash
cd usecases/110-code-coverage-reporter

# Build the image
docker build -t n8n-usecase-110 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-110 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-110

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-110:
    image: n8n-usecase-110
    container_name: n8n-usecase-110
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_110_data:/home/node/.n8n"]

volumes:
  n8n_usecase_110_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
