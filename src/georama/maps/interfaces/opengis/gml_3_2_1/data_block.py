from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.data_block_type import DataBlockType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DataBlock(DataBlockType):
    """Gml:DataBlock describes the Range as a block of text encoded values similar
    to a Common Separated Value (CSV) representation.

    The range set parameterization is described by the property
    gml:rangeParameters.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
