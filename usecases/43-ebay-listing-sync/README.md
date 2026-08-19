# 043 - eBay Listing Sync

> **Category:** E-commerce & Retail

Syncs eBay listings with inventory counts in real time. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["eBay Trigger (Listing)"]
    B["Fetch Listing Data"]
    C["Update Inventory"]
    D["IF: Quantity changed?"]
    E["Log Listing"]
    F["Alert Low Quantity"]
    G["Sync to Sheet"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| eBay Trigger | Listing event |
| eBay API | Listing data |
| IF | Quantity check |
| SQLite | Inventory store |
| Google Sheets | Sync log |
| Slack | Low stock alert |

## Dockerfile

Dockerfile: [usecases/43-ebay-listing-sync/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/43-ebay-listing-sync/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `EBAY_WEBHOOK_PATH=ebay-sync`

## Build & Run

```bash
cd usecases/43-ebay-listing-sync

# Build the image
docker build -t n8n-usecase-043 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-043 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-043

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-043:
    image: n8n-usecase-043
    container_name: n8n-usecase-043
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_043_data:/home/node/.n8n"]

volumes:
  n8n_usecase_043_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
