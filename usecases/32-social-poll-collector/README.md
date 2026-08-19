# 032 - Social Poll Collector

> **Category:** Social Media & Marketing

Collects poll responses from social platforms and analyzes results. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Social Trigger (Poll Response)"]
    B["Capture Response"]
    C["Compile Results"]
    D["IF: Poll closed?"]
    E["Record Vote"]
    F["Publish Result Post"]
    G["Log to Sheet"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Social Trigger | Poll events |
| Code | Captures votes |
| IF | Closure check |
| Google Sheets | Vote log |
| Social API | Publishes result |
| Code | Compiles results |

## Dockerfile

Dockerfile: [usecases/32-social-poll-collector/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/32-social-poll-collector/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `POLL_WEBHOOK_PATH=poll-vote`

## Build & Run

```bash
cd usecases/32-social-poll-collector

# Build the image
docker build -t n8n-usecase-032 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-032 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-032

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-032:
    image: n8n-usecase-032
    container_name: n8n-usecase-032
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_032_data:/home/node/.n8n"]

volumes:
  n8n_usecase_032_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
