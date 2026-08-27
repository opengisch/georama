from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.maximum_value import MaximumValue
from georama.maps.interfaces.ogc.wfs_2_0_0.minimum_value import MinimumValue
from georama.maps.interfaces.ogc.wfs_2_0_0.range_closure_value import RangeClosureValue
from georama.maps.interfaces.ogc.wfs_2_0_0.spacing import Spacing

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class RangeType:
    """A range of values of a numeric parameter.

    This range can be continuous or discrete, defined by a fixed spacing
    between adjacent valid values. If the MinimumValue or MaximumValue
    is not included, there is no value limit in that direction.
    Inclusion of the specified minimum and maximum values in the range
    shall be defined by the rangeClosure.

    :ivar minimum_value:
    :ivar maximum_value:
    :ivar spacing: Shall be included when the allowed values are NOT
        continuous in this range. Shall not be included when the allowed
        values are continuous in this range.
    :ivar range_closure: Shall be included unless the default value
        applies.
    """

    minimum_value: MinimumValue | None = field(
        default=None,
        metadata={
            "name": "MinimumValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    maximum_value: MaximumValue | None = field(
        default=None,
        metadata={
            "name": "MaximumValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    spacing: Spacing | None = field(
        default=None,
        metadata={
            "name": "Spacing",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    range_closure: RangeClosureValue = field(
        default=RangeClosureValue.CLOSED,
        metadata={
            "name": "rangeClosure",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
