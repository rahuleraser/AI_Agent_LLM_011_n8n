# 090 - File Format Converter

> **Category:** Data & Database

Converts files between formats (CSV, JSON, XML, Excel). Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (File)"]
    B["Detect Input Format"]
    C["Transform to Target"]
    D["IF: Conversion ok?"]
    E["Save Converted File"]
    F["Return Error"]
    G["Log Conversion"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | File upload |
| Code | Format detect |
| Code | Transform |
| IF | Success check |
| Google Drive | Save file |
| SQLite | Conversion log |

## Dockerfile

Dockerfile: [usecases/90-file-format-converter/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/90-file-format-converter/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `CONVERT_WEBHOOK_PATH=convert`

## Build & Run

```bash
cd usecases/90-file-format-converter

# Build the image
docker build -t n8n-usecase-090 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-090 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-090

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-090:
    image: n8n-usecase-090
    container_name: n8n-usecase-090
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_090_data:/home/node/.n8n"]

volumes:
  n8n_usecase_090_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
