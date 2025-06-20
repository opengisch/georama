from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.eid import Eid
from georama.maps.interfaces.opengis.filter_1_1_0.fid import Fid

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class IdCapabilitiesType:
    class Meta:
        name = "Id_CapabilitiesType"

    eid: list[Eid] = field(
        default_factory=list,
        metadata={
            "name": "EID",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    fid: list[Fid] = field(
        default_factory=list,
        metadata={
            "name": "FID",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
