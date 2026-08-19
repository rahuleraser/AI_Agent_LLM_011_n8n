# 017 - Twitter Thread Publisher

> **Category:** Social Media & Marketing

Publishes a multi-tweet thread from a spreadsheet of tweets. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Spreadsheet Trigger (Thread)"]
    B["Load Tweets in Order"]
    C["Publish Tweet Sequentially"]
    D["IF: Validate each tweet?"]
    E["Flag Invalid Tweet"]
    F["Wait Between Tweets"]
    G["Log Published Thread"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Spreadsheet File | Tweet list |
| Code | Validates tweets |
| Twitter | Publishes tweet |
| Wait | Spacing delay |
| IF | Validation branch |
| Spreadsheet | Publish log |

## Dockerfile

Dockerfile: [usecases/17-twitter-thread-publisher/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/17-twitter-thread-publisher/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `THREAD_WAIT_SECONDS=30`
- `TWEET_LIMIT_CHARS=280`

## Build & Run

```bash
cd usecases/17-twitter-thread-publisher

# Build the image
docker build -t n8n-usecase-017 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-017 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-017

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-017:
    image: n8n-usecase-017
    container_name: n8n-usecase-017
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_017_data:/home/node/.n8n"]

volumes:
  n8n_usecase_017_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
