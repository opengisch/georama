from dataclasses import dataclass, field
from typing import Optional, Union

from georama.maps.interfaces.opengis.filter_1_1_0.actuate_type import ActuateType
from georama.maps.interfaces.opengis.filter_1_1_0.cartesian_cs import CartesianCs
from georama.maps.interfaces.opengis.filter_1_1_0.cylindrical_cs import CylindricalCs
from georama.maps.interfaces.opengis.filter_1_1_0.ellipsoidal_cs import EllipsoidalCs
from georama.maps.interfaces.opengis.filter_1_1_0.linear_cs import LinearCs
from georama.maps.interfaces.opengis.filter_1_1_0.oblique_cartesian_cs import (
    ObliqueCartesianCs,
)
from georama.maps.interfaces.opengis.filter_1_1_0.polar_cs import PolarCs
from georama.maps.interfaces.opengis.filter_1_1_0.show_type import ShowType
from georama.maps.interfaces.opengis.filter_1_1_0.spherical_cs import SphericalCs
from georama.maps.interfaces.opengis.filter_1_1_0.temporal_cs import TemporalCs
from georama.maps.interfaces.opengis.filter_1_1_0.type_type import TypeType
from georama.maps.interfaces.opengis.filter_1_1_0.user_defined_cs import UserDefinedCs
from georama.maps.interfaces.opengis.filter_1_1_0.vertical_cs import VerticalCs

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoordinateSystemRefType:
    """
    Association to a coordinate system, either referencing or containing the
    definition of that coordinate system.
    """

    choice: Optional[
        Union[
            ObliqueCartesianCs,
            CylindricalCs,
            PolarCs,
            SphericalCs,
            UserDefinedCs,
            LinearCs,
            TemporalCs,
            VerticalCs,
            CartesianCs,
            EllipsoidalCs,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ObliqueCartesianCS",
                    "type": ObliqueCartesianCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CylindricalCS",
                    "type": CylindricalCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "PolarCS",
                    "type": PolarCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "SphericalCS",
                    "type": SphericalCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "UserDefinedCS",
                    "type": UserDefinedCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "LinearCS",
                    "type": LinearCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TemporalCS",
                    "type": TemporalCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "VerticalCS",
                    "type": VerticalCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CartesianCS",
                    "type": CartesianCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "EllipsoidalCS",
                    "type": EllipsoidalCs,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        },
    )
