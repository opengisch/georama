from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_id_type import AbstractIdType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class Id(AbstractIdType):
    class Meta:
        name = "_Id"
        namespace = "http://www.opengis.net/ogc"
