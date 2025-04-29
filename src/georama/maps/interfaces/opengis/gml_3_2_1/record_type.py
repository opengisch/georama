from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.record_type_type import RecordTypeType

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class RecordType(RecordTypeType):
    class Meta:
        namespace = "http://www.isotc211.org/2005/gco"
