from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.datum_ref_type import DatumRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DatumRef(DatumRefType):
    class Meta:
        name = "datumRef"
        namespace = "http://www.opengis.net/gml"
