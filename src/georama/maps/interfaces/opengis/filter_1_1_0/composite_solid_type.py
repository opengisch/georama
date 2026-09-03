from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_solid_type import (
    AbstractSolidType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.actuate_type import ActuateType
from georama.maps.interfaces.opengis.filter_1_1_0.show_type import ShowType
from georama.maps.interfaces.opengis.filter_1_1_0.solid import Solid
from georama.maps.interfaces.opengis.filter_1_1_0.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CompositeSolidType(AbstractSolidType):
    """A composite solid is a geometry type with all the geometric properties of a
    (primitive) solid.

    Essentially, a composite solid is a collection of solids that join
    in pairs on common boundary surfaces and which, when considered as a
    whole, form a single solid.

    :ivar solid_member: This element references or contains one solid in
        the composite solid. The solids are contiguous. NOTE: This
        definition allows for a nested structure, i.e. a CompositeSolid
        may use, for example, another CompositeSolid as a member.
    """

    solid_member: list["SolidMember"] = field(
        default_factory=list,
        metadata={
            "name": "solidMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )


@dataclass
class CompositeSolid(CompositeSolidType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class SolidPropertyType:
    """A property that has a solid as its value domain can either be an appropriate
    geometry element encapsulated in an element of this type or an XLink reference
    to a remote geometry element (where remote includes geometry elements located
    elsewhere in the same document).

    Either the reference or the contained element must be given, but
    neither both nor none.
    """

    solid_or_composite_solid: Solid | CompositeSolid | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Solid",
                    "type": Solid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CompositeSolid",
                    "type": CompositeSolid,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: ShowType | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: ActuateType | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    remote_schema: str | None = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        },
    )


@dataclass
class SolidMember(SolidPropertyType):
    """This property element either references a solid via the XLink-attributes or
    contains the solid element.

    A solid element is any element which is substitutable for "_Solid".
    """

    class Meta:
        name = "solidMember"
        namespace = "http://www.opengis.net/gml"
