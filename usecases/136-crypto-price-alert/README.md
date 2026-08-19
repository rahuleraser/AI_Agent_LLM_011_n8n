# 136 - Crypto Price Alert

> **Category:** Finance & Accounting

Sends alerts when crypto prices cross thresholds. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (5 min)"]
    B["Fetch Coin Price"]
    C["Send Buy / Sell Alert"]
    D["IF: Above / below?"]
    E["Log Price"]
    F["Update Alerts Board"]
    G["Notify Trader"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Price poll |
| HTTP Request | Coin API |
| IF | Threshold check |
| Telegram | Alert send |
| Google Sheets | Alerts board |
| SQLite | Price log |

## Dockerfile

Dockerfile: [usecases/136-crypto-price-alert/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/136-crypto-price-alert/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `CRYPTO_ALERT_CRON=*/5 * * * *`
- `PRICE_HIGH=60000`

## Build & Run

```bash
cd usecases/136-crypto-price-alert

# Build the image
docker build -t n8n-usecase-136 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-136 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-136

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-136:
    image: n8n-usecase-136
    container_name: n8n-usecase-136
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_136_data:/home/node/.n8n"]

volumes:
  n8n_usecase_136_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
