from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UnitOfMeasureType:
    """Reference to a unit of measure definition that applies to all the numerical
    values described by the element containing this element.

    Notice that a complexType which needs to include the uom attribute
    can do so by extending this complexType. Alternately, this
    complexType can be used as a pattern for a new complexType.

    :ivar uom: Reference to a unit of measure definition, usually within
        the same XML document but possibly outside the XML document
        which contains this reference. For a reference within the same
        XML document, the "#" symbol should be used, followed by a text
        abbreviation of the unit name. However, the "#" symbol may be
        optional, and still may be interpreted as a reference.
    """

    uom: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
