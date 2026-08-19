# 130 - Tax Document Collector

> **Category:** Finance & Accounting

Collects and organizes tax documents before deadlines. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Quarterly)"]
    B["Request Missing Docs"]
    C["Sort by Category"]
    D["IF: All received?"]
    E["Send Reminders"]
    F["Store Documents"]
    G["Notify Accountant"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Quarterly run |
| Email | Doc requests |
| IF | Completeness check |
| Google Drive | Sort files |
| Email | Reminder send |
| Slack | Accountant notify |

## Dockerfile

Dockerfile: [usecases/130-tax-document-collector/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/130-tax-document-collector/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `TAX_CRON=0 8 1 * *`

## Build & Run

```bash
cd usecases/130-tax-document-collector

# Build the image
docker build -t n8n-usecase-130 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-130 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-130

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-130:
    image: n8n-usecase-130
    container_name: n8n-usecase-130
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_130_data:/home/node/.n8n"]

volumes:
  n8n_usecase_130_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
