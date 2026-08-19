# 001 - Gmail Inbox Processor

> **Category:** Email & Communication

Processes incoming Gmail, classifies mail and logs every action to a spreadsheet. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Gmail Trigger (New Email)"]
    B["Read Email Body and Sender"]
    C["Classify with IF / Keywords"]
    D["IF: Important sender?"]
    E["Send Reply with Template"]
    F["Archive and Label Email"]
    G["Log to Google Sheets"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Gmail Trigger | Fires on new email |
| Gmail | Reads body and sender |
| IF | Classifies mail type |
| Gmail Send | Replies with template |
| Google Sheets | Logs every action |
| SQLite | Stores audit history |

## Dockerfile

Dockerfile: [usecases/01-gmail-inbox-processor/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/01-gmail-inbox-processor/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | `n8n-nodes-sqlite` |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `WEBHOOK_PATH=email-process`
- `POLL_MINUTES=15`

## Build & Run

```bash
cd usecases/01-gmail-inbox-processor

# Build the image
docker build -t n8n-usecase-001 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-001 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-001

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-001:
    image: n8n-usecase-001
    container_name: n8n-usecase-001
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_001_data:/home/node/.n8n"]

volumes:
  n8n_usecase_001_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
