# 093 - GitHub Release Tracker

> **Category:** Developer & DevOps

Watches GitHub releases and announces them. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["GitHub Trigger (Release)"]
    B["Fetch Release Notes"]
    C["Skip Announce"]
    D["IF: Pre-release?"]
    E["Post Release Announcement"]
    F["Send Changelog Digest"]
    G["Log Releases"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| GitHub Trigger | New release |
| GitHub | Release data |
| IF | Pre-release check |
| Discord | Announce post |
| Email | Changelog |
| SQLite | Release log |

## Dockerfile

Dockerfile: [usecases/93-github-release-tracker/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/93-github-release-tracker/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | `n8n-nodes-github`, `n8n-nodes-discord` |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `RELEASE_WEBHOOK_PATH=release`

## Build & Run

```bash
cd usecases/93-github-release-tracker

# Build the image
docker build -t n8n-usecase-093 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-093 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-093

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-093:
    image: n8n-usecase-093
    container_name: n8n-usecase-093
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_093_data:/home/node/.n8n"]

volumes:
  n8n_usecase_093_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
