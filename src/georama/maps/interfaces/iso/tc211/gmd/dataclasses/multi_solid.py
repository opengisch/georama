from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.multi_solid_type import (
    MultiSolidType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiSolid(MultiSolidType):
    """A gml:MultiSolid is defined by one or more gml:AbstractSolids.

    The members of the geometric aggregate may be specified either using
    the "standard" property (gml:solidMember) or the array property
    (gml:solidMembers). It is also valid to use both the "standard" and
    the array properties in the same collection.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
