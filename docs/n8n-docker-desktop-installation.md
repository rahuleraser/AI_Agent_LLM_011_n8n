# n8n on Docker Desktop — Lifetime-Free Step-by-Step Installation

This guide installs **n8n** (self-hosted workflow automation) on **Docker Desktop**
for **free, forever**, using only your local machine's resources.

> **Why is it lifetime free?**
> - n8n is open source (Sustainable Use License) — self-hosting and running your
>   own workflows is free with no user limits, workflow limits or time limits.
> - Everything runs on **your** machine inside Docker Desktop — no server rental.
> - All data stays in local Docker volumes — no hidden cloud storage charges.
> - The community edition includes unlimited workflows, executions and the full
>   node library of 400+ integrations.

---

## Prerequisites

| Requirement | Detail |
|-------------|--------|
| Docker Desktop | Windows 10/11 Pro/Home or macOS (Intel/Apple Silicon). Linux users can use Docker Engine. |
| RAM          | 4 GB free RAM recommended (8 GB ideal). n8n itself is lightweight. |
| Disk space   | ~1.5 GB for images + your workflow volume. |
| Free time    | ~10 minutes. |

### Install Docker Desktop (if you do not have it)

1. Download from https://www.docker.com/products/docker-desktop/
2. Run the installer and accept defaults.
3. On Windows, ensure **WSL 2 backend** is enabled during install.
4. On macOS, allow Docker Desktop to use your local HyperKit/Virtualization framework.
5. Launch **Docker Desktop** and wait until the whale icon shows **"Engine running"**.

Verify:

```bash
docker --version
docker compose version
```

---

## Step 1 — Get the n8n image

```bash
docker pull n8nio/n8n:latest
```

---

## Step 2 — Run n8n with a persistent volume (recommended)

```bash
mkdir -p ~/.n8n

docker run -d \
  --name n8n \
  --restart unless-stopped \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  -e N8N_ENCRYPTION_KEY="$(openssl rand -hex 32)" \
  n8nio/n8n:latest
```

| Flag | Meaning |
|------|---------|
| `-d` | Run detached in background |
| `--name n8n` | Container name |
| `--restart unless-stopped` | Auto-restart with Docker Desktop |
| `-p 5678:5678` | Expose editor on http://localhost:5678 |
| `-v ~/.n8n:/home/node/.n8n` | Persist workflows & credentials on your disk |
| `-e N8N_ENCRYPTION_KEY` | Stable secret so credentials survive restarts |

---

## Step 3 — Open the editor

1. Open a browser: **http://localhost:5678**
2. Create your free local owner account (stored only on your machine).
3. You are in. Build unlimited workflows.

---

## Step 4 — (Recommended) Upgrade to PostgreSQL backend

SQLite is fine to start. For heavy usage, switch to Postgres so your data stays
safe even if you rebuild the n8n container:

```bash
cd docker

cp .env.example .env
# edit .env and set a strong N8N_ENCRYPTION_KEY

docker compose up -d
```

Open **http://localhost:5678** again — now backed by Postgres.

---

## Step 5 — Build the base image from this repo (optional)

```bash
docker build -f docker/base/Dockerfile.n8n -t n8n-base:latest docker/base

docker run -d \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8n-base:latest
```

---

## Using a use-case image

Every use case in `usecases/` builds its own image, e.g.:

```bash
cd usecases/10-ai-llm-chatbot
docker build -t n8n-ai-chatbot .

docker run -d --name n8n-ai \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8n-ai-chatbot
```

---

## Common operations

```bash
# View logs
docker logs -f n8n

# Stop n8n (data is preserved)
docker stop n8n

# Start again
docker start n8n

# Reset everything (data volume is deleted)
docker rm -f n8n
docker volume rm n8n_data

# Pull latest n8n update
docker pull n8nio/n8n:latest
docker stop n8n && docker rm n8n
# re-run Step 2
```

---

## Security checklist for local use

- Enable basic auth in `docker/.env`:
  `N8N_BASIC_AUTH_ACTIVE=true`, set your own user/password.
- Set a **unique** `N8N_ENCRYPTION_KEY` before your first workflow.
- Do not expose port 5678 to the public internet without a reverse proxy + HTTPS.
- Backup `~/.n8n` (or the `n8n_data` volume) regularly.

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `localhost:5678` refuses connection | Wait 10-20s for startup; run `docker logs n8n`; check port conflict with `docker ps`. |
| Port 5678 already in use | Change the host port: `-p 5679:5678`. |
| Credentials lost after restart | You did not set `N8N_ENCRYPTION_KEY`. Re-set it and restore the volume. |
| Low memory errors | Give Docker Desktop more RAM (Settings > Resources). |
| WSL2 not found (Windows) | `wsl --install` in PowerShell, then restart. |

---

## "Lifetime Free" summary

| Cost item | Free? | Why |
|-----------|-------|-----|
| n8n software | YES | Open-source community edition |
| Number of workflows | YES | Unlimited |
| Number of executions | YES | Unlimited |
| Node library (400+) | YES | Included |
| Scheduler / webhooks | YES | Included |
| Server hosting | YES | Uses your local machine |
| Team members | YES | Community edition has no seat limits |

**Total recurring cost: $0**
