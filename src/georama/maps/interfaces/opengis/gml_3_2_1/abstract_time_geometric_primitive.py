from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_time_primitive_type import (
    AbstractTimeGeometricPrimitiveType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractTimeGeometricPrimitive(AbstractTimeGeometricPrimitiveType):
    """Gml:TimeGeometricPrimitive acts as the head of a substitution group for
    geometric temporal primitives.

    A temporal geometry shall be associated with a temporal reference
    system through the frame attribute that provides a URI reference
    that identifies a description of the reference system. Following ISO
    19108, the Gregorian calendar with UTC is the default reference
    system, but others may also be used. The GPS calendar is an
    alternative reference systems in common use. The two geometric
    primitives in the temporal dimension are the instant and the period.
    GML components are defined to support these as follows.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
