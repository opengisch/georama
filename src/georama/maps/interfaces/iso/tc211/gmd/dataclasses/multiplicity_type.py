from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.multiplicity_range_property_type import (
    MultiplicityRangePropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class MultiplicityType(AbstractObjectType):
    """Use to represent the possible cardinality of a relation.

    Represented by a set of simple multiplicity ranges.
    """

    class Meta:
        name = "Multiplicity_Type"

    range: list[MultiplicityRangePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
            "min_occurs": 1,
        },
    )
