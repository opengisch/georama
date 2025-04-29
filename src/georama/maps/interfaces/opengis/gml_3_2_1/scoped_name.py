from dataclasses import dataclass

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class ScopedName:
    class Meta:
        namespace = "http://www.isotc211.org/2005/gco"
