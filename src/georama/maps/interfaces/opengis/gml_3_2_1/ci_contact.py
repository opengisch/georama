from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.ci_contact_type import CiContactType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class CiContact(CiContactType):
    class Meta:
        name = "CI_Contact"
        namespace = "http://www.isotc211.org/2005/gmd"
