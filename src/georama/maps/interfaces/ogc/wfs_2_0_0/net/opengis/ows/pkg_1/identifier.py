from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.code_type import (
    CodeType,
)

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class Identifier(CodeType):
    """
    Unique identifier or name of this dataset.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
