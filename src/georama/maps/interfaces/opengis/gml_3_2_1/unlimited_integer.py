from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.unlimited_integer_type import (
    UnlimitedIntegerType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class UnlimitedInteger(UnlimitedIntegerType):
    class Meta:
        nillable = True
        namespace = "http://www.isotc211.org/2005/gco"
