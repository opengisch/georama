from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.eid import Eid
from georama.maps.interfaces.opengis.filter_1_1_0.fid import Fid

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class IdCapabilitiesType:
    class Meta:
        name = "Id_CapabilitiesType"

    eid_or_fid: list[Eid | Fid] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "EID",
                    "type": Eid,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "FID",
                    "type": Fid,
                    "namespace": "http://www.opengis.net/ogc",
                },
            ),
        },
    )
