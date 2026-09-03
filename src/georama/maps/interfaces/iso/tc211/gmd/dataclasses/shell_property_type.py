from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.shell import Shell

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ShellPropertyType:
    """
    A property with the content model of gml:ShellPropertyType encapsulates a shell
    to represent a component of a solid boundary.
    """

    shell: Shell | None = field(
        default=None,
        metadata={
            "name": "Shell",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
