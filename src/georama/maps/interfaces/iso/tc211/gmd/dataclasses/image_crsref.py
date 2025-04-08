from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.image_crsproperty_type import (
    ImageCrspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ImageCrsref(ImageCrspropertyType):
    class Meta:
        name = "imageCRSRef"
        namespace = "http://www.opengis.net/gml"
