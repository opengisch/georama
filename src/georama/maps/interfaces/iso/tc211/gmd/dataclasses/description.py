from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.string_or_ref_type import (
    StringOrRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Description(StringOrRefType):
    """The value of this property is a text description of the object.

    gml:description uses gml:StringOrRefType as its content model, so it
    may contain a simple text string content, or carry a reference to an
    external description. The use of gml:description to reference an
    external description has been deprecated and replaced by the
    gml:descriptionReference property.
    """

    class Meta:
        name = "description"
        namespace = "http://www.opengis.net/gml"
