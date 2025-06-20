from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MeridianName(CodeType):
    """The name by which this prime meridian is identified.

    The meridianName most common value is Greenwich, and that value
    shall be used when the greenwichLongitude value is zero.
    """

    class Meta:
        name = "meridianName"
        namespace = "http://www.opengis.net/gml"
