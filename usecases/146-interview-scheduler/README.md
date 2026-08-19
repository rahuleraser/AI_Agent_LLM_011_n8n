# 146 - Interview Scheduler

> **Category:** HR & Internal Ops

Coordinates interview slots between candidates and panels. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Webhook (Interview)"]
    B["Fetch Candidate Availability"]
    C["Book Interview"]
    D["IF: Panel free?"]
    E["Suggest Alternatives"]
    F["Send Invite"]
    G["Log Scheduling"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Webhook | Interview request |
| Google Calendar | Availability |
| IF | Slot check |
| Zoom | Create meeting |
| Email | Invite send |
| Google Sheets | Schedule log |

## Dockerfile

Dockerfile: [usecases/146-interview-scheduler/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/146-interview-scheduler/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | `n8n-nodes-zoom` |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `INTERVIEW_WEBHOOK_PATH=interview`

## Build & Run

```bash
cd usecases/146-interview-scheduler

# Build the image
docker build -t n8n-usecase-146 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-146 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-146

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-146:
    image: n8n-usecase-146
    container_name: n8n-usecase-146
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_146_data:/home/node/.n8n"]

volumes:
  n8n_usecase_146_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
