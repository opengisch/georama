from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.abstract_id_type import AbstractIdType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class Id(AbstractIdType):
    class Meta:
        name = "_Id"
        namespace = "http://www.opengis.net/fes/2.0"
