from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.range_set_type import (
    RangeSetType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class RangeSet(RangeSetType):
    """The gml:rangeSet property element contains the values of the coverage
    (sometimes called the attribute values).

    Its content model is given by gml:RangeSetType. This content model
    supports a structural description of the range.  The semantic
    information describing the range set is embedded using a uniform
    method, as part of the explicit values, or as a template value
    accompanying the representation using gml:DataBlock and gml:File.
    The values from each component (or “band”) in the range may be
    encoded within a gml:ValueArray element or a concrete member of the
    gml:AbstractScalarValueList substitution group . Use of these
    elements satisfies the value-type homogeneity requirement.
    """

    class Meta:
        name = "rangeSet"
        namespace = "http://www.opengis.net/gml"
