from adrf.routers import DefaultRouter as AdrfDefaultRouter
from adrf.routers import SimpleRouter as AdrfSimpleRouter


class SimpleRouter(AdrfSimpleRouter):
    """A SimpleRouter that omits trailing slashes by default."""

    def __init__(self, *args, trailing_slash=False, **kwargs):
        super().__init__(*args, trailing_slash=trailing_slash, **kwargs)


class DefaultRouter(AdrfDefaultRouter):
    """A DefaultRouter that omits trailing slashes by default."""

    def __init__(self, *args, trailing_slash=False, **kwargs):
        super().__init__(*args, trailing_slash=trailing_slash, **kwargs)
