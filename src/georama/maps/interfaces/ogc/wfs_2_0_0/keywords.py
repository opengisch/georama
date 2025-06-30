from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.keywords_type import KeywordsType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class Keywords(KeywordsType):
    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
