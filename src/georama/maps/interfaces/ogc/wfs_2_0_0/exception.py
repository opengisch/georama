from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.exception_type import ExceptionType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class Exception(ExceptionType):
    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
