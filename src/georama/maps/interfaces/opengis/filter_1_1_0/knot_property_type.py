from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.knot_type import KnotType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class KnotPropertyType:
    """
    Encapsulates a knot to use it in a geometric type.
    """

    knot: KnotType | None = field(
        default=None,
        metadata={
            "name": "Knot",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
