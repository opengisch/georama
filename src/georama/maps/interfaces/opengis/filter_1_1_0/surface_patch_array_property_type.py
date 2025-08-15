from dataclasses import dataclass, field
from typing import Union

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

    choice: list[Union[Sphere, Cylinder, Cone, Rectangle, Triangle, PolygonPatch]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Sphere",
                    "type": Sphere,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Cylinder",
                    "type": Cylinder,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Cone",
                    "type": Cone,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Rectangle",
                    "type": Rectangle,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Triangle",
                    "type": Triangle,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "PolygonPatch",
                    "type": PolygonPatch,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )
