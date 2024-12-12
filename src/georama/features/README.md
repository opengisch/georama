# Vectorparrot

![](static/features/assets/img/logo.jpg)

Extracts vector features with pygeoapi power


## Handling pygeoapi config

The configuration to pygeoapi is created directly from the corresponding schemas
to avoid boilerplate code. We use xsdata for that.

We have 2 configuration which have to be implemented:

- server config
- oapi config

For both we can create the necesary python classes for de-/serialization with xsdata as follows:

### Server configuration

It is available [here](https://github.com/geopython/pygeoapi/blob/master/pygeoapi/schemas/config/pygeoapi-config-0.x.yml)

For some reason they offer it as a yml file written as a JSON schema. We need to convert
yml first to json:

```python
import json
import yaml
import requests
r = requests.get("https://raw.githubusercontent.com/geopython/pygeoapi/0.17.0/pygeoapi/schemas/config/pygeoapi-config-0.x.yml")
yaml_object = yaml.safe_load(r.content)
with open('/tmp/pygeoapi-config-0.x.json', "w+") as fh:
    fh.write(json.dumps(yaml_object, indent=2))
```

Once we have this we can generate the python classes with xsdata:
```shell
xsdata generate -p interfaces.pygeoapi.server /tmp/pygeoapi-config-0.x.jsonschema
```

this will write a python package to `interfaces/pygeoapi/server` folder.

It is necessary to change the first line in [__init__.py](interfaces/pygeoapi/server/__init__.py)

from

```python
from interfaces.pygeoapi.server.server import (
```

to

```python
from georama.features.interfaces.pygeoapi.server.server import (
```

after every new creation.

### OAPI configuration

The configuration is available [here (pygeoapi v0.17.0)](https://raw.githubusercontent.com/geopython/pygeoapi/0.17.0/pygeoapi/schemas/openapi/openapi-3.0.x.json)
and since it is a json schema directly we can simply use this to create the corresponding classes:

```shell
xsdata generate -p interfaces.pygeoapi.openapi https://raw.githubusercontent.com/geopython/pygeoapi/0.17.0/pygeoapi/schemas/openapi/openapi-3.0.x.json
```
