# 101 - SSL Certificate Expiry Alert

> **Category:** Developer & DevOps

Warns before SSL certificates expire. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["Cron Trigger (Daily)"]
    B["Check Cert Expiry"]
    C["Send Expiry Alert"]
    D["IF: < 14 days?"]
    E["Log Cert Status"]
    F["Update Cert Tracker"]
    G["Notify Ops Team"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| Cron Trigger | Daily check |
| Code | Cert fetch |
| IF | Expiry window |
| Email | Expiry alert |
| Google Sheets | Cert tracker |
| Slack | Ops notify |

## Dockerfile

Dockerfile: [usecases/101-ssl-certificate-expiry-alert/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/101-ssl-certificate-expiry-alert/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `SSL_CRON=0 9 * * *`
- `CERT_WARN_DAYS=14`
- `DOMAIN_LIST=example.com`

## Build & Run

```bash
cd usecases/101-ssl-certificate-expiry-alert

# Build the image
docker build -t n8n-usecase-101 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-101 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-101

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-101:
    image: n8n-usecase-101
    container_name: n8n-usecase-101
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_101_data:/home/node/.n8n"]

volumes:
  n8n_usecase_101_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
