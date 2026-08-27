from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.cone import Cone
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.cylinder import Cylinder
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.polygon_patch import PolygonPatch
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.rectangle import Rectangle
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.sphere import Sphere
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.triangle import Triangle

__NAMESPACE__ = "http://www.opengis.net/gml"


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
