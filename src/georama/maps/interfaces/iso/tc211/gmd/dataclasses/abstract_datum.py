from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.sc_crs_property_type import (
    AbstractDatumType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractDatum(AbstractDatumType):
    """A gml:AbstractDatum specifies the relationship of a coordinate system to the
    earth, thus creating a coordinate reference system.

    A datum uses a parameter or set of parameters that determine the
    location of the origin of the coordinate reference system. Each
    datum subtype may be associated with only specific types of
    coordinate systems. This abstract complex type shall not be used,
    extended, or restricted, in a GML Application Schema, to define a
    concrete subtype with a meaning equivalent to a concrete subtype
    specified in this document.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
