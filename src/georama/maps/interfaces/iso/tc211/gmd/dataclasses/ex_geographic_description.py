from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.ex_geographic_description_type import (
    ExGeographicDescriptionType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class ExGeographicDescription(ExGeographicDescriptionType):
    class Meta:
        name = "EX_GeographicDescription"
        namespace = "http://www.isotc211.org/2005/gmd"
