from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.conf import settings


class AccountAdapter(DefaultAccountAdapter):
    """Georama's say in allauth's local accounts. allauth keeps signup open for
    everyone unless somebody tells it otherwise, this is the place where we do.
    """

    def is_open_for_signup(self, request) -> bool:
        """Decides if people may create a local account themselves. Closed unless
        `LOGIN_LOCAL_SIGNUP_ENABLED` is switched on.

        Args:
            request: The django request.

        Returns:
            True if the signup page offers its form.
        """
        return settings.LOGIN_LOCAL_SIGNUP_ENABLED


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    """Georama's say in allauth's accounts coming from an identity provider."""

    def is_open_for_signup(self, request, sociallogin) -> bool:
        """Lets the first login through an identity provider create the user, no matter
        if the local signup is closed.

        Args:
            request: The django request.
            sociallogin: The login allauth is about to finish.

        Returns:
            Always True.
        """
        # allauth asks the account adapter by default, but the identity provider
        # decides who gets in, so the first login there still creates the user
        return True
