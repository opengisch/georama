from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.allowed_values import (
    AllowedValues,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.any_value import (
    AnyValue,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.data_type import (
    DataType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.default_value import (
    DefaultValue,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.meaning import Meaning
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.metadata import (
    Metadata,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.no_values import (
    NoValues,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.reference_system import (
    ReferenceSystem,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.uom import Uom
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.values_reference import (
    ValuesReference,
)

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class UnNamedDomainType:
    """
    Valid domain (or allowed set of values) of one quantity, with needed metadata
    but without a quantity name or identifier.

    :ivar allowed_values:
    :ivar any_value:
    :ivar no_values:
    :ivar values_reference:
    :ivar default_value: Optional default value for this quantity, which
        should be included when this quantity has a default value.
    :ivar meaning: Meaning metadata should be referenced or included for
        each quantity.
    :ivar data_type: This data type metadata should be referenced or
        included for each quantity.
    :ivar uom: Identifier of unit of measure of this set of values.
        Should be included then this set of values has units (and not a
        more complete reference system).
    :ivar reference_system: Identifier of reference system used by this
        set of values. Should be included then this set of values has a
        reference system (not just units).
    :ivar metadata: Optional unordered list of other metadata about this
        quantity. A list of required and optional other metadata
        elements for this quantity should be specified in the
        Implementation Specification for this service.
    """

    allowed_values: Optional[AllowedValues] = field(
        default=None,
        metadata={
            "name": "AllowedValues",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    any_value: Optional[AnyValue] = field(
        default=None,
        metadata={
            "name": "AnyValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    no_values: Optional[NoValues] = field(
        default=None,
        metadata={
            "name": "NoValues",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    values_reference: Optional[ValuesReference] = field(
        default=None,
        metadata={
            "name": "ValuesReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    default_value: Optional[DefaultValue] = field(
        default=None,
        metadata={
            "name": "DefaultValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    meaning: Optional[Meaning] = field(
        default=None,
        metadata={
            "name": "Meaning",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    data_type: Optional[DataType] = field(
        default=None,
        metadata={
            "name": "DataType",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    uom: Optional[Uom] = field(
        default=None,
        metadata={
            "name": "UOM",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    reference_system: Optional[ReferenceSystem] = field(
        default=None,
        metadata={
            "name": "ReferenceSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    metadata: list[Metadata] = field(
        default_factory=list,
        metadata={
            "name": "Metadata",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
