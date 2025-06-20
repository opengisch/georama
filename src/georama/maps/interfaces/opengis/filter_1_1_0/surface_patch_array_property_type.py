from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.cone import Cone
from georama.maps.interfaces.opengis.filter_1_1_0.cylinder import Cylinder
from georama.maps.interfaces.opengis.filter_1_1_0.polygon_patch import PolygonPatch
from georama.maps.interfaces.opengis.filter_1_1_0.rectangle import Rectangle
from georama.maps.interfaces.opengis.filter_1_1_0.sphere import Sphere
from georama.maps.interfaces.opengis.filter_1_1_0.triangle import Triangle

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SurfacePatchArrayPropertyType:
    """
    A container for an array of surface patches.
    """

    sphere: list[Sphere] = field(
        default_factory=list,
        metadata={
            "name": "Sphere",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequence": 1,
        },
    )
    cylinder: list[Cylinder] = field(
        default_factory=list,
        metadata={
            "name": "Cylinder",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequence": 1,
        },
    )
    cone: list[Cone] = field(
        default_factory=list,
        metadata={
            "name": "Cone",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequence": 1,
        },
    )
    rectangle: list[Rectangle] = field(
        default_factory=list,
        metadata={
            "name": "Rectangle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequence": 1,
        },
    )
    triangle: list[Triangle] = field(
        default_factory=list,
        metadata={
            "name": "Triangle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequence": 1,
        },
    )
    polygon_patch: list[PolygonPatch] = field(
        default_factory=list,
        metadata={
            "name": "PolygonPatch",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequence": 1,
        },
    )
