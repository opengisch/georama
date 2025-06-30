from dataclasses import dataclass, field
from typing import Union

from georama.maps.interfaces.opengis.filter_1_1_0.curve_property_type import (
    CompositeCurve,
    Curve,
    OrientableCurve,
)
from georama.maps.interfaces.opengis.filter_1_1_0.line_string import LineString

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CurveArrayPropertyType:
    """A container for an array of curves.

    The elements are always contained in the array property, referencing
    geometry elements or arrays of geometry elements is not supported.
    """

    choice: list[Union[OrientableCurve, Curve, CompositeCurve, LineString]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OrientableCurve",
                    "type": OrientableCurve,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Curve",
                    "type": Curve,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CompositeCurve",
                    "type": CompositeCurve,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "LineString",
                    "type": LineString,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )
