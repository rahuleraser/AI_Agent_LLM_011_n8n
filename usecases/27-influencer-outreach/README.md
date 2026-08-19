# 027 - Influencer Outreach

> **Category:** Social Media & Marketing

Automates influencer outreach and tracks campaign responses. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Spreadsheet Trigger (Influencers)"]
    B["Personalize Outreach DM"]
    C["Add to Campaign"]
    D["IF: Reply received?"]
    E["Send Follow-up"]
    F["Update Status"]
    G["Notify Campaign Manager"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Spreadsheet File | Influencer list |
| Email/DM | Outreach |
| IF | Reply detection |
| Spreadsheet | Status update |
| Slack | Campaign alert |
| Code | Personalization |

## Dockerfile

Dockerfile: [usecases/27-influencer-outreach/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/27-influencer-outreach/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `INFLUENCER_WAIT_DAYS=2`
- `CAMPAIGN_ID=your-campaign`

## Build & Run

```bash
cd usecases/27-influencer-outreach

# Build the image
docker build -t n8n-usecase-027 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-027 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-027

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-027:
    image: n8n-usecase-027
    container_name: n8n-usecase-027
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_027_data:/home/node/.n8n"]

volumes:
  n8n_usecase_027_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
