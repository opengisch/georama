---
tags:
  - Setup
  - Development
---

# 🛠️ Development Guide

These pages outline how to develop and run **Georama** either inside a Docker container or directly on your
local machine.

Georama is a service encapsulating a number of different internal services. However, it relies on external
services too. Those are:

- **PostGIS Database**: For management of Georama (users, groups, layers, configuration, etc.)
- **QGIS-Server-Light**: The worker(s) which are processing the jobs
- **Redis**: Is used as the queue system between QGIS-Server-Light and Georama

Each approach described in the following subsections has to provide theses as a minimum.

!!! success
    After succeeding with one of the suggested solutions head to the [Workflow](../workflow.md)
