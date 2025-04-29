from dataclasses import dataclass

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class RangeMeaning:
    """Gml:rangeMeaning describes the meaning of axis value range specified by
    gml:minimumValue and gml:maximumValue.

    This element shall be omitted when both gml:minimumValue and
    gml:maximumValue are omitted. This element should be included when
    gml:minimumValue and/or gml:maximumValue are included. If this
    element is omitted when the gml:minimumValue and/or gml:maximumValue
    are included, the meaning is unspecified. The codeSpace attribute
    shall reference a source of information specifying the values and
    meanings of all the allowed string values for this property.
    """

    class Meta:
        name = "rangeMeaning"
        namespace = "http://www.opengis.net/gml/3.2"
