from dataclasses import dataclass

from wfs_2_0_0.net.opengis.ows.pkg_1.reference_group_type import ReferenceGroupType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class ReferenceGroup(ReferenceGroupType):
    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
