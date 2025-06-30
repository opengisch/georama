from dataclasses import dataclass

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class FeatureTypeTypeNoCrs:
    class Meta:
        global_type = False
