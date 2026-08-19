# 144 - Timesheet Validator

> **Category:** HR & Internal Ops

Validates submitted timesheets and flags issues. Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

```mermaid
flowchart TD
    A["HR Trigger (Timesheet)"]
    B["Check Hours Entries"]
    C["Flag Overtime"]
    D["IF: Over 40 hours?"]
    E["Validate Entries"]
    F["Update Payroll Sheet"]
    G["Notify Employee"]
    A --> B --> C --> D
    D -- "Yes" --> E --> G
    D -- "No" --> F --> G
```

## Key Nodes

| Node | Purpose |
|------|---------|
| HR Trigger | Timesheet submit |
| Code | Hours check |
| IF | Overtime flag |
| Google Sheets | Payroll update |
| Email | Employee notify |
| SQLite | Validation log |

## Dockerfile

Dockerfile: [usecases/144-timesheet-validator/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/144-timesheet-validator/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | None (built-in nodes) |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

- `TIMESHEET_WEBHOOK_PATH=timesheet`

## Build & Run

```bash
cd usecases/144-timesheet-validator

# Build the image
docker build -t n8n-usecase-144 .

# Run on Docker Desktop
docker run -d --name n8n-usecase-144 -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n n8n-usecase-144

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-144:
    image: n8n-usecase-144
    container_name: n8n-usecase-144
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_144_data:/home/node/.n8n"]

volumes:
  n8n_usecase_144_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
