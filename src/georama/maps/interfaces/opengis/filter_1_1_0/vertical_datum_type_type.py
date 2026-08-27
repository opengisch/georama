from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class VerticalDatumTypeType(CodeType):
    """
    Type of a vertical datum.

    :ivar code_space: Reference to a source of information specifying
        the values and meanings of all the allowed string values for
        this VerticalDatumTypeType.
    """

    code_space: str | None = field(
        default=None,
        metadata={
            "name": "codeSpace",
            "type": "Attribute",
            "required": True,
        },
    )
