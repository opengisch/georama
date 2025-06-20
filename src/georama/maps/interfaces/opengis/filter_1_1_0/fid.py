from dataclasses import dataclass

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class Fid:
    class Meta:
        name = "FID"
        namespace = "http://www.opengis.net/ogc"
