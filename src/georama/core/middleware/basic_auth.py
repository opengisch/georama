import base64
import binascii
import logging

from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest, HttpResponse
from django.utils.translation import gettext_lazy as _

from georama.core.common.login_attempts import LoginAttempts, TooManyLoginAttemptsError
from georama.core.middleware.authentication import MiddlewareAuthentication

# Header encoding (see RFC5987)
HTTP_HEADER_ENCODING = "iso-8859-1"

log = logging.getLogger(__name__)


class BasicAuthenticationMiddleware:
    """HTTP Basic authentication against username/password."""

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
                    # the REST framework takes the user over from here
                    setattr(request, MiddlewareAuthentication.request_flag, True)
            except TooManyLoginAttemptsError:
                log.debug(_("Too many failed login attempts."))
                return HttpResponse("Too Many Requests", status=429)
            except PermissionDenied:
                # AuthenticationFailed: there was a http auth header,
                # but auth failed: consider the user unlogged.
                log.debug(_("User was not authenticated."))
                return self.unauthorized_response(request)
            except Exception as e:  # noqa: BLE001
                log.error(e)
        return self.get_response(request)

    def unauthorized_response(self, request: HttpRequest) -> HttpResponse:
        """The 401 with the challenge, the same for every reason a login failed.

        Args:
            request: The django request.

        Returns:
            The 401 response.
        """
        response = HttpResponse("Unauthorized", status=401)
        # without the challenge clients don't know they may ask for credentials again
        response["WWW-Authenticate"] = self.authenticate_header(request)
        return response

    def authenticate(self, request) -> tuple[AbstractUser, None] | None:
        """Returns a `User` if a correct username and password have been supplied
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
        """Authenticate the userid and password against username and password
        with optional request for context.
        """
        if LoginAttempts.blocked(request, userid):
            raise TooManyLoginAttemptsError

        credentials = {get_user_model().USERNAME_FIELD: userid, "password": password}
        user = authenticate(request=request, **credentials)

        if user is None:
            LoginAttempts.count_failure(request, userid)
            msg = _("Invalid username/password.")
            log.debug(msg)
            raise PermissionDenied(msg)

        if not user.is_active:
            LoginAttempts.count_failure(request, userid)
            msg = _("User inactive or deleted.")
            log.debug(msg)
            raise PermissionDenied(msg)

        if user.is_superuser:
            # counted like a wrong password, otherwise the count would tell a guesser
            # when the password of a superuser was right
            LoginAttempts.count_failure(request, userid)
            log.warning(
                _("Superuser %s tried basic authentication, use a non superuser account."),
                userid,
            )
            raise PermissionDenied(_("Invalid username/password."))

        return user, None

    def authenticate_header(self, request):
        """Builds the challenge of the 401, it names Georama as the protection space.

        Args:
            request: The django request.

        Returns:
            The value of the WWW-Authenticate header.
        """
        # the realm names the protection space, clients keep their credentials per realm
        realm = settings.SITE_TITLE.replace("\\", "\\\\").replace('"', '\\"')
        return f'Basic realm="{realm}"'

    @staticmethod
    def get_authorization_header(request: HttpRequest):
        """Return request's 'Authorization:' header, as a bytestring.

        Hide some test client ickyness where the header can be unicode.
        """
        auth = request.META.get("HTTP_AUTHORIZATION", b"")
        if isinstance(auth, str):
            # Work around django test client oddness
            auth = auth.encode(HTTP_HEADER_ENCODING)
        return auth
