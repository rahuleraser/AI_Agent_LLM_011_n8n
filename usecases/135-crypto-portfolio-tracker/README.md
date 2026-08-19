# 135 - Crypto Portfolio Tracker

> **Category:** Finance & Accounting

Tracks crypto portfolio value and daily changes. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Hourly)"]
    B["Fetch Coin Prices"]
    C["Compute Portfolio Value"]
    D["IF: Change > 5%?"]
    E["Send Change Alert"]
    F["Update Tracker"]
    G["Log Snapshot"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Price poll |
| HTTP Request | Coin API |
| Code | Value compute |
| IF | Change threshold |
| Google Sheets | Portfolio tracker |
| Email | Change alert |

## Dockerfile

Dockerfile: [usecases/135-crypto-portfolio-tracker/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/135-crypto-portfolio-tracker/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `CRYPTO_CRON=0 * * * *`
- `COINS=BTC,ETH`
- `ALERT_PCT=5`

## Build & Run

```bash
cd usecases/135-crypto-portfolio-tracker

# Build the image
docker build -t n8n-usecase-135 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-135 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-135

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-135:
    image: n8n-usecase-135
    container_name: n8n-usecase-135
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_135_data:/home/node/.n8n"]

volumes:
  n8n_usecase_135_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
