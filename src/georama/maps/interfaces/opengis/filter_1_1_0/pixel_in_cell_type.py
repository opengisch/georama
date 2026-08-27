from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PixelInCellType(CodeType):
    """
    Specification of the way an image grid is associated with the image data
    attributes.

    :ivar code_space: Reference to a source of information specifying
        the values and meanings of all the allowed string values for
        this PixelInCellType.
    """

    code_space: str | None = field(
        default=None,
        metadata={
            "name": "codeSpace",
            "type": "Attribute",
            "required": True,
        },
    )
