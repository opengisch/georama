from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.ci_telephone_type import CiTelephoneType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class CiTelephone(CiTelephoneType):
    class Meta:
        name = "CI_Telephone"
        namespace = "http://www.isotc211.org/2005/gmd"
