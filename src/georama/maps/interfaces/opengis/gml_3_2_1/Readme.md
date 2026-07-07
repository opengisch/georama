This module was created by the following commands (in project root) on 22.05.2025 12:30:
```shell
source .venv/bin/activate
xsdata generate -p gml_3_2_1 -r --unnest-classes -ss clusters https://schemas.opengis.net/gml/3.2.1/gml.xsd
rm src/georama/maps/interfaces/opengis/gml_3_2_1/*.py
mv gml_3_2_1/*.py src/georama/maps/interfaces/opengis/gml_3_2_1/
rm -r gml_3_2_1
find src/georama/maps/interfaces/opengis/gml_3_2_1/ -type f -name '*.py' -exec sed -i 's/from gml_3_2_1/from georama.maps.interfaces.opengis.gml_3_2_1/g' {} \;
deactivate
```
