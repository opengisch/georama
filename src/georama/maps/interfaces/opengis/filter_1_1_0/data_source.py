from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.string_or_ref_type import (
    StringOrRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DataSource(StringOrRefType):
    class Meta:
        name = "dataSource"
        namespace = "http://www.opengis.net/gml"
