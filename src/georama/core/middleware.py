from django.http import HttpRequest, HttpResponse

from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import AuthenticationFailed


def basic_http_authentication_middleware(get_response):

    def middleware(request: HttpRequest) -> HttpResponse:
        basic_http_auth = BasicAuthentication()
        # www_authenticate_realm unused at the moment,
        # but setting it as a reminder use it in the future
        basic_http_auth.www_authenticate_realm = "georama"

        if not request.user.is_authenticated:
            try:
                user = basic_http_auth.authenticate(request)
            except AuthenticationFailed:
                # AuthenticationFailed: there was a a http auth header,
                # but auth failed: consider the user unlogged.
                pass
            if user is not None:
                request.user = user[0]
        response = get_response(request)
        return response

    return middleware

