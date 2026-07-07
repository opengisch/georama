from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_crstype import CrspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ReferenceSystemRef(CrspropertyType):
    class Meta:
        name = "referenceSystemRef"
        namespace = "http://www.opengis.net/gml/3.2"
