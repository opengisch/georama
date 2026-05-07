---
tags:
  - Setup
  - Local-setup
---

# 🗺️ Georama Local Setup Guide

⚠️ **About this guide**

This guide walks you through setting up Georama **locally on your own machine**, for the purpose of **testing and exploring the software**. It is intentionally simplified and aimed at people with no, or little, prior Docker experience.

**This is NOT a production deployment guide**. It uses development settings (debug mode on, default passwords, no HTTPS, no real authentication setup) that are completely inappropriate for a publicly accessible server. Do not use this setup to serve real users or sensitive data.

If you need to deploy Georama in a real environment, refer to the official documentation and use the production configuration instead.

It has been tested on Ubuntu 24.04 LTS.

## 🧱 PART 1: Install Docker (one-time setup)

Docker is like a "portable box" that runs software without you needing to install all its complicated dependencies manually. You only need to do this once.

Open a **Terminal** (`Ctrl+Alt+T`) and run these commands **one at a time**:

**1. Remove any old/broken Docker versions:**
```bash
sudo apt remove docker docker-engine docker.io containerd runc
```

**2. Install required tools:**
```bash
sudo apt update
sudo apt install -y ca-certificates curl gnupg
```

**3. Add Docker's official source:**
```bash
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

**4. Install Docker:**
```bash
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

**5. Allow your user to run Docker without `sudo` (important!):**
```bash
sudo usermod -aG docker $USER
```

**6. ⚠️ Log out and log back in** (or reboot) so the group change takes effect. Then verify it worked:
```bash
docker run hello-world
```
You should see a message saying "Hello from Docker!" — that means Docker is working. ✅

---

## 📦 PART 2: Get the Georama Code

> ⚠️ **Important:** The Georama repository is private. You need a GitHub account that has been granted access, and you need a **Personal Access Token** to authenticate — GitHub no longer accepts your regular password for Git operations.
>
> **To create a token:**
> 1. Go to https://github.com/settings/tokens/new
> 2. Give it any name (e.g. `georama-local`)
> 3. Set an expiration (or choose "No expiration")
> 4. Tick the **`repo`** scope
> 5. Click **"Generate token"** and **copy it immediately** — GitHub only shows it once!
>    It looks like `ghp_xxxxxxxxxxxxxxxxxxxx`
>
> When Git asks for your **password**, paste this token — not your GitHub password.

**7. Install Git (if not already installed):**
```bash
sudo apt install -y git
```

**8. Clone (download) the Georama repository:**
```bash
git clone https://github.com/opengisch/georama.git
cd georama
```
When prompted:
- **Username:** your GitHub username
- **Password:** paste your Personal Access Token

---

## ⚙️ PART 3: Configure Georama

**9. Create your personal settings file:**
```bash
cp .env.dev.example .env
```

**10. Create a folder where your QGIS projects will live:**
```bash
mkdir -p ~/georama-data
```

**11. Add the two required path variables to your `.env`.**

The first tells Docker which folder on your machine to share with the container. The second tells Django where to find that data inside the container (always `/io/data` — do not change this).

```bash
echo "GEORAMA_LOCAL_DATA=$HOME/georama-data" >> .env
sed -i "s|GEORAMA_DATA_INTEGRATION_ROOT=.*|GEORAMA_DATA_INTEGRATION_ROOT=/io/data|" .env
```

Verify both look correct:
```bash
grep -E "GEORAMA_LOCAL_DATA|GEORAMA_DATA_INTEGRATION_ROOT" .env
```

Expected output:
```
GEORAMA_DATA_INTEGRATION_ROOT=/io/data
GEORAMA_LOCAL_DATA=/home/yourname/georama-data
```
✅

---

## 🚀 PART 4: Start Georama

**12. Build the Docker containers** (this downloads everything needed — may take 5–15 minutes the first time):
```bash
docker compose build
```

**13. Start all services in the background:**
```bash
docker compose up -d
```

**14. Set up the database:**
```bash
docker compose exec georama make migrate
```

**15. Set the password for the admin account:**
```bash
docker compose exec georama make create-superuser
```
Georama automatically creates a user called **`admin`**. You will only be asked to type a password for it — choose something you'll remember!

**16. Load some example content:**
```bash
docker compose exec georama make create-example-content
```

**17. Open Georama in your browser:**

👉 **http://localhost:4242/admin/**

Log in with username **`admin`** and the password you just set. 🎉

---

## 🔄 PART 5: Updating to the Latest Version (do this anytime)

When you want to pull in the latest Georama code from GitHub:

```bash
# Navigate to your georama folder (if you're not already there)
cd ~/georama

# Stop the running services
docker compose down

# Pull the latest code from GitHub
git pull

# Rebuild the containers with the new code
docker compose build

# Start everything back up
docker compose up -d

# Apply any new database changes
docker compose exec georama make migrate
```

That's it — you're on the latest version. ✅

---

## 🛑 PART 6: Everyday Usage

| What you want to do | Command (run inside the `georama` folder) |
|---|---|
| Start Georama | `docker compose up -d` |
| Stop Georama | `docker compose down` |
| See if it's running | `docker compose ps` |
| View logs if something is wrong | `docker compose logs` |

---

## 🗂️ Quick Reference: Where things live

| Thing | Location |
|---|---|
| Georama source code | `~/georama/` |
| Your QGIS projects folder | `~/georama-data/` |
| Georama web interface | http://localhost:4242/ |
| Georama admin panel (Django) | http://localhost:4242/admin/ |
