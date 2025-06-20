from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.locator_type import LocatorType

__NAMESPACE__ = "http://www.w3.org/1999/xlink"


@dataclass
class Locator(LocatorType):
    class Meta:
        name = "locator"
        namespace = "http://www.w3.org/1999/xlink"
