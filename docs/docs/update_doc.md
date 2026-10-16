---
icon: lucide/book-open
---

# Update the Documentation

This documentation is built with [Zensical](https://zensical.org/), a static site generator
written by the team behind Material for MkDocs. Pages are written in Markdown.

## Where Things Are

| Path                                   | Content                                                     |
| -------------------------------------- | ----------------------------------------------------------- |
| `docs/zensical.toml`                   | Site configuration: navigation, theme, Markdown extensions. |
| `docs/docs/`                           | The Markdown pages, plus assets and stylesheets.            |
| `docs/site/`                           | The generated site. Ignored by git.                         |
| `.github/workflows/docs.yml`           | The workflow that builds and deploys the site.              |

When you add a page, also add it to the `nav` list in `docs/zensical.toml`, or it will not
appear in the navigation.

## Preview Locally

Zensical is declared in the `docs` dependency group of `pyproject.toml`. You only need
[uv](https://docs.astral.sh/uv/) on your machine, no Docker. Run the commands from the `docs/`
folder:

```bash
cd docs

# Serve the site on http://localhost:8000, with live reload
uv run --frozen --only-group docs zensical serve

# Build the static site into docs/site/
uv run --frozen --only-group docs zensical build
```

`--only-group docs` installs Zensical alone, without Georama and its dependencies (GDAL,
QGIS-Server-Light…), which are only available in the Docker image. `--frozen` uses the version
pinned in `uv.lock`.

!!! tip "Port already in use"

    If port 8000 is taken, choose another one with `--dev-addr localhost:8001`.

## Deployment

The site is deployed automatically to GitHub Pages: the `Documentation` workflow
(`.github/workflows/docs.yml`) builds it and publishes it on each push to the `zensical-doc`
branch. It runs the same `zensical build` command as above, with the Zensical version pinned in
`uv.lock`, so the deployed site matches your local preview. There is nothing to do by hand; check the workflow run in the **Actions** tab of the
repository if your changes do not show up.
