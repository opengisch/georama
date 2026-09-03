from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.integer_property_type import (
    IntegerPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.unlimited_integer_property_type import (
    UnlimitedIntegerPropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class MultiplicityRangeType(AbstractObjectType):
    """
    A component of a multiplicity, consisting of an non-negative lower bound, and a
    potentially infinite upper bound.
    """

    class Meta:
        name = "MultiplicityRange_Type"

    lower: IntegerPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
            "required": True,
        },
    )
    upper: UnlimitedIntegerPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
            "required": True,
        },
    )
