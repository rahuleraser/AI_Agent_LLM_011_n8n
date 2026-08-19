# 030 - Social Media Ad Monitor

> **Category:** Social Media & Marketing

Monitors ad campaign budgets and performance across platforms. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Daily)"]
    B["Pull Ad Spend Metrics"]
    C["Alert Marketing Team"]
    D["IF: Spend over budget?"]
    E["Log Performance"]
    F["Pause Underperforming Ads"]
    G["Email Daily Summary"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Daily pull |
| Facebook Ads API | Metrics |
| IF | Budget check |
| Slack | Marketing alert |
| Facebook Ads | Pause action |
| Email | Summary report |

## Dockerfile

Dockerfile: [usecases/30-social-media-ad-monitor/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/30-social-media-ad-monitor/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `AD_MONITOR_CRON=0 8 * * *`
- `AD_BUDGET=100`

## Build & Run

```bash
cd usecases/30-social-media-ad-monitor

# Build the image
docker build -t n8n-usecase-030 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-030 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-030

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-030:
    image: n8n-usecase-030
    container_name: n8n-usecase-030
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_030_data:/home/node/.n8n"]

volumes:
  n8n_usecase_030_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
