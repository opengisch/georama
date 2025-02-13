from dataclasses import dataclass

from wfs_2_0_0.net.opengis.fes.pkg_2.resource_id_type import ResourceIdType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class ResourceId(ResourceIdType):
    class Meta:
        namespace = "http://www.opengis.net/fes/2.0"
