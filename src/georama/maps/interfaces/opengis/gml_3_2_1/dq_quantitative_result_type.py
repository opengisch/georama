from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_dq_result_type import (
    AbstractDqResultType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.character_string_property_type import (
    CharacterStringPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.record_property_type import (
    RecordPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.record_type_property_type import (
    RecordTypePropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.unit_of_measure_property_type import (
    UnitOfMeasurePropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqQuantitativeResultType(AbstractDqResultType):
    """Quantitative_conformance_measure from Quality Procedures.

    -  - Renamed to remove implied use limitation -  - OCL - -- result is type specified by valueDomain - result.tupleType = valueDomain
    """

    class Meta:
        name = "DQ_QuantitativeResult_Type"

    value_type: RecordTypePropertyType | None = field(
        default=None,
        metadata={
            "name": "valueType",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    value_unit: UnitOfMeasurePropertyType | None = field(
        default=None,
        metadata={
            "name": "valueUnit",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    error_statistic: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "errorStatistic",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    value: list[RecordPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        },
    )
