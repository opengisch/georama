from dataclasses import dataclass, field
from typing import Union

from georama.maps.interfaces.ogc.wfs_2_0_0.available_crs import AvailableCrs
from georama.maps.interfaces.ogc.wfs_2_0_0.basic_identification_type import (
    BasicIdentificationType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.bounding_box import BoundingBox
from georama.maps.interfaces.ogc.wfs_2_0_0.output_format import OutputFormat
from georama.maps.interfaces.ogc.wfs_2_0_0.supported_crs import SupportedCrs
from georama.maps.interfaces.ogc.wfs_2_0_0.wgs84_bounding_box import Wgs84BoundingBox

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class IdentificationType(BasicIdentificationType):
    """Extended metadata identifying and describing a set of data.

    This type shall be extended if needed for each specific OWS to
    include additional metadata for each type of dataset. If needed,
    this type should first be restricted for each specific OWS to change
    the multiplicity (or optionality) of some elements.

    :ivar wgs84_bounding_box_or_bounding_box:
    :ivar output_format: Unordered list of zero or more references to
        data formats supported for server outputs.
    :ivar supported_crs_or_available_crs:
    """

    wgs84_bounding_box_or_bounding_box: list[Union[Wgs84BoundingBox, BoundingBox]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "WGS84BoundingBox",
                    "type": Wgs84BoundingBox,
                    "namespace": "http://www.opengis.net/ows/1.1",
                },
                {
                    "name": "BoundingBox",
                    "type": BoundingBox,
                    "namespace": "http://www.opengis.net/ows/1.1",
                },
            ),
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
    supported_crs_or_available_crs: list[Union[SupportedCrs, AvailableCrs]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SupportedCRS",
                    "type": SupportedCrs,
                    "namespace": "http://www.opengis.net/ows/1.1",
                },
                {
                    "name": "AvailableCRS",
                    "type": AvailableCrs,
                    "namespace": "http://www.opengis.net/ows/1.1",
                },
            ),
        },
    )
