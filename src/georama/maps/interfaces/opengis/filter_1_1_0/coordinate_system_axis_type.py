from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.axis_abbrev import AxisAbbrev
from georama.maps.interfaces.opengis.filter_1_1_0.axis_direction import AxisDirection
from georama.maps.interfaces.opengis.filter_1_1_0.axis_id import AxisId
from georama.maps.interfaces.opengis.filter_1_1_0.coordinate_system_axis_base_type import (
    CoordinateSystemAxisBaseType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.remarks import Remarks

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoordinateSystemAxisType(CoordinateSystemAxisBaseType):
    """
    Definition of a coordinate system axis.

    :ivar axis_id: Set of alternative identifications of this coordinate
        system axis. The first axisID, if any, is normally the primary
        identification code, and any others are aliases.
    :ivar remarks: Comments on or information about this coordinate
        system axis, including data source information.
    :ivar axis_abbrev:
    :ivar axis_direction:
    :ivar uom:
    """

    axis_id: list[AxisId] = field(
        default_factory=list,
        metadata={
            "name": "axisID",
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
    axis_abbrev: AxisAbbrev | None = field(
        default=None,
        metadata={
            "name": "axisAbbrev",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    axis_direction: AxisDirection | None = field(
        default=None,
        metadata={
            "name": "axisDirection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    uom: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
