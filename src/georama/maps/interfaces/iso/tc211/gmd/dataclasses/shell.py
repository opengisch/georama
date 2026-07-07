from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.shell_type import ShellType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Shell(ShellType):
    """A shell is used to represent a single connected component of a solid
    boundary as specified in ISO 19107:2003, 6.3.8.

    Every gml:surfaceMember references or contains one surface, i.e. any
    element which is substitutable for gml:AbstractSurface. In the
    context of a shell, the surfaces describe the boundary of the solid.
    If provided, the aggregationType attribute shall have the value
    “set”.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
