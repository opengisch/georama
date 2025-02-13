from dataclasses import dataclass, field

from wfs_2_0_0.net.opengis.ows.pkg_1.request_method_type import RequestMethodType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class Http:
    """Connect point URLs for the HTTP Distributed Computing Platform (DCP).

    Normally, only one Get and/or one Post is included in this element.
    More than one Get and/or Post is allowed to support including
    alternative URLs for uses such as load balancing or backup.

    :ivar get: Connect point URL prefix and any constraints for the HTTP
        "Get" request method for this operation request.
    :ivar post: Connect point URL and any constraints for the HTTP
        "Post" request method for this operation request.
    """

    class Meta:
        name = "HTTP"
        namespace = "http://www.opengis.net/ows/1.1"

    get: list[RequestMethodType] = field(
        default_factory=list,
        metadata={
            "name": "Get",
            "type": "Element",
        },
    )
    post: list[RequestMethodType] = field(
        default_factory=list,
        metadata={
            "name": "Post",
            "type": "Element",
        },
    )
