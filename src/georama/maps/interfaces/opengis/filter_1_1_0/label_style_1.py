from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.label_style_type import LabelStyleType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LabelStyle1(LabelStyleType):
    """
    The style descriptor for labels of a feature, geometry or topology.
    """

    class Meta:
        name = "LabelStyle"
        namespace = "http://www.opengis.net/gml"
