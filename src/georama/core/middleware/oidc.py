import logging

import jwt
import requests
from allauth.socialaccount.adapter import get_adapter
from allauth.socialaccount.models import SocialAccount
from django.conf import settings
from django.contrib.auth import get_user_model, login
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest

logger = logging.getLogger(__name__)


class GeoGirafeAuthenticationMiddleware:
    """Authentication middleware for OIDC authentication of GeoGirafe requests.

    This middleware allows to authenticate a user based on an OIDC Access token
    that is passed in the `Authorization` header.

    This middleware MUST be listed after these:

    - django.contrib.auth.middleware.AuthenticationMiddleware
    - allauth.account.middleware.AccountMiddleware
    - django.contrib.messages.middleware.MessageMiddleware

    This middleware looks for an Access token in the Authorization header, extracts
    it, and then validates the token against the public key of the provider.

    Attributes:
        oidc_config: We only load that info once at server start
            (when this class is instantiated) since we consider it static.
        jwks_client: PyJWKClient caches keys automatically and handles key rotation on provider
            side, so we create one at server start too and use its cache.
        get_response: This is a callable, since middlewares are chained callables this callable
            some not reliably specified callable of the middleware active before this dedicated
            one. Only thing we have to do here, is to call it and pass the response as arg.
    """

    def __init__(self, get_response):
        """The middleware is instantiated once at server start.

        Args:
            get_response: The callable in from the previously loaded middleware in the chain.
        """
        self.get_response = get_response
        # we only set attributes if the URL is available through config actually, it turns
        # out we have problems with tests otherwise, since this class is instantiated
        # always.
        if settings.OIDC_SERVER_URL:
            self.oidc_config = requests.get(settings.OIDC_SERVER_URL).json()
            self.jwks_client = jwt.PyJWKClient(self.oidc_config["jwks_uri"])

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
        if request.user.is_authenticated:
            # User already has a session
            return self.get_response(request)

        access_token = self.get_access_token(request)
        if not access_token:
            # No token found, nothing for us to do
            return self.get_response(request)

        try:
            payload = self.verify_token(access_token)
        except Exception:
            return self.get_response(request)

        user = self.get_or_create_user(payload)
        # login the user and assign a session cookie
        # so on subsequent requests request.user.is_authenticated is
        # True already.
        login(request, user)

        return self.get_response(request)

    def create_user_via_allauth(self, payload: dict):
        """Creates a new user and links it to the socialaccount django-allauth ecosystem.

        Args:
            payload: The decoded token.

        Returns:
            The newly created user object.
        """
        adapter = get_adapter()
        User = get_user_model()

        user = User(
            username=payload["preferred_username"],
            email=payload.get("email"),
            first_name=payload.get("given_name"),
            last_name=payload.get("family_name"),
        )

        adapter.populate_user(None, user, payload)
        user.save()

        social_account = SocialAccount(
            user=user,
            provider=settings.OIDC_PROVIDER_ID,
            uid=payload["sub"],
            extra_data=payload,
        )
        social_account.save()

        return user

    def get_or_create_user(self, payload: dict):
        """Tries to find user in socialaccount django-allauth system or initiates
        creation of new user if none was found.

        Args:
            payload: The decoded token dict.

        Returns:
            The found or freshly created user.
        """
        try:
            social = SocialAccount.objects.get(
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
            return jwt.decode(
                token,
                signing_key.key,
                algorithms=["RS256"],
                audience=settings.OIDC_CLIENT_ID,
                issuer=self.oidc_config["issuer"],
            )
        except jwt.ExpiredSignatureError as e:
            raise PermissionDenied("Token expired") from e
        except jwt.InvalidTokenError as e:
            raise PermissionDenied("Invalid token") from e
