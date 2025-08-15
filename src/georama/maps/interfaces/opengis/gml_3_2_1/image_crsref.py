from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.image_crsproperty_type import (
    ImageCrspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ImageCrsref(ImageCrspropertyType):
    class Meta:
        name = "imageCRSRef"
        namespace = "http://www.opengis.net/gml/3.2"
