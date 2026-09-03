from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_gmltype import (
    AbstractGmltype,
)
from georama.maps.interfaces.opengis.filter_1_1_0.animate_2 import Animate2
from georama.maps.interfaces.opengis.filter_1_1_0.animate_color_2 import AnimateColor2
from georama.maps.interfaces.opengis.filter_1_1_0.animate_motion_2 import AnimateMotion2
from georama.maps.interfaces.opengis.filter_1_1_0.scale_type import ScaleType
from georama.maps.interfaces.opengis.filter_1_1_0.set_2 import Set2
from georama.maps.interfaces.opengis.filter_1_1_0.style_variation_type import (
    StyleVariationType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class BaseStyleDescriptorType(AbstractGmltype):
    """
    Base complex type for geometry, topology, label and graph styles.
    """

    spatial_resolution: ScaleType | None = field(
        default=None,
        metadata={
            "name": "spatialResolution",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    style_variation: list[StyleVariationType] = field(
        default_factory=list,
        metadata={
            "name": "styleVariation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    animate: list[Animate2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/SMIL20/",
        },
    )
    animate_motion: list[AnimateMotion2] = field(
        default_factory=list,
        metadata={
            "name": "animateMotion",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/SMIL20/",
        },
    )
    animate_color: list[AnimateColor2] = field(
        default_factory=list,
        metadata={
            "name": "animateColor",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/SMIL20/",
        },
    )
    set: list[Set2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/SMIL20/",
        },
    )
