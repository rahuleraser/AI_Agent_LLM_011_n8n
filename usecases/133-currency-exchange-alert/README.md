# 133 - Currency Exchange Alert

> **Category:** Finance & Accounting

Alerts when currency exchange rates hit targets. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Hourly)"]
    B["Fetch Exchange Rates"]
    C["Send Rate Alert"]
    D["IF: Rate target hit?"]
    E["Log Rates"]
    F["Update Tracker"]
    G["Notify Trader"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Rate poll |
| HTTP Request | FX API |
| IF | Target check |
| Email | Rate alert |
| Google Sheets | Rate tracker |
| Slack | Trader notify |

## Dockerfile

Dockerfile: [usecases/133-currency-exchange-alert/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/133-currency-exchange-alert/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `FX_CRON=0 * * * *`
- `FX_TARGET=1.10`

## Build & Run

```bash
cd usecases/133-currency-exchange-alert

# Build the image
docker build -t n8n-usecase-133 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-133 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-133

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-133:
    image: n8n-usecase-133
    container_name: n8n-usecase-133
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_133_data:/home/node/.n8n"]

volumes:
  n8n_usecase_133_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
