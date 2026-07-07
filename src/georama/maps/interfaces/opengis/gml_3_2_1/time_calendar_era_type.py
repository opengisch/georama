from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union

from xsdata.models.datatype import XmlDate, XmlPeriod

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_time_primitive_type import (
    TimePeriodPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.definition_type import DefinitionType
from georama.maps.interfaces.opengis.gml_3_2_1.string_or_ref_type import StringOrRefType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TimeCalendarEraType(DefinitionType):
    reference_event: Optional[StringOrRefType] = field(
        default=None,
        metadata={
            "name": "referenceEvent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    reference_date: Optional[Union[XmlDate, XmlPeriod]] = field(
        default=None,
        metadata={
            "name": "referenceDate",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    julian_reference: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "julianReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    epoch_of_use: Optional[TimePeriodPropertyType] = field(
        default=None,
        metadata={
            "name": "epochOfUse",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
