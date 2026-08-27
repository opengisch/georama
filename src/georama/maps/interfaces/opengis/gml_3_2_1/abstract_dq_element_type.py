from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.character_string_property_type import (
    CharacterStringPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.date_time_property_type import (
    DateTimePropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.dq_evaluation_method_type_code_property_type import (
    DqEvaluationMethodTypeCodePropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.dq_result_property_type import (
    DqResultPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_identifier_type import (
    CiCitationPropertyType,
    MdIdentifierPropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class AbstractDqElementType(AbstractObjectType):
    class Meta:
        name = "AbstractDQ_Element_Type"

    name_of_measure: list[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "nameOfMeasure",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    measure_identification: MdIdentifierPropertyType | None = field(
        default=None,
        metadata={
            "name": "measureIdentification",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    measure_description: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "measureDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    evaluation_method_type: DqEvaluationMethodTypeCodePropertyType | None = field(
        default=None,
        metadata={
            "name": "evaluationMethodType",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    evaluation_method_description: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "evaluationMethodDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    evaluation_procedure: CiCitationPropertyType | None = field(
        default=None,
        metadata={
            "name": "evaluationProcedure",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    date_time: list[DateTimePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "dateTime",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    result: list[DqResultPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )
