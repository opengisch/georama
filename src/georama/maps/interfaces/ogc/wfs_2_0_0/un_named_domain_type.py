from dataclasses import dataclass, field
from typing import Optional, Union

from georama.maps.interfaces.ogc.wfs_2_0_0.allowed_values import AllowedValues
from georama.maps.interfaces.ogc.wfs_2_0_0.any_value import AnyValue
from georama.maps.interfaces.ogc.wfs_2_0_0.data_type import DataType
from georama.maps.interfaces.ogc.wfs_2_0_0.default_value import DefaultValue
from georama.maps.interfaces.ogc.wfs_2_0_0.meaning import Meaning
from georama.maps.interfaces.ogc.wfs_2_0_0.metadata import Metadata
from georama.maps.interfaces.ogc.wfs_2_0_0.no_values import NoValues
from georama.maps.interfaces.ogc.wfs_2_0_0.reference_system import ReferenceSystem
from georama.maps.interfaces.ogc.wfs_2_0_0.uom import Uom
from georama.maps.interfaces.ogc.wfs_2_0_0.values_reference import ValuesReference

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class UnNamedDomainType:
    """
    Valid domain (or allowed set of values) of one quantity, with needed metadata
    but without a quantity name or identifier.

    :ivar choice:
    :ivar default_value: Optional default value for this quantity, which
        should be included when this quantity has a default value.
    :ivar meaning: Meaning metadata should be referenced or included for
        each quantity.
    :ivar data_type: This data type metadata should be referenced or
        included for each quantity.
    :ivar uom_or_reference_system:
    :ivar metadata: Optional unordered list of other metadata about this
        quantity. A list of required and optional other metadata
        elements for this quantity should be specified in the
        Implementation Specification for this service.
    """

    choice: Optional[Union[AllowedValues, AnyValue, NoValues, ValuesReference]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AllowedValues",
                    "type": AllowedValues,
                    "namespace": "http://www.opengis.net/ows/1.1",
                },
                {
                    "name": "AnyValue",
                    "type": AnyValue,
                    "namespace": "http://www.opengis.net/ows/1.1",
                },
                {
                    "name": "NoValues",
                    "type": NoValues,
                    "namespace": "http://www.opengis.net/ows/1.1",
                },
                {
                    "name": "ValuesReference",
                    "type": ValuesReference,
                    "namespace": "http://www.opengis.net/ows/1.1",
                },
            ),
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
    uom_or_reference_system: Optional[Union[Uom, ReferenceSystem]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "UOM",
                    "type": Uom,
                    "namespace": "http://www.opengis.net/ows/1.1",
                },
                {
                    "name": "ReferenceSystem",
                    "type": ReferenceSystem,
                    "namespace": "http://www.opengis.net/ows/1.1",
                },
            ),
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
