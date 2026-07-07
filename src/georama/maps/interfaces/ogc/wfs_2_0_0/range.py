from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.range_type import RangeType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class Range(RangeType):
    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
