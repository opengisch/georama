from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.element_type import ElementType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class Element(ElementType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
