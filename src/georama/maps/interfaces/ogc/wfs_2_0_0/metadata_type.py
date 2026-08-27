from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.actuate_type import ActuateType
from georama.maps.interfaces.ogc.wfs_2_0_0.show_type import ShowType
from georama.maps.interfaces.ogc.wfs_2_0_0.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class MetadataType:
    """This element either references or contains more metadata about the element
    that includes this element.

    To reference metadata stored remotely, at least the xlinks:href
    attribute in xlink:simpleAttrs shall be included. Either at least
    one of the attributes in xlink:simpleAttrs or a substitute for the
    AbstractMetaData element shall be included, but not both. An
    Implementation Specification can restrict the contents of this
    element to always be a reference or always contain metadata.
    (Informative: This element was adapted from the metaDataProperty
    element in GML 3.0.)

    :ivar type_value:
    :ivar href:
    :ivar role:
    :ivar arcrole:
    :ivar title:
    :ivar show:
    :ivar actuate:
    :ivar about: Optional reference to the aspect of the element which
        includes this "metadata" element that this metadata provides
        more information about.
    """

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
    about: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
