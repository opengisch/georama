from dataclasses import dataclass

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AnchorPoint:
    class Meta:
        name = "anchorPoint"
        namespace = "http://www.opengis.net/gml/3.2"
