from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.resource_type import ResourceType

__NAMESPACE__ = "http://www.w3.org/1999/xlink"


@dataclass
class Resource(ResourceType):
    class Meta:
        name = "resource"
        namespace = "http://www.w3.org/1999/xlink"
