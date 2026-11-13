from rest_framework.authentication import BaseAuthentication
from rest_framework.request import Request


class MiddlewareAuthentication(BaseAuthentication):
    """Takes the user of Georama's header middlewares (HTTP Basic, bearer token of
    GeoGirafe) over into the REST framework.

    The middleware already checked the credentials, so they aren't checked a second
    time here. Without this class the session authentication of the REST framework
    would take the user and ask for a CSRF token, which a client sending its
    credentials in a header never has.
    """

    # set on the request by the middleware which authenticated the user from a header
    request_flag = "georama_header_authenticated"

    def authenticate(self, request: Request):
        """Picks up the user the middleware put on the request, if it was one of ours.

        Args:
            request: The request of the REST framework.

        Returns:
            The user and no token, or None so the next authentication class is asked.
        """
        if getattr(request._request, self.request_flag, False):
            return request._request.user, None
        return None
