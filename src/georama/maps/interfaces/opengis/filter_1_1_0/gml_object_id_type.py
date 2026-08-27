from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_id_type import AbstractIdType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class GmlObjectIdType(AbstractIdType):
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
