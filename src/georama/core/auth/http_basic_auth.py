import base64
import binascii
import logging
from typing import Tuple

from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest, HttpResponse
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import AuthenticationFailed

from georama.core.auth import BaseAuthentication, get_authorization_header

log = logging.getLogger(__name__)


class BasicAuthentication(BaseAuthentication):
    """
    HTTP Basic authentication against username/password.
    """

    www_authenticate_realm = "api"

    def authenticate(self, request) -> Tuple[User, None] | None:
        """
        Returns a `User` if a correct username and password have been supplied
        using HTTP Basic authentication.  Otherwise returns `None`.
        """
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != b"basic":
            return None

        if len(auth) == 1:
            msg = _("Invalid basic header. No credentials provided.")
            log.debug(msg)
            raise PermissionDenied(msg)
        elif len(auth) > 2:
            msg = _("Invalid basic header. Credentials string should not contain spaces.")
            log.debug(msg)
            raise PermissionDenied(msg)

        try:
            try:
                auth_decoded = base64.b64decode(auth[1]).decode("utf-8")
            except UnicodeDecodeError:
                auth_decoded = base64.b64decode(auth[1]).decode("latin-1")

            userid, password = auth_decoded.split(":", 1)
        except (TypeError, ValueError, UnicodeDecodeError, binascii.Error):
            msg = _("Invalid basic header. Credentials not correctly base64 encoded.")
            log.debug(msg)
            raise PermissionDenied(msg)

        return self.authenticate_credentials(userid, password, request)

    def authenticate_credentials(
        self, userid, password, request=None
    ) -> Tuple[User, None] | None:
        """
        Authenticate the userid and password against username and password
        with optional request for context.
        """
        credentials = {get_user_model().USERNAME_FIELD: userid, "password": password}
        user = authenticate(request=request, **credentials)

        if user is None:
            msg = _("Invalid username/password.")
            log.debug(msg)
            raise PermissionDenied(msg)

        if not user.is_active:
            msg = _("User inactive or deleted.")
            log.debug(msg)
            raise PermissionDenied(msg)

        return user, None

    def authenticate_header(self, request):
        return 'Basic realm="%s"' % self.www_authenticate_realm


def basic_http_authentication_middleware(get_response):
    def middleware(request: HttpRequest) -> HttpResponse:
        basic_http_auth = BasicAuthentication()
        # www_authenticate_realm unused at the moment,
        # but setting it as a reminder if used in the future
        basic_http_auth.www_authenticate_realm = "georama"

        if not request.user.is_authenticated:
            try:
                user_token = basic_http_auth.authenticate(request)
                if user_token is not None:
                    log.debug(_("User was authenticated."))
                    request.user = user_token[0]
                    response = get_response(request)
                    return response
            except AuthenticationFailed:
                # AuthenticationFailed: there was a http auth header,
                # but auth failed: consider the user unlogged.
                log.debug(_("User was not authenticated."))
                return HttpResponse("Unauthorized", status=401)
            except Exception as e:
                log.error(e)

    return middleware
