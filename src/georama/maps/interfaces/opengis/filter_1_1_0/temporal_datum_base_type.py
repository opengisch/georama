from dataclasses import dataclass, field
from typing import Any

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_datum_type import (
    AbstractDatumType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TemporalDatumBaseType(AbstractDatumType):
    """Partially defines the origin of a temporal coordinate reference system.

    This type restricts the AbstractDatumType to remove the
    "anchorPoint" and "realizationEpoch" elements.

    :ivar remarks: Comments on this reference system, including source
        information.
    :ivar anchor_point:
    :ivar realization_epoch:
    :ivar description:
    :ivar group_name:
    :ivar parameter_name:
    :ivar method_name:
    :ivar coordinate_operation_name:
    :ivar ellipsoid_name:
    :ivar meridian_name:
    :ivar cs_name:
    :ivar srs_name:
    :ivar name: Multiple names may be provided.  These will often be
        distinguished by being assigned by different authorities, as
        indicated by the value of the codeSpace attribute.  In an
        instance document there will usually only be one name per
        authority.
    """

    remarks: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    anchor_point: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    realization_epoch: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    description: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    group_name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    parameter_name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    method_name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    coordinate_operation_name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    ellipsoid_name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    meridian_name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    cs_name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    srs_name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
