from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.array_association_type import (
    AssociationRoleType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractAssociationRole(AssociationRoleType):
    """Applying this pattern shall restrict the multiplicity of objects in a
    property element using this content model to exactly one. An instance of this
    type shall contain an element representing an object, or serve as a pointer to
    a remote object.

    Applying the pattern to define an application schema specific property type allows to restrict
    -       the inline object to specified object types,
    -       the encoding to „by-reference only“ (see 7.2.3.7),
    -       the encoding to „inline only“ (see 7.2.3.8).
    """

    class Meta:
        name = "abstractAssociationRole"
        namespace = "http://www.opengis.net/gml"
