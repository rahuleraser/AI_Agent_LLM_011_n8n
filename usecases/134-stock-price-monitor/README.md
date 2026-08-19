# 134 - Stock Price Monitor

> **Category:** Finance & Accounting

Monitors stock prices and sends alerts on movements. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (15 min)"]
    B["Fetch Stock Quotes"]
    C["Send Price Alert"]
    D["IF: Price limit hit?"]
    E["Log Prices"]
    F["Update Watchlist"]
    G["Notify Investor"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Quote poll |
| HTTP Request | Stock API |
| IF | Limit check |
| Email | Price alert |
| Google Sheets | Watchlist |
| SQLite | Price log |

## Dockerfile

Dockerfile: [usecases/134-stock-price-monitor/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/134-stock-price-monitor/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `STOCK_CRON=*/15 * * * *`
- `STOCK_SYMBOL=APPL`

## Build & Run

```bash
cd usecases/134-stock-price-monitor

# Build the image
docker build -t n8n-usecase-134 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-134 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-134

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-134:
    image: n8n-usecase-134
    container_name: n8n-usecase-134
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_134_data:/home/node/.n8n"]

volumes:
  n8n_usecase_134_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
