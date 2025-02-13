from dataclasses import dataclass

from wfs_2_0_0.net.opengis.ows.pkg_1.get_resource_by_id_type import GetResourceByIdType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class GetResourceById(GetResourceByIdType):
    class Meta:
        name = "GetResourceByID"
        namespace = "http://www.opengis.net/ows/1.1"
