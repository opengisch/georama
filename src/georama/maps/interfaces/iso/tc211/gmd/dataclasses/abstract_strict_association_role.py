from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.array_association_type import (
    AssociationRoleType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractStrictAssociationRole(AssociationRoleType):
    """
    This element shows how an element declaration may include a Schematron
    constraint to limit the property to act in either inline or by-reference mode,
    but not both.
    """

    class Meta:
        name = "abstractStrictAssociationRole"
        namespace = "http://www.opengis.net/gml"
