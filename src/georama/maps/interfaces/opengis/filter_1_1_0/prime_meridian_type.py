from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.greenwich_longitude import (
    GreenwichLongitude,
)
from georama.maps.interfaces.opengis.filter_1_1_0.meridian_id import MeridianId
from georama.maps.interfaces.opengis.filter_1_1_0.prime_meridian_base_type import (
    PrimeMeridianBaseType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.remarks import Remarks

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PrimeMeridianType(PrimeMeridianBaseType):
    """
    A prime meridian defines the origin from which longitude values are determined.

    :ivar meridian_id: Set of alternative identifications of this prime
        meridian. The first meridianID, if any, is normally the primary
        identification code, and any others are aliases.
    :ivar remarks: Comments on or information about this prime meridian,
        including source information.
    :ivar greenwich_longitude:
    """

    meridian_id: list[MeridianId] = field(
        default_factory=list,
        metadata={
            "name": "meridianID",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    remarks: Remarks | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    greenwich_longitude: GreenwichLongitude | None = field(
        default=None,
        metadata={
            "name": "greenwichLongitude",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
