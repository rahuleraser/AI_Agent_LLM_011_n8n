# 148 - Reference Check Requester

> **Category:** HR & Internal Ops

Requests and tracks reference checks for final candidates. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["HR Trigger (Candidate)"]
    B["Fetch Reference Contacts"]
    C["Send Reference Form"]
    D["IF: All received?"]
    E["Update Candidate Record"]
    F["Send Reminder"]
    G["Notify HR"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| HR Trigger | Final candidate |
| Email | Form send |
| Wait | Response window |
| IF | Completeness check |
| Google Sheets | Candidate record |
| Slack | HR notify |

## Dockerfile

Dockerfile: [usecases/148-reference-check-requester/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/148-reference-check-requester/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `REFERENCE_WEBHOOK_PATH=reference`

## Build & Run

```bash
cd usecases/148-reference-check-requester

# Build the image
docker build -t n8n-usecase-148 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-148 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-148

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-148:
    image: n8n-usecase-148
    container_name: n8n-usecase-148
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_148_data:/home/node/.n8n"]

volumes:
  n8n_usecase_148_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
