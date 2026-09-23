import base64
import binascii
import logging

from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest, HttpResponse
from django.utils.translation import gettext_lazy as _

# Header encoding (see RFC5987)
HTTP_HEADER_ENCODING = "iso-8859-1"

log = logging.getLogger(__name__)


class BasicAuthenticationMiddleware:
    """
    HTTP Basic authentication against username/password.
    """

    www_authenticate_realm = "api"

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        if request.path_info.startswith(settings.STATIC_URL):
            return self.get_response(request)

        if not request.user.is_authenticated:
            try:
                user_token = self.authenticate(request)
                if user_token is not None:
                    log.debug(_("User was authenticated."))
                    request.user = user_token[0]
            except PermissionDenied:
                # AuthenticationFailed: there was a http auth header,
                # but auth failed: consider the user unlogged.
                log.debug(_("User was not authenticated."))
                return HttpResponse("Unauthorized", status=401)
            except Exception as e:
                log.error(e)
        return self.get_response(request)

    def authenticate(self, request) -> tuple[AbstractUser, None] | None:
        """
        Returns a `User` if a correct username and password have been supplied
        using HTTP Basic authentication.  Otherwise returns `None`.
        """
        auth = self.get_authorization_header(request).split()

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
        except (TypeError, ValueError, UnicodeDecodeError, binascii.Error) as esc:
            msg = _("Invalid basic header. Credentials not correctly base64 encoded.")
            log.debug(msg)
            raise PermissionDenied(msg) from esc

        return self.authenticate_credentials(userid, password, request)

    def authenticate_credentials(
        self, userid, password, request=None
    ) -> tuple[AbstractUser, None] | None:
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
        return f'Basic realm="{self.www_authenticate_realm}"'

    @staticmethod
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
