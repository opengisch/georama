from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.cone import Cone
from georama.maps.interfaces.opengis.gml_3_2_1.cylinder import Cylinder
from georama.maps.interfaces.opengis.gml_3_2_1.polygon_patch import PolygonPatch
from georama.maps.interfaces.opengis.gml_3_2_1.rectangle import Rectangle
from georama.maps.interfaces.opengis.gml_3_2_1.sphere import Sphere
from georama.maps.interfaces.opengis.gml_3_2_1.triangle import Triangle

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class SurfacePatchArrayPropertyType:
    """
    Gml:SurfacePatchArrayPropertyType is a container for a sequence of surface
    patches.
    """

    sphere: list[Sphere] = field(
        default_factory=list,
        metadata={
            "name": "Sphere",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    cylinder: list[Cylinder] = field(
        default_factory=list,
        metadata={
            "name": "Cylinder",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    cone: list[Cone] = field(
        default_factory=list,
        metadata={
            "name": "Cone",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    rectangle: list[Rectangle] = field(
        default_factory=list,
        metadata={
            "name": "Rectangle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    triangle: list[Triangle] = field(
        default_factory=list,
        metadata={
            "name": "Triangle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    polygon_patch: list[PolygonPatch] = field(
        default_factory=list,
        metadata={
            "name": "PolygonPatch",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
