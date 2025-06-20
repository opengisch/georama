from dataclasses import dataclass

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class Eid:
    class Meta:
        name = "EID"
        namespace = "http://www.opengis.net/ogc"
