# Welcome to Georama Documentation!

Georama is a collection of django apps to organize and publish
geodata out of QGIS projects. It handles the following usecases:

- import QGIS project
- publish imported layers as WMS (1.3.0) via [qgis-server-light](https://github.com/opengisch/qgis-server-light)
- publish imported layers as WFS 3 (OGC API Features) via [pygeoapi](https://github.com/geopython/pygeoapi)
- flexible/extendable maintenance of metadata
- permission handling of published resources (layers, columns, metadata, etc.)
- integration with external identity providers via third party django apps

#
