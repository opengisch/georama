from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.ellipsoid_base_type import (
    EllipsoidBaseType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.ellipsoid_id import EllipsoidId
from georama.maps.interfaces.opengis.filter_1_1_0.remarks import Remarks
from georama.maps.interfaces.opengis.filter_1_1_0.second_defining_parameter import (
    SecondDefiningParameter,
)
from georama.maps.interfaces.opengis.filter_1_1_0.semi_major_axis import SemiMajorAxis

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EllipsoidType(EllipsoidBaseType):
    """An ellipsoid is a geometric figure that can be used to describe the
    approximate shape of the earth.

    In mathematical terms, it is a surface formed by the rotation of an
    ellipse about its minor axis.

    :ivar ellipsoid_id: Set of alternative identifications of this
        ellipsoid. The first ellipsoidID, if any, is normally the
        primary identification code, and any others are aliases.
    :ivar remarks: Comments on or information about this ellipsoid,
        including source information.
    :ivar semi_major_axis:
    :ivar second_defining_parameter:
    """

    ellipsoid_id: list[EllipsoidId] = field(
        default_factory=list,
        metadata={
            "name": "ellipsoidID",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    remarks: Remarks | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    semi_major_axis: SemiMajorAxis | None = field(
        default=None,
        metadata={
            "name": "semiMajorAxis",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    second_defining_parameter: SecondDefiningParameter | None = field(
        default=None,
        metadata={
            "name": "secondDefiningParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
