from dataclasses import dataclass, field

from wfs_2_0_0.net.opengis.ows.pkg_1.available_crs import AvailableCrs
from wfs_2_0_0.net.opengis.ows.pkg_1.basic_identification_type import (
    BasicIdentificationType,
)
from wfs_2_0_0.net.opengis.ows.pkg_1.bounding_box import BoundingBox
from wfs_2_0_0.net.opengis.ows.pkg_1.output_format import OutputFormat
from wfs_2_0_0.net.opengis.ows.pkg_1.supported_crs import SupportedCrs
from wfs_2_0_0.net.opengis.ows.pkg_1.wgs84_bounding_box import Wgs84BoundingBox

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class IdentificationType(BasicIdentificationType):
    """Extended metadata identifying and describing a set of data.

    This type shall be extended if needed for each specific OWS to
    include additional metadata for each type of dataset. If needed,
    this type should first be restricted for each specific OWS to change
    the multiplicity (or optionality) of some elements.

    :ivar wgs84_bounding_box:
    :ivar bounding_box: Unordered list of zero or more bounding boxes
        whose union describes the extent of this dataset.
    :ivar output_format: Unordered list of zero or more references to
        data formats supported for server outputs.
    :ivar supported_crs:
    :ivar available_crs: Unordered list of zero or more available
        coordinate reference systems.
    """

    wgs84_bounding_box: list[Wgs84BoundingBox] = field(
        default_factory=list,
        metadata={
            "name": "WGS84BoundingBox",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    bounding_box: list[BoundingBox] = field(
        default_factory=list,
        metadata={
            "name": "BoundingBox",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    output_format: list[OutputFormat] = field(
        default_factory=list,
        metadata={
            "name": "OutputFormat",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    supported_crs: list[SupportedCrs] = field(
        default_factory=list,
        metadata={
            "name": "SupportedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    available_crs: list[AvailableCrs] = field(
        default_factory=list,
        metadata={
            "name": "AvailableCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
