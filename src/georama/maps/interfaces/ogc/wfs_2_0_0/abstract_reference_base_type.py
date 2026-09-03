from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.actuate_type import ActuateType
from georama.maps.interfaces.ogc.wfs_2_0_0.show_type import ShowType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class AbstractReferenceBaseType:
    """Base for a reference to a remote or local resource.

    This type contains only a restricted and annotated set of the
    attributes from the xlink:simpleAttrs attributeGroup.

    :ivar type_value:
    :ivar href: Reference to a remote resource or local payload. A
        remote resource is typically addressed by a URL. For a local
        payload (such as a multipart mime message), the xlink:href must
        start with the prefix cid:.
    :ivar role: Reference to a resource that describes the role of this
        reference. When no value is supplied, no particular role value
        is to be inferred.
    :ivar arcrole: Although allowed, this attribute is not expected to
        be useful in this application of xlink:simpleAttrs.
    :ivar title: Describes the meaning of the referenced resource in a
        human-readable fashion.
    :ivar show: Although allowed, this attribute is not expected to be
        useful in this application of xlink:simpleAttrs.
    :ivar actuate: Although allowed, this attribute is not expected to
        be useful in this application of xlink:simpleAttrs.
    """

    type_value: str = field(
        init=False,
        default="simple",
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    href: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "required": True,
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
