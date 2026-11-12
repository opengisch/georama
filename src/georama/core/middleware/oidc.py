import logging
import time

import jwt
import requests
from allauth.account.adapter import get_adapter as get_account_adapter
from allauth.socialaccount.models import SocialAccount
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ImproperlyConfigured, PermissionDenied
from django.db import transaction
from django.http import HttpRequest
from django.urls import reverse

from georama.core.middleware.authentication import MiddlewareAuthentication

logger = logging.getLogger(__name__)


class GeoGirafeAuthenticationMiddleware:
    """Authentication middleware for OIDC authentication of GeoGirafe requests.

    This middleware allows to authenticate a user based on an OIDC Access token
    that is passed in the `Authorization` header.

    This middleware MUST be listed after these:

    - django.contrib.auth.middleware.AuthenticationMiddleware
    - allauth.account.middleware.AccountMiddleware
    - django.contrib.messages.middleware.MessageMiddleware

    It is only loaded when `OIDC_SERVER_URL` is configured. It looks for an Access
    token in the Authorization header, extracts it, and then validates the token
    against the public key of the provider. The user is set for this request only, a
    token never turns into a session.

    Attributes:
        oidc_config: The provider's configuration, loaded with the first token and
            then kept, since we consider it static.
        jwks_client: PyJWKClient caches keys automatically and handles key rotation on provider
            side, so we create one with the configuration and use its cache.
        get_response: This is a callable, since middlewares are chained callables this callable
            some not reliably specified callable of the middleware active before this dedicated
            one. Only thing we have to do here, is to call it and pass the response as arg.
    """

    # what happens when the provider's username already exists locally
    username_conflict_modes = ("suffix", "connect")

    def __init__(self, get_response):
        """The middleware is instantiated once at server start. Nothing is fetched from
        the provider here, an unreachable provider must not keep Georama from starting.

        Args:
            get_response: The callable in from the previously loaded middleware in the chain.
        """
        if settings.OIDC_USERNAME_CONFLICT not in self.username_conflict_modes:
            raise ImproperlyConfigured(
                f"GEORAMA_OIDC_USERNAME_CONFLICT must be one of "
                f"{', '.join(self.username_conflict_modes)}."
            )
        self.get_response = get_response
        self.oidc_config = None
        self.jwks_client = None
        self.provider_retry_at = 0.0

    def __call__(self, request: HttpRequest):
        """Detect and extract HTTP headers intended for OIDC auth.

        Because this code gets called for *every* single request, we need to
        be quite defensive here. For reasons of performance and robustness.

        We need to abort as early as possible if we can determine that the
        request is not intended for OIDC auth. And we must not cause any
        unhandled exceptions that could interfere with normal requests.

        Args:
            request: The django request which is intercepted
        """
        if request.path_info == reverse("core:health"):
            # the health has no user, touching request.user would load the session from
            # the database, which might be down
            return self.get_response(request)

        if request.user.is_authenticated:
            # User already has a session
            return self.get_response(request)

        access_token = self.get_access_token(request)
        if not access_token:
            # No token found, nothing for us to do
            return self.get_response(request)

        if not self.load_provider():
            # the token can't be checked right now, the request goes on as anonymous
            return self.get_response(request)

        try:
            payload = self.verify_token(access_token)
            user = self.get_or_create_user(payload)
        except Exception as e:  # noqa: BLE001
            logger.debug(f"Bearer token refused: {e}")
            return self.get_response(request)

        if not user.is_active:
            logger.info(f"Deactivated user {user.username} sent a bearer token, refused.")
            return self.get_response(request)
        if user.is_superuser and not settings.GEOGIRAFE_SUPERUSER_ENABLED:
            # a token lives in the browser of GeoGirafe, by default it must not carry
            # superuser rights
            logger.warning(
                f"Superuser {user.username} sent a bearer token, refused. "
                f"Use a non superuser account in GeoGirafe."
            )
            return self.get_response(request)

        # for this request only, no session: the next request brings its token again
        request.user = user
        setattr(request, MiddlewareAuthentication.request_flag, True)
        return self.get_response(request)

    def load_provider(self) -> bool:
        """Loads the provider's configuration and signing keys client, once. If the
        provider can't be reached, we log it and try again after a while.

        Returns:
            True if tokens can be checked.
        """
        if self.jwks_client is not None:
            return True
        if time.monotonic() < self.provider_retry_at:
            return False
        try:
            response = requests.get(settings.OIDC_SERVER_URL, timeout=settings.OIDC_TIMEOUT_SECONDS)
            response.raise_for_status()
            self.oidc_config = response.json()
            self.jwks_client = jwt.PyJWKClient(
                self.oidc_config["jwks_uri"], timeout=settings.OIDC_TIMEOUT_SECONDS
            )
        except (requests.RequestException, ValueError, KeyError) as e:
            self.provider_retry_at = time.monotonic() + settings.OIDC_RETRY_SECONDS
            logger.warning(
                f"Identity provider {settings.OIDC_SERVER_URL} not reachable, bearer tokens "
                f"are refused for the next {settings.OIDC_RETRY_SECONDS} seconds: {e}"
            )
            return False
        return True

    def create_user_via_allauth(self, payload: dict):
        """Creates a new user and links it to the socialaccount django-allauth ecosystem.

        Args:
            payload: The decoded token.

        Returns:
            The newly created user object.
        """
        User = get_user_model()  # noqa: N806

        user = self.local_user_to_connect(payload) or User(
            # the preferred username might be taken by a local account already, then
            # allauth appends a number
            username=get_account_adapter().generate_unique_username(
                [payload.get("preferred_username"), payload.get("email"), "user"]
            ),
            email=payload.get("email") or "",
            first_name=payload.get("given_name") or "",
            last_name=payload.get("family_name") or "",
        )
        with transaction.atomic():
            if user._state.adding:
                user.save()
            SocialAccount.objects.create(
                user=user,
                provider=settings.OIDC_PROVIDER_ID,
                uid=payload["sub"],
                extra_data=payload,
            )

        return user

    @staticmethod
    def local_user_to_connect(payload: dict):
        """Finds the local account with the provider's username, when the setting says
        both are the same person.

        Args:
            payload: The decoded token.

        Returns:
            The local user to connect or None.
        """
        if settings.OIDC_USERNAME_CONFLICT != "connect" or not payload.get("preferred_username"):
            return None
        return get_user_model().objects.filter(username=payload["preferred_username"]).first()

    def get_or_create_user(self, payload: dict):
        """Tries to find user in socialaccount django-allauth system or initiates
        creation of new user if none was found.

        Args:
            payload: The decoded token dict.

        Returns:
            The found or freshly created user.
        """
        try:
            social = SocialAccount.objects.select_related("user").get(
                provider=settings.OIDC_PROVIDER_ID,
                uid=payload["sub"],
            )
            user = social.user
        except SocialAccount.DoesNotExist:
            user = self.create_user_via_allauth(payload)
        return user

    def get_access_token(self, request: HttpRequest) -> str | None:
        """Extracts token from the request header.

        Args:
            request: The django request

        Returns:
            The key string or None if no token or token does not match expectations.
        """
        auth_header = request.headers.get("Authorization")

        if not (auth_header and auth_header.startswith("Bearer ")):
            return None

        id_token = auth_header.split(" ")[1]
        return id_token

    def verify_token(self, token) -> dict:
        """Decodes and the token and verify it against the public key of the
        configured provider.

        Args:
            token: The token encoded body.

        Returns:
            The decoded and verified token (basically a dict)

        Raises:
            PermissionDenied: In case a token is expired, or invalid in other means.
        """
        # This receives the public key from the provider. Be aware that a cache is
        # in place here which is implemented in jwt.PyJWKClient. We could expose
        # settings some day maybe, currently we go with default settings.
        signing_key = self.jwks_client.get_signing_key_from_jwt(token)
        try:
            # This step decodes AND validates the token. In this case:
            #   - audience (aud)
            #   - client-id (azp)
            #   - issuer (iss)
            #   - expire (exp)
            # More validation might be added when necessary.
            payload = jwt.decode(
                token,
                signing_key.key,
                algorithms=["RS256"],
                audience=settings.OIDC_CLIENT_ID,
                issuer=self.oidc_config["issuer"],
            )
            # the audience alone doesn't tell which client the token was issued to
            if payload.get("azp") != settings.OIDC_CLIENT_ID:
                raise jwt.InvalidTokenError("Token was not issued to this client")
            return payload
        except jwt.ExpiredSignatureError as e:
            raise PermissionDenied("Token expired") from e
        except jwt.InvalidTokenError as e:
            raise PermissionDenied("Invalid token") from e
