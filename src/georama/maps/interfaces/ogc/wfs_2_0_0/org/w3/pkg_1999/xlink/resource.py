from dataclasses import dataclass

from wfs_2_0_0.org.w3.pkg_1999.xlink.resource_type import ResourceType

__NAMESPACE__ = "http://www.w3.org/1999/xlink"


@dataclass
class Resource(ResourceType):
    class Meta:
        name = "resource"
        namespace = "http://www.w3.org/1999/xlink"
