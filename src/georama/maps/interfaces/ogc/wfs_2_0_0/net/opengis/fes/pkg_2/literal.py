from dataclasses import dataclass

from wfs_2_0_0.net.opengis.fes.pkg_2.literal_type import LiteralType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class Literal(LiteralType):
    class Meta:
        namespace = "http://www.opengis.net/fes/2.0"
