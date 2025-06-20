from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.grid_function_type import (
    GridFunctionType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class IndexMapType(GridFunctionType):
    """Exends GridFunctionType with a lookUpTable.

    This contains a list of indexes of members within the rangeSet
    corresponding with the members of the domainSet.  The domainSet is
    traversed in list order if it is enumerated explicitly, or in the
    order specified by a SequenceRule if the domain is an implicit set.
    The length of the lookUpTable corresponds with the length of the
    subset of the domainSet for which the coverage is defined.
    """

    look_up_table: list[int] = field(
        default_factory=list,
        metadata={
            "name": "lookUpTable",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "tokens": True,
        },
    )
