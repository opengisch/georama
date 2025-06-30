from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.resource_type import ResourceType

__NAMESPACE__ = "http://www.w3.org/1999/xlink"


@dataclass
class ResourceAbstract(ResourceType):
    class Meta:
        name = "resource"
        namespace = "http://www.w3.org/1999/xlink"
