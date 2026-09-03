from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.get import Get
from georama.maps.interfaces.ogc.wfs_2_0_0.post import Post

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class Http:
    """Connect point URLs for the HTTP Distributed Computing Platform (DCP).

    Normally, only one Get and/or one Post is included in this element.
    More than one Get and/or Post is allowed to support including
    alternative URLs for uses such as load balancing or backup.
    """

    class Meta:
        name = "HTTP"
        namespace = "http://www.opengis.net/ows/1.1"

    get_or_post: list[Get | Post] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Get",
                    "type": Get,
                },
                {
                    "name": "Post",
                    "type": Post,
                },
            ),
        },
    )
