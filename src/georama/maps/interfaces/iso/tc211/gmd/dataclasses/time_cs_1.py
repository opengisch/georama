from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.time_cstype import TimeCstype

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeCs1(TimeCstype):
    """Gml:TimeCS is a one-dimensional coordinate system containing a time axis,
    used to describe the temporal position of a point in the specified time units
    from a specified time origin.

    A TimeCS shall have one gml:axis property element.
    """

    class Meta:
        name = "TimeCS"
        namespace = "http://www.opengis.net/gml"
