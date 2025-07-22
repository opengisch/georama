import logging

from allauth.socialaccount.adapter import get_adapter
from allauth.socialaccount.helpers import complete_social_login
from allauth.socialaccount.models import SocialToken
from django.conf import settings
from django.http import HttpRequest

logger = logging.getLogger(__name__)


class GeoGirafeAuthenticationMiddleware:
    """Authentication middleware for OIDC authentication of GeoGirafe requests.

    This middleware allows to authenticate a user based on an OIDC ID token
    that is passed in the `Authorization` header.

    This middleware MUST be listed after these:

    - django.contrib.auth.middleware.AuthenticationMiddleware
    - allauth.account.middleware.AccountMiddleware
    - django.contrib.messages.middleware.MessageMiddleware

    This middleware looks for an ID token in the Authorization header, extracts
    it, and then delegates the actual authentication to django-allauth. Once
    that succeeds, the user is logged in, a session is created, and the session
    is persisted using the standard mechanisms (e.g. a session cookie).

    But because GeoGirafe doesn't send both the token and cookies in its
    requests (only either or, never both), it won't actually use the session.
    Therefore, authentication actually will happen for every single request.
    This is something that should be optimized in the future.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        """Detect and extract HTTP headers intended for OIDC auth.

        Because this code gets called for *every* single request, we need to
        be quite defensive here. For reasons of performance and robustness.

        We need to abort as early as possible if we can determine that the
        request is not intended for OIDC auth. And we must not cause any
        unhandled exceptions that could interfere with normal requests.
        """
        if request.user.is_authenticated:
            # User already has a session
            return self.get_response(request)

        id_token = self.get_id_token(request)
        if not id_token:
            # No token found, nothing for us to do
            return self.get_response(request)

        provider = self.get_provider(request)
        if not provider:
            # Could not determine the provider, bail
            return self.get_response(request)

        # Delegate the actual authentication to django-allauth.
        #
        # We do this by emulating the parameters for django-allauth's
        # OAuth2Adapter.complete_login() method in the way that it expects them.
        #
        # Specifically, a SocialToken instance with either an access or ID token,
        # and a `response` dictionary with the ID token.
        token = SocialToken(token=id_token)
        token_response = {"id_token": id_token}

        # This verifies the token, determines attributes like 'uid' and 'email',
        # and prepares a SocialLogin instance.
        oauth_adapter = provider.get_oauth2_adapter(request)
        social_login = oauth_adapter.complete_login(
            request, provider.app, token, response=token_response
        )

        # This performs signup of the a user, if necessary, authenticates
        # the user, links the social account, and creates a session.
        complete_social_login(request, social_login)

        if settings.DEBUG:
            logger.info("Authenticated user: %s" % request.user)

        return self.get_response(request)

    def get_id_token(self, request: HttpRequest):
        auth_header = request.headers.get("Authorization")

        if not (auth_header and auth_header.startswith("Bearer ")):
            return None

        id_token = auth_header.split(" ")[1]
        return id_token

    def get_provider(self, request: HttpRequest):
        social_account_adapter = get_adapter(request)
        providers = social_account_adapter.list_providers(request)

        if not providers:
            return None

        # We currentls assume that when OIDC is used, there is exactly one
        # socialaccount provider configured. If at some point we have a need
        # to handle multiple providers, we would need to devise a mechanism
        # to signal which provider a token is intended for.
        return providers[0]
