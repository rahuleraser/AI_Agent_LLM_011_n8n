# 068 - Jira Issue Creator

> **Category:** Support & Customer Service

Creates Jira issues automatically from support requests. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Email / Support Trigger"]
    B["Parse Issue Details"]
    C["Link Existing Issue"]
    D["IF: Duplicate issue?"]
    E["Create Jira Issue"]
    F["Assign to Team"]
    G["Notify Reporter"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Email Trigger | Support mail |
| Code | Issue parsing |
| IF | Duplicate check |
| Jira | Create issue |
| Jira | Assignment |
| Email | Reporter notify |

## Dockerfile

Dockerfile: [usecases/68-jira-issue-creator/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/68-jira-issue-creator/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `JIRA_WEBHOOK_PATH=jira-create`

## Build & Run

```bash
cd usecases/68-jira-issue-creator

# Build the image
docker build -t n8n-usecase-068 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-068 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-068

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-068:
    image: n8n-usecase-068
    container_name: n8n-usecase-068
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_068_data:/home/node/.n8n"]

volumes:
  n8n_usecase_068_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
