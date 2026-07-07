from dataclasses import dataclass, field
from typing import Optional, Union

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.measure_type import MeasureType
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Quantity(MeasureType):
    """
    An XML attribute uom (“unit of measure”) is required, whose value is a URI
    which identifies the definition of a ratio scale or units by which the numeric
    value shall be multiplied, or an interval or position scale on which the value
    occurs.
    """

    class Meta:
        nillable = True
        namespace = "http://www.opengis.net/gml"

    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        },
    )
