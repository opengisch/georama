from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.topo_curve import TopoCurve

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoCurvePropertyType:
    topo_curve: TopoCurve | None = field(
        default=None,
        metadata={
            "name": "TopoCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
