from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.reference_type import ReferenceType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DataSourceReference(ReferenceType):
    """
    Evidence is represented by a simple gml:dataSource or gml:dataSourceReference
    property that indicates the source of the temporal data.
    """

    class Meta:
        name = "dataSourceReference"
        namespace = "http://www.opengis.net/gml/3.2"
