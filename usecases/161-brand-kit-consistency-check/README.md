# 161 - Brand Kit Consistency Check

> **Category:** Content & Publishing

Checks content against brand guidelines. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Content)"]
    B["Extract Colors and Fonts"]
    C["Approve Content"]
    D["IF: Matches brand?"]
    E["Flag Violation"]
    F["Log Checks"]
    G["Notify Brand Manager"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Content submit |
| Code | Brand extract |
| IF | Match check |
| Google Sheets | Approval log |
| Slack | Brand manager alert |
| SQLite | Check log |

## Dockerfile

Dockerfile: [usecases/161-brand-kit-consistency-check/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/161-brand-kit-consistency-check/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `BRAND_CHECK_WEBHOOK_PATH=brand-check`

## Build & Run

```bash
cd usecases/161-brand-kit-consistency-check

# Build the image
docker build -t n8n-usecase-161 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-161 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-161

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-161:
    image: n8n-usecase-161
    container_name: n8n-usecase-161
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_161_data:/home/node/.n8n"]

volumes:
  n8n_usecase_161_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
