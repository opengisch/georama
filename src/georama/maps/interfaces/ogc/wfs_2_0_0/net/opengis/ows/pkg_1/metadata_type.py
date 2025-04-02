from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.ogc.wfs_2_0_0.org.w3.pkg_1999.xlink.actuate_type import (
    ActuateType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.org.w3.pkg_1999.xlink.show_type import (
    ShowType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.org.w3.pkg_1999.xlink.type_type import (
    TypeType,
)

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
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    about: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
