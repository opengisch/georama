from dataclasses import dataclass

from wfs_2_0_0.net.opengis.ows.pkg_1.exception_type import ExceptionType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class Exception(ExceptionType):
    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
