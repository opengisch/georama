from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.axis_abbrev import AxisAbbrev
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.axis_direction import (
    AxisDirection,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.identified_object_type import (
    IdentifiedObjectType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.maximum_value import MaximumValue
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.minimum_value import MinimumValue
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.range_meaning import RangeMeaning

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoordinateSystemAxisType(IdentifiedObjectType):
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
    minimum_value: MinimumValue | None = field(
        default=None,
        metadata={
            "name": "minimumValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    maximum_value: MaximumValue | None = field(
        default=None,
        metadata={
            "name": "maximumValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    range_meaning: RangeMeaning | None = field(
        default=None,
        metadata={
            "name": "rangeMeaning",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
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
