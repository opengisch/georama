from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractMemberType:
    """To create a collection of GML Objects that are not all features, a property
    type shall be derived by extension from gml:AbstractMemberType.

    This abstract property type is intended to be used only in object
    types where software shall be able to identify that an instance of
    such an object type is to be interpreted as a collection of objects.
    By default, this abstract property type does not imply any ownership
    of the objects in the collection. The owns attribute of
    gml:OwnershipAttributeGroup may be used on a property element
    instance to assert ownership of an object in the collection. A
    collection shall not own an object already owned by another object.
    """

    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
