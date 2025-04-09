from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.reference_type import (
    ReferenceType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DescriptionReference(ReferenceType):
    """The value of this property is a remote text description of the object.

    The xlink:href attribute of the gml:descriptionReference property
    references the external description.
    """

    class Meta:
        name = "descriptionReference"
        namespace = "http://www.opengis.net/gml"
