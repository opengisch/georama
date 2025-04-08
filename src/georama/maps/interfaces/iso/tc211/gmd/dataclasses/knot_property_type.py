from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.knot_type import KnotType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class KnotPropertyType:
    """
    Gml:KnotPropertyType encapsulates a knot to use it in a geometric type.

    :ivar knot: A knot is a breakpoint on a piecewise spline curve.
        value is the value of the parameter at the knot of the spline
        (see ISO 19107:2003, 6.4.24.2). multiplicity is the multiplicity
        of this knot used in the definition of the spline (with the same
        weight). weight is the value of the averaging weight used for
        this knot of the spline.
    """

    knot: Optional[KnotType] = field(
        default=None,
        metadata={
            "name": "Knot",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
