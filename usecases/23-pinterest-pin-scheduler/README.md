# 023 - Pinterest Pin Scheduler

> **Category:** Social Media & Marketing

Schedules pins from a content board to Pinterest. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Spreadsheet Trigger (Pins)"]
    B["Fetch Pin Image and Link"]
    C["Build Pin Metadata"]
    D["IF: Valid image?"]
    E["Schedule Pin"]
    F["Flag Broken Image"]
    G["Log Pin Status"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Spreadsheet File | Pin list |
| Code | Prepares pin |
| Pinterest | Creates pin |
| IF | Image validation |
| Spreadsheet | Pin status |
| Code | Metadata build |

## Dockerfile

Dockerfile: [usecases/23-pinterest-pin-scheduler/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/23-pinterest-pin-scheduler/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `PINTEREST_WEBHOOK_PATH=pin-schedule`

## Build & Run

```bash
cd usecases/23-pinterest-pin-scheduler

# Build the image
docker build -t n8n-usecase-023 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-023 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-023

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-023:
    image: n8n-usecase-023
    container_name: n8n-usecase-023
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_023_data:/home/node/.n8n"]

volumes:
  n8n_usecase_023_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
