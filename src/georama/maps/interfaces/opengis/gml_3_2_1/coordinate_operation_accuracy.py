from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.actuate_type import ActuateType
from georama.maps.interfaces.opengis.gml_3_2_1.dq_absolute_external_positional_accuracy import (
    DqAbsoluteExternalPositionalAccuracy,
)
from georama.maps.interfaces.opengis.gml_3_2_1.dq_gridded_data_positional_accuracy import (
    DqGriddedDataPositionalAccuracy,
)
from georama.maps.interfaces.opengis.gml_3_2_1.dq_relative_internal_positional_accuracy import (
    DqRelativeInternalPositionalAccuracy,
)
from georama.maps.interfaces.opengis.gml_3_2_1.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from georama.maps.interfaces.opengis.gml_3_2_1.show_type import ShowType
from georama.maps.interfaces.opengis.gml_3_2_1.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


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
        namespace = "http://www.opengis.net/gml/3.2"

    dq_absolute_external_positional_accuracy: (
        DqAbsoluteExternalPositionalAccuracy | None
    ) = field(
        default=None,
        metadata={
            "name": "DQ_AbsoluteExternalPositionalAccuracy",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    dq_gridded_data_positional_accuracy: DqGriddedDataPositionalAccuracy | None = field(
        default=None,
        metadata={
            "name": "DQ_GriddedDataPositionalAccuracy",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    dq_relative_internal_positional_accuracy: (
        DqRelativeInternalPositionalAccuracy | None
    ) = field(
        default=None,
        metadata={
            "name": "DQ_RelativeInternalPositionalAccuracy",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: ShowType | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: ActuateType | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    nil_reason: str | NilReasonEnumerationValue | None = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        },
    )
    remote_schema: str | None = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
