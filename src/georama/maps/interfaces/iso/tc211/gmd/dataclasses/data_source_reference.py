from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.reference_type import (
    ReferenceType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DataSourceReference(ReferenceType):
    """
    Evidence is represented by a simple gml:dataSource or gml:dataSourceReference
    property that indicates the source of the temporal data.
    """

    class Meta:
        name = "dataSourceReference"
        namespace = "http://www.opengis.net/gml"
