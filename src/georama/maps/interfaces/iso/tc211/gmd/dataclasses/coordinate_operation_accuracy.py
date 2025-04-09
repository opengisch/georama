from dataclasses import dataclass, field
from typing import Optional, Union

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.actuate_value import ActuateValue
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.dq_absolute_external_positional_accuracy import (
    DqAbsoluteExternalPositionalAccuracy,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.dq_gridded_data_positional_accuracy import (
    DqGriddedDataPositionalAccuracy,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.dq_relative_internal_positional_accuracy import (
    DqRelativeInternalPositionalAccuracy,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.show_value import ShowValue

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoordinateOperationAccuracy:
    """Gml:coordinateOperationAccuracy is an association role to a
    DQ_PositionalAccuracy object as encoded in ISO/TS 19139, either referencing or
    containing the definition of that positional accuracy.

    That object contains an estimate of the impact of this coordinate
    operation on point accuracy. That is, it gives position error
    estimates for the target coordinates of this coordinate operation,
    assuming no errors in the source coordinates.
    """

    class Meta:
        name = "coordinateOperationAccuracy"
        namespace = "http://www.opengis.net/gml"

    dq_absolute_external_positional_accuracy: Optional[
        DqAbsoluteExternalPositionalAccuracy
    ] = field(
        default=None,
        metadata={
            "name": "DQ_AbsoluteExternalPositionalAccuracy",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    dq_gridded_data_positional_accuracy: Optional[DqGriddedDataPositionalAccuracy] = field(
        default=None,
        metadata={
            "name": "DQ_GriddedDataPositionalAccuracy",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    dq_relative_internal_positional_accuracy: Optional[
        DqRelativeInternalPositionalAccuracy
    ] = field(
        default=None,
        metadata={
            "name": "DQ_RelativeInternalPositionalAccuracy",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    type_value: str = field(
        init=False,
        default="simple",
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        },
    )
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        },
    )
