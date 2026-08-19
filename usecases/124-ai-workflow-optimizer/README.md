# 124 - AI Workflow Optimizer

> **Category:** AI & LLM

Analyzes workflow logs and suggests optimizations. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Weekly)"]
    B["Fetch Execution Logs"]
    C["Suggest Optimization"]
    D["IF: Bottleneck found?"]
    E["Log Healthy"]
    F["Send AI Report"]
    G["Archive Analysis"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Weekly run |
| SQLite | Execution logs |
| AI LLM | Analyze logs |
| IF | Bottleneck check |
| Email | AI report |
| Google Sheets | Analysis store |

## Dockerfile

Dockerfile: [usecases/124-ai-workflow-optimizer/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/124-ai-workflow-optimizer/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `OPTIMIZE_CRON=0 6 * * 1`

## Build & Run

```bash
cd usecases/124-ai-workflow-optimizer

# Build the image
docker build -t n8n-usecase-124 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-124 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-124

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-124:
    image: n8n-usecase-124
    container_name: n8n-usecase-124
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_124_data:/home/node/.n8n"]

volumes:
  n8n_usecase_124_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
