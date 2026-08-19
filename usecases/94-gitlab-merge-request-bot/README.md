# 094 - GitLab Merge Request Bot

> **Category:** Developer & DevOps

Automates GitLab merge request notifications and approvals. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["GitLab Trigger (MR)"]
    B["Fetch MR Info"]
    C["Request Approval"]
    D["IF: Pipeline passing?"]
    E["Flag Pipeline Failure"]
    F["Post Comment"]
    G["Notify Reviewers"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| GitLab Trigger | MR event |
| GitLab | MR details |
| IF | Pipeline check |
| GitLab | Approval request |
| GitLab | Comment post |
| Slack | Reviewer notify |

## Dockerfile

Dockerfile: [usecases/94-gitlab-merge-request-bot/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/94-gitlab-merge-request-bot/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `GITLAB_WEBHOOK_PATH=mr-event`

## Build & Run

```bash
cd usecases/94-gitlab-merge-request-bot

# Build the image
docker build -t n8n-usecase-094 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-094 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-094

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-094:
    image: n8n-usecase-094
    container_name: n8n-usecase-094
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_094_data:/home/node/.n8n"]

volumes:
  n8n_usecase_094_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
