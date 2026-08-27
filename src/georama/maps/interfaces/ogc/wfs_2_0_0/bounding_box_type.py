from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class BoundingBoxType:
    """XML encoded minimum rectangular bounding box (or region) parameter,
    surrounding all the associated data.

    This type is adapted from the EnvelopeType of GML 3.1, with modified
    contents and documentation for encoding a MINIMUM size box
    SURROUNDING all associated data.

    :ivar lower_corner: Position of the bounding box corner at which the
        value of each coordinate normally is the algebraic minimum
        within this bounding box. In some cases, this position is
        normally displayed at the top, such as the top left for some
        image coordinates. For more information, see Subclauses 10.2.5
        and C.13.
    :ivar upper_corner: Position of the bounding box corner at which the
        value of each coordinate normally is the algebraic maximum
        within this bounding box. In some cases, this position is
        normally displayed at the bottom, such as the bottom right for
        some image coordinates. For more information, see Subclauses
        10.2.5 and C.13.
    :ivar crs: Usually references the definition of a CRS, as specified
        in [OGC Topic 2]. Such a CRS definition can be XML encoded using
        the gml:CoordinateReferenceSystemType in [GML 3.1]. For well
        known references, it is not required that a CRS definition exist
        at the location the URI points to. If no anyURI value is
        included, the applicable CRS must be either: a)      Specified
        outside the bounding box, but inside a data structure that
        includes this bounding box, as specified for a specific OWS use
        of this bounding box type. b)      Fixed and specified in the
        Implementation Specification for a specific OWS use of the
        bounding box type.
    :ivar dimensions: The number of dimensions in this CRS (the length
        of a coordinate sequence in this use of the PositionType). This
        number is specified by the CRS definition, but can also be
        specified here.
    """

    lower_corner: list[float] = field(
        default_factory=list,
        metadata={
            "name": "LowerCorner",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
            "tokens": True,
        },
    )
    upper_corner: list[float] = field(
        default_factory=list,
        metadata={
            "name": "UpperCorner",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
            "tokens": True,
        },
    )
    crs: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dimensions: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
