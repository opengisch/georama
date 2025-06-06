---
tags:
  - Endpoints
  - WMS
  - WFS
  - QGIS
  - Docker
  - Workflow
  - Development
---

# 🌐 Georama Endpoints

This page documents the key endpoints provided by the Georama development setup. These are useful for development, testing, and integration with external tools such as QGIS Desktop.

---

## 🔐 Admin & Authentication

- **Admin Interface**  
  Access the Django admin panel to manage users, layers, permissions, and more.  
  ➜ [http://localhost:8080/admin/](http://localhost:8080/admin/)

- **User Login Page**  
  Interface for authenticating standard users (with third-party provider support if enabled).  
  ➜ [http://localhost:8080/login](http://localhost:8080/login)

---

## 🗺️ Web Map Service (WMS)

- **WMS Capabilities**  
  Retrieves the WMS 1.3.0 service capabilities (layer listing, supported formats, etc.).  
  ➜ [`GET` WMS Capabilities](http://localhost:8080/maps?service=WMS&request=GetCapabilities&version=1.3.0)

- **WMS Endpoint for QGIS Desktop**  
  Use this endpoint to connect QGIS to your local Georama WMS service.  
  ➜ `http://localhost:8080/maps`

---

## 📦 Web Feature Service (WFS / OGC API Features)

- **WFS Endpoint for QGIS Desktop**  
  Use this endpoint to access vector data (features) via the OGC API - Features standard (aka WFS 3).  
  ➜ `http://localhost:8080/features/`
  ➜ `http://localhost:8080/features/openapi`
  ➜ `http://localhost:8080/features/conformance`
  ➜ `http://localhost:8080/features/collections`

---

## 🐳 Notes on Docker-Based Development

All endpoints above assume you're running Georama locally using Docker on the default development port `8080`. If you've mapped ports differently or deployed to a remote host, adjust the URLs accordingly.

---

## ✅ Quick Test Checklist

- [ ] Can you log in via `/login`?
- [ ] Can you access `/admin/` as a superuser?
- [ ] Can QGIS successfully connect to both `/maps` and `/features`?
- [ ] Do layers appear in the WMS GetCapabilities response?

---

For additional setup instructions or troubleshooting, see the [Quickstart](quick_start.md).
