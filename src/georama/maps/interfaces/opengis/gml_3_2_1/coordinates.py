from dataclasses import dataclass

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Coordinates:
    class Meta:
        name = "coordinates"
        namespace = "http://www.opengis.net/gml/3.2"
