# 035 - Social Profile Health Check

> **Category:** Social Media & Marketing

Checks all social profiles for issues like broken links or missing info. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Monthly)"]
    B["Fetch Profile Fields"]
    C["Validate Against Checklist"]
    D["IF: Issue found?"]
    E["Create Fix Task"]
    F["Mark Healthy"]
    G["Email Health Report"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Monthly scan |
| HTTP Request | Profile data |
| Code | Checklist checks |
| IF | Issue detection |
| Google Sheets | Fix tasks |
| Email | Health report |

## Dockerfile

Dockerfile: [usecases/35-social-profile-health-check/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/35-social-profile-health-check/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `PROFILE_CRON=0 9 1 * *`
- `CHECKLIST_URL=sheet-link`

## Build & Run

```bash
cd usecases/35-social-profile-health-check

# Build the image
docker build -t n8n-usecase-035 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-035 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-035

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-035:
    image: n8n-usecase-035
    container_name: n8n-usecase-035
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_035_data:/home/node/.n8n"]

volumes:
  n8n_usecase_035_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
