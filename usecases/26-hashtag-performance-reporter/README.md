# 026 - Hashtag Performance Reporter

> **Category:** Social Media & Marketing

Reports which hashtags drive the most engagement per week. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Weekly)"]
    B["Collect Post Metrics"]
    C["Group by Hashtag"]
    D["IF: Metric improved?"]
    E["Add to Winner List"]
    F["Keep in Watch List"]
    G["Email Performance Report"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Weekly run |
| HTTP Request | Post metrics |
| Code | Groups hashtags |
| IF | Improvement check |
| Email | Sends report |
| Google Sheets | Trend data |

## Dockerfile

Dockerfile: [usecases/26-hashtag-performance-reporter/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/26-hashtag-performance-reporter/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `HASHTAG_CRON=0 9 * * 1`
- `TRACKED_HASHTAGS=#brand,#launch`

## Build & Run

```bash
cd usecases/26-hashtag-performance-reporter

# Build the image
docker build -t n8n-usecase-026 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-026 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-026

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-026:
    image: n8n-usecase-026
    container_name: n8n-usecase-026
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_026_data:/home/node/.n8n"]

volumes:
  n8n_usecase_026_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
