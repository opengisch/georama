from allauth.mfa.utils import is_mfa_enabled
from allauth.socialaccount.models import SocialAccount
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect

MFA_ENROLLMENT_URL = "/accounts/2fa/"
EXEMPT_URLS = [
    "/accounts/",
    "/static/",
    "/i18n/",
]


class MFAEnforcementMiddleware:
    """Redirect staff/superusers to MFA enrollment if they haven't set it up.

    This middleware checks authenticated staff and superuser requests. If the
    user has no MFA device enrolled and did not authenticate via a social
    (OIDC) provider, they are redirected to the MFA enrollment page.

    Users authenticated via a linked SocialAccount (e.g. Keycloak OIDC) are
    exempt because their identity provider is trusted to handle its own MFA.

    This middleware MUST be listed after:

    - django.contrib.auth.middleware.AuthenticationMiddleware
    - allauth.account.middleware.AccountMiddleware
    - georama.core.auth.middleware.GeoGirafeAuthenticationMiddleware
    """

    def __init__(self, get_response):
        """Initialize the middleware.

        Args:
            get_response: The callable from the next middleware in the chain.
        """
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        """Check MFA enrollment for staff/superuser requests.

        If the user is staff or superuser, has no MFA device, did not
        authenticate via a social account, and is not requesting an exempt
        URL, redirect them to the MFA enrollment page.

        Args:
            request: The incoming Django request.

        Returns:
            A redirect response to MFA enrollment or the normal response.
        """
        if (
            request.user.is_authenticated
            and (request.user.is_staff or request.user.is_superuser)
            and not is_mfa_enabled(request.user)
            and not self._authenticated_via_social(request.user)
            and not any(request.path.startswith(url) for url in EXEMPT_URLS)
        ):
            return redirect(MFA_ENROLLMENT_URL)
        return self.get_response(request)

    def _authenticated_via_social(self, user) -> bool:
        """Check if the user has a linked social account.

        Args:
            user: The authenticated user instance.

        Returns:
            True if the user has at least one linked SocialAccount.
        """
        return SocialAccount.objects.filter(user=user).exists()
