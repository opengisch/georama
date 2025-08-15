from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.request_method_type import RequestMethodType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class Get(RequestMethodType):
    class Meta:
        global_type = False
