from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractMetadataPropertyType:
    """To associate metadata described by any XML Schema with a GML object, a
    property element shall be defined whose content model is derived by extension
    from gml:AbstractMetadataPropertyType.

    The value of such a property shall be metadata. The content model of
    such a property type, i.e. the metadata application schema shall be
    specified by the GML Application Schema. By default, this abstract
    property type does not imply any ownership of the metadata. The owns
    attribute of gml:OwnershipAttributeGroup may be used on a metadata
    property element instance to assert ownership of the metadata. If
    metadata following the conceptual model of ISO 19115 is to be
    encoded in a GML document, the corresponding Implementation
    Specification specified in ISO/TS 19139 shall be used to encode the
    metadata information.
    """

    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
