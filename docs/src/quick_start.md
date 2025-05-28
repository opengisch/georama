---
tags:
  - Setup
  - Quick-start
---

# ⚡ Quick-start Guide

Set up **Georama** locally using Docker with minimal effort.

📘 **Also see:**  
<a href="https://github.com/opengisch/georama?tab=readme-ov-file#quickstart" target="_blank">
Official README.md</a>

---

## 🐳 Quickstart with Docker Compose

### ✅ Prerequisites

Make sure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/)

---

### 📦 Clone the Repository

```bash
git clone git@github.com:opengisch/georama.git
cd georama
```

### ⚙️ Environment Configuration
Copy the example environment file and customize it:

```bash
cp .env.example .env
```

Set the path to your QGIS projects:

```bash
GEORAMA_LOCAL_DATA=/absolute/path/to/your/qgis/projects
```
Optionally, adjust other variables in the .env file to match your environment.

### 🚀 Start the Services
Build and launch all containers:

```bash
docker compose build
docker compose up -d
```
⏳ Note: The first run downloads ~5GB of test data. Be patient.

### 🗃️ Prepare the Django Database
Once services are running, apply migrations and create a superuser:

```bash
docker compose exec georama make migrate
docker compose exec georama make create-superuser
```

### 🔐 Access the Admin Interface
Admin panel: http://localhost:8080/admin/
Login with the superuser credentials you chose.

### ➡️ Next Steps
Explore the recommended Workflow Guide to import data, publish services, and manage metadata.
See the [Workflow](workflow.md)

