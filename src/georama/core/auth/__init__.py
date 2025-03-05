from typing import List

from django.http import HttpRequest

# Header encoding (see RFC5987)
HTTP_HEADER_ENCODING = "iso-8859-1"

ALL_AUTHENTICATION_METHODS = [
    ("BASIC_HTTP", "georama.core.auth.http_basic_auth.basic_http_authentication_middleware"),
]


def get_authentication_methods_middlewares(selected_auth_methods: List[str]) -> List[str]:
    return [
        m
        for auth_method, m in ALL_AUTHENTICATION_METHODS
        if auth_method in selected_auth_methods
    ]


class BaseAuthentication:
    """
    All authentication classes should extend BaseAuthentication.
    """

    def authenticate(self, request: HttpRequest):
        """
        Authenticate the request and return a two-tuple of (user, token).
        """
        raise NotImplementedError(".authenticate() must be overridden.")

    def authenticate_header(self, request: HttpRequest):
        """
        Return a string to be used as the value of the `WWW-Authenticate`
        header in a `401 Unauthenticated` response, or `None` if the
        authentication scheme should return `403 Permission Denied` responses.
        """


def get_authorization_header(request: HttpRequest):
    """
    Return request's 'Authorization:' header, as a bytestring.

    Hide some test client ickyness where the header can be unicode.
    """
    auth = request.META.get("HTTP_AUTHORIZATION", b"")
    if isinstance(auth, str):
        # Work around django test client oddness
        auth = auth.encode(HTTP_HEADER_ENCODING)
    return auth
