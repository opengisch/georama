from dataclasses import dataclass

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class NoValues:
    """
    Specifies that no values are allowed for this parameter or quantity.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
