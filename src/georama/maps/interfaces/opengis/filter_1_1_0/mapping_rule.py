from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.string_or_ref_type import (
    StringOrRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MappingRule(StringOrRefType):
    """
    Description of a rule for associating members from the domainSet with members
    of the rangeSet.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
