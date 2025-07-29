---
tags:
  - Setup
  - Development
---



6. Create example content::
Create example content (like demo users):

```shell
make create-example-content
```

## 🔃🛠️ Update QGIS Server light lib

[qgis-server-light](https://github.com/opengisch/qgis-server-light) interface is part of georama.

It is currently installed directly from github. You may want to use an updated version in your setup
while coding.

To force reinstall GitHub dep qgis_server_light **docker compose**:
```shell
docker compose exec georama bash -c '/opt/georama/venv/bin/pip install --force-reinstall --no-deps "git+ssh://git@github.com/opengisch/qgis-server-light.git@master#qgis_server_light"'
```

To force reinstall GitHub dep qgis_server_light **locally**:
```shell
.venv/bin/pip install --force-reinstall --no-deps "git+ssh://git@github.com/opengisch/qgis-server-light.git@master#qgis_server_light"
```





## ✅ Next Steps
See the [Workflow](workflow.md)
