# 006 - Cold Email Outreach

> **Category:** Email & Communication

Sends a personalized cold outreach sequence to a lead list with follow-ups. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Spreadsheet Trigger (Lead List)"]
    B["Format Personalized Email"]
    C["Wait N Days"]
    D["IF: Got a reply?"]
    E["Stop Sequence"]
    F["Send Follow-up"]
    G["Mark Status in Sheet"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Spreadsheet File | Reads leads |
| Email Send | Sends first email |
| Wait | Adds delay |
| Gmail | Checks replies |
| IF | Branches sequence |
| Spreadsheet | Tracks status |

## Dockerfile

Dockerfile: [usecases/06-cold-email-outreach/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/06-cold-email-outreach/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `OUTREACH_STEP_WAIT_DAYS=3`
- `MAX_FOLLOWUPS=3`

## Build & Run

```bash
cd usecases/06-cold-email-outreach

# Build the image
docker build -t n8n-usecase-006 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-006 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-006

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-006:
    image: n8n-usecase-006
    container_name: n8n-usecase-006
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_006_data:/home/node/.n8n"]

volumes:
  n8n_usecase_006_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
