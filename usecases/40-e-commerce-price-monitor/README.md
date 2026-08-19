# 040 - E-commerce Price Monitor

> **Category:** E-commerce & Retail

Monitors competitor prices and alerts when thresholds are crossed. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Daily)"]
    B["Scrape Product Pages"]
    C["Extract Prices"]
    D["IF: Price below target?"]
    E["Alert Pricing Team"]
    F["Store Price"]
    G["Update Price Tracker"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Daily scrape |
| HTTP Request | Product pages |
| Code | Extracts price |
| IF | Threshold check |
| Slack | Pricing alert |
| Google Sheets | Price tracker |

## Dockerfile

Dockerfile: [usecases/40-e-commerce-price-monitor/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/40-e-commerce-price-monitor/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `PRICE_CRON=0 7 * * *`
- `PRICE_TARGET=49.99`

## Build & Run

```bash
cd usecases/40-e-commerce-price-monitor

# Build the image
docker build -t n8n-usecase-040 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-040 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-040

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-040:
    image: n8n-usecase-040
    container_name: n8n-usecase-040
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_040_data:/home/node/.n8n"]

volumes:
  n8n_usecase_040_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
