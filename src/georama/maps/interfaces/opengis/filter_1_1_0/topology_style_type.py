from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.base_style_descriptor_type import (
    BaseStyleDescriptorType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.label_style_2 import LabelStyle2
from georama.maps.interfaces.opengis.filter_1_1_0.symbol import Symbol

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopologyStyleType(BaseStyleDescriptorType):
    """[complexType of] The style descriptor for topologies of a feature.

    Describes individual topology elements styles.
    """

    symbol_or_style: Symbol | str | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "symbol",
                    "type": Symbol,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "style",
                    "type": str,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )
    label_style: LabelStyle2 | None = field(
        default=None,
        metadata={
            "name": "labelStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    topology_property: str | None = field(
        default=None,
        metadata={
            "name": "topologyProperty",
            "type": "Attribute",
        },
    )
    topology_type: str | None = field(
        default=None,
        metadata={
            "name": "topologyType",
            "type": "Attribute",
        },
    )
