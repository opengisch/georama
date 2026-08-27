from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.http import Http

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class Dcp:
    """Information for one distributed Computing Platform (DCP) supported for this
    operation.

    At present, only the HTTP DCP is defined, so this element only
    includes the HTTP element.
    """

    class Meta:
        name = "DCP"
        namespace = "http://www.opengis.net/ows/1.1"

    http: Http | None = field(
        default=None,
        metadata={
            "name": "HTTP",
            "type": "Element",
            "required": True,
        },
    )
