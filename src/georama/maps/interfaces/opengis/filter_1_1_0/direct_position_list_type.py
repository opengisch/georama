from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DirectPositionListType:
    """
    DirectPositionList instances hold the coordinates for a sequence of direct
    positions within the same coordinate reference system (CRS).

    :ivar value:
    :ivar srs_name: In general this reference points to a CRS instance
        of gml:CoordinateReferenceSystemType (see
        coordinateReferenceSystems.xsd). For well known references it is
        not required that the CRS description exists at the location the
        URI points to. If no srsName attribute is given, the CRS must be
        specified as part of the larger context this geometry element is
        part of, e.g. a geometric element like point, curve, etc. It is
        expected that this attribute will be specified at the direct
        position level only in rare cases.
    :ivar srs_dimension: The "srsDimension" is the length of coordinate
        sequence (the number of entries in the list). This dimension is
        specified by the coordinate reference system. When the srsName
        attribute is omitted, this attribute shall be omitted.
    :ivar axis_labels: Ordered list of labels for all the axes of this
        CRS. The gml:axisAbbrev value should be used for these axis
        labels, after spaces and forbiddden characters are removed. When
        the srsName attribute is included, this attribute is optional.
        When the srsName attribute is omitted, this attribute shall also
        be omitted.
    :ivar uom_labels: Ordered list of unit of measure (uom) labels for
        all the axes of this CRS. The value of the string in the
        gml:catalogSymbol should be used for this uom labels, after
        spaces and forbiddden characters are removed. When the
        axisLabels attribute is included, this attribute shall also be
        included. When the axisLabels attribute is omitted, this
        attribute shall also be omitted.
    :ivar count: "count" allows to specify the number of direct
        positions in the list. If the attribute count is present then
        the attribute srsDimension shall be present, too.
    """

    value: list[float] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
    srs_name: str | None = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        },
    )
    srs_dimension: int | None = field(
        default=None,
        metadata={
            "name": "srsDimension",
            "type": "Attribute",
        },
    )
    axis_labels: list[str] = field(
        default_factory=list,
        metadata={
            "name": "axisLabels",
            "type": "Attribute",
            "tokens": True,
        },
    )
    uom_labels: list[str] = field(
        default_factory=list,
        metadata={
            "name": "uomLabels",
            "type": "Attribute",
            "tokens": True,
        },
    )
    count: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
