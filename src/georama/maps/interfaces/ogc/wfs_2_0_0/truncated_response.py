from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.exception_report import ExceptionReport

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class TruncatedResponse:
    class Meta:
        name = "truncatedResponse"
        namespace = "http://www.opengis.net/wfs/2.0"

    exception_report: ExceptionReport | None = field(
        default=None,
        metadata={
            "name": "ExceptionReport",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
            "required": True,
        },
    )
