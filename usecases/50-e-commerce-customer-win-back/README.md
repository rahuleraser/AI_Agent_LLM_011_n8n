# 050 - E-commerce Customer Win-back

> **Category:** E-commerce & Retail

Re-engages lapsed customers with targeted offers. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Weekly)"]
    B["Find Inactive Customers"]
    C["Segment by Spend"]
    D["IF: High value customer?"]
    E["Send VIP Offer"]
    F["Send Standard Offer"]
    G["Log Campaign"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Weekly scan |
| SQLite | Customer data |
| Code | Segmentation |
| IF | Value branch |
| Email | Offer sends |
| Spreadsheet | Campaign log |

## Dockerfile

Dockerfile: [usecases/50-e-commerce-customer-win-back/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/50-e-commerce-customer-win-back/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `WINBACK_CRON=0 10 * * 1`
- `INACTIVE_DAYS=90`

## Build & Run

```bash
cd usecases/50-e-commerce-customer-win-back

# Build the image
docker build -t n8n-usecase-050 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-050 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-050

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-050:
    image: n8n-usecase-050
    container_name: n8n-usecase-050
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_050_data:/home/node/.n8n"]

volumes:
  n8n_usecase_050_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
