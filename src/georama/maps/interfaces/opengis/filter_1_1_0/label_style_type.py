from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.base_style_descriptor_type import (
    BaseStyleDescriptorType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.label_type import LabelType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LabelStyleType(BaseStyleDescriptorType):
    """
    [complexType of] The style descriptor for labels of a feature, geometry or
    topology.
    """

    style: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    label: LabelType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
