# Georama

<div align="center">
  <br>
  <img width="150" height="136" alt="georama_logo" src="https://github.com/user-attachments/assets/abcf1b27-c221-454b-a526-ed086d9a38b8" />
  <br>
</div>

**The open, interoperable platform for any geospatial data publication workflows, from complex enterprise workflows down to anyone sharing their first dataset.**

Georama is an open-source project by [OPENGIS.ch](https://opengis.ch), the team behind [QField](https://qfield.org), [QFieldCloud](https://qfield.cloud), and other open geospatial tools.

## What is Georama?

Georama bridges the gap between desktop GIS and the web. It lets you take your QGIS projects and publish them as standards-compliant web services, complete with metadata management, fine-grained access control, and, thanks to its native integration with [GeoGirafe](https://geogirafe.org/), a modern web map interface.

Whether you are a small organization sharing a handful of datasets, or a large institution managing hundreds of projects and complex publication workflows, Georama is designed to scale with you.

## Core features

- **QGIS-native workflow:** import and manage QGIS projects directly, keeping your existing data and styling intact
- **WMS publishing:** serve your layers as OGC-compliant WMS 1.3.0 services via [qgis-server-light](https://github.com/opengisch/qgis-server-light)
- **OGC API Features (WFS 3):** share vector data using modern open standards, powered by [pygeoapi](https://github.com/geopython/pygeoapi)
- **Metadata management:** maintain flexible, extensible metadata for your layers and datasets
- **Fine-grained permissions:** control who can see, edit, and publish what, down to the attribute level
- **Identity provider integration:** connect to external authentication providers (OAuth, SAML, LDAP) via standard Django apps
- **Modern web map interface:** end users explore your data through [GeoGirafe](https://gitlab.com/geogirafe/gg-viewer), a clean and accessible WebGIS frontend

## How it works

Georama is a modular suite of [Django](https://www.djangoproject.com) apps. At its core, it connects four components:

- [**QGIS**](https://qgis.org/) as the data integration and styling engine
- [**Django**](https://www.djangoproject.com/) as the application and permission layer
- [**pygeoapi**](https://github.com/geopython/pygeoapi) and [**qgis-server-light**](https://github.com/opengisch/qgis-server-light) as the standards-based service backends
- [**GeoGirafe**](https://gitlab.com/geogirafe/gg-viewer) as the frontend WebGIS

This architecture keeps each component focused and isolated, and is designed with a future plugin and extension system in mind.

## Getting started

The full documentation, including setup guides, configuration references, and API docs, is available at [docs.georama.io](https://docs.georama.io).

### Quickstart with Docker Compose

Copy the example environment file and adjust it to your needs:

```shell
cp .env.dev.example .env
```

Build Georama:

```shell
docker compose build georama
```

Start all services:

```shell
docker compose up -d
```

Once the services are up, initialize the Django database:

```shell
docker compose exec georama make migrate
docker compose exec georama make create-superuser
docker compose exec georama make create-example-content
```

The admin interface is available at [http://localhost:4242/admin/](http://localhost:4242/admin/) (user: `admin`, password: as chosen during setup).

## Contributing

We welcome contributions of all kinds: bug reports, feature ideas, documentation improvements, and pull requests.

Before investing time in a new feature or fix, please get in touch first, either by [opening an issue](https://github.com/opengisch/georama/issues) or starting a conversation in our [Discussions space](https://github.com/opengisch/georama/discussions). This helps us align early and makes sure your effort has the best chance of being merged.

See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines.

## About OPENGIS.ch

Georama is built and maintained by [OPENGIS.ch](https://opengis.ch), a Swiss company specializing in open-source geospatial software. We are also the team behind [QField](https://qfield.org) and [QFieldCloud](https://qfield.cloud). We believe open standards and open software are the foundation of a healthy geospatial ecosystem.

<div align="center">
  <a href="https://opengis.ch">
    <img width="413" height="162" alt="logo_opengisch_open-source-geoninjas" src="https://github.com/user-attachments/assets/ebdb2d99-48a4-418d-8822-a17ac6f1365b" />
  </a>
</div>

