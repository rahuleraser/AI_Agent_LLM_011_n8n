# 147 - Candidate Screening

> **Category:** HR & Internal Ops

Screens job applicants by matching skills to requirements. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["HR Trigger (Application)"]
    B["Parse Candidate Resume"]
    C["Move to Shortlist"]
    D["IF: Skills match?"]
    E["Send Rejection"]
    F["Update Pipeline"]
    G["Notify Recruiter"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| HR Trigger | Application |
| AI LLM | Resume parse |
| IF | Match check |
| Google Sheets | Pipeline update |
| Email | Rejection send |
| Slack | Recruiter notify |

## Dockerfile

Dockerfile: [usecases/147-candidate-screening/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/147-candidate-screening/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `SCREEN_WEBHOOK_PATH=screen`

## Build & Run

```bash
cd usecases/147-candidate-screening

# Build the image
docker build -t n8n-usecase-147 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-147 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-147

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-147:
    image: n8n-usecase-147
    container_name: n8n-usecase-147
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_147_data:/home/node/.n8n"]

volumes:
  n8n_usecase_147_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
