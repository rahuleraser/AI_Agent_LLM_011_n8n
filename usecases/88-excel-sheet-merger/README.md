# 088 - Excel Sheet Merger

> **Category:** Data & Database

Merges multiple Excel files into a single workbook. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["File Trigger (Excel)"]
    B["Read All Sheets"]
    C["Merge Rows"]
    D["IF: Headers match?"]
    E["Flag Mismatch"]
    F["Save Merged File"]
    G["Notify Owner"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| File Trigger | New files |
| Spreadsheet File | Read sheets |
| Code | Header check |
| IF | Merge branch |
| Spreadsheet File | Save merged |
| Email | Owner notify |

## Dockerfile

Dockerfile: [usecases/88-excel-sheet-merger/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/88-excel-sheet-merger/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `MERGE_WEBHOOK_PATH=merge-excel`

## Build & Run

```bash
cd usecases/88-excel-sheet-merger

# Build the image
docker build -t n8n-usecase-088 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-088 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-088

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-088:
    image: n8n-usecase-088
    container_name: n8n-usecase-088
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_088_data:/home/node/.n8n"]

volumes:
  n8n_usecase_088_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
