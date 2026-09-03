from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DerivedCrstypeType(CodeType):
    """
    Type of a derived coordinate reference system.

    :ivar code_space: Reference to a source of information specifying
        the values and meanings of all the allowed string values for
        this DerivedCRSTypeType.
    """

    class Meta:
        name = "DerivedCRSTypeType"

    code_space: str | None = field(
        default=None,
        metadata={
            "name": "codeSpace",
            "type": "Attribute",
            "required": True,
        },
    )
