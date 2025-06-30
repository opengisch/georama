from dataclasses import dataclass, field
from typing import Optional, Union

from georama.maps.interfaces.opengis.filter_1_1_0.base_style_descriptor_type import (
    BaseStyleDescriptorType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.label_style_2 import LabelStyle2
from georama.maps.interfaces.opengis.filter_1_1_0.symbol import Symbol

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeometryStyleType(BaseStyleDescriptorType):
    """
    [complexType of] The style descriptor for geometries of a feature.
    """

    symbol_or_style: Optional[Union[Symbol, str]] = field(
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
    label_style: Optional[LabelStyle2] = field(
        default=None,
        metadata={
            "name": "labelStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geometry_property: Optional[str] = field(
        default=None,
        metadata={
            "name": "geometryProperty",
            "type": "Attribute",
        },
    )
    geometry_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "geometryType",
            "type": "Attribute",
        },
    )
