from dataclasses import dataclass

from wfs_2_0_0.net.opengis.ows.pkg_1.reference_type import ReferenceType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class Reference(ReferenceType):
    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
