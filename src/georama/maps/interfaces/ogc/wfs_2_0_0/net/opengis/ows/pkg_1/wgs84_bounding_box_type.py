from dataclasses import dataclass, field

from wfs_2_0_0.net.opengis.ows.pkg_1.bounding_box_type import BoundingBoxType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class Wgs84BoundingBoxType(BoundingBoxType):
    """XML encoded minimum rectangular bounding box (or region) parameter,
    surrounding all the associated data.

    This box is specialized for use with the 2D WGS 84 coordinate
    reference system with decimal values of longitude and latitude. This
    type is adapted from the general BoundingBoxType, with modified
    contents and documentation for use with the 2D WGS 84 coordinate
    reference system.

    :ivar crs: This attribute can be included when considered useful.
        When included, this attribute shall reference the 2D WGS 84
        coordinate reference system with longitude before latitude and
        decimal values of longitude and latitude.
    :ivar dimensions: The number of dimensions in this CRS (the length
        of a coordinate sequence in this use of the PositionType). This
        number is specified by the CRS definition, but can also be
        specified here.
    """

    class Meta:
        name = "WGS84BoundingBoxType"

    crs: str = field(
        init=False,
        default="urn:ogc:def:crs:OGC:2:84",
        metadata={
            "type": "Attribute",
        },
    )
    dimensions: int = field(
        init=False,
        default=2,
        metadata={
            "type": "Attribute",
        },
    )
