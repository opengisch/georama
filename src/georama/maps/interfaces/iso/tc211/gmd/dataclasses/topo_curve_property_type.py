from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.topo_curve import TopoCurve

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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
