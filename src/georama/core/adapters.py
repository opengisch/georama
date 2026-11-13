import logging

from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.internal.flows.manage_email import assess_unique_email
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.conf import settings

logger = logging.getLogger(__name__)


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

    def is_auto_signup_allowed(self, request, sociallogin) -> bool:
        """Leaves the decision to allauth, but tells the operator when allauth won't
        create the user automatically because a local account already has the email of
        the provider. The user then lands on the signup form and has to enter another
        email, without the log nobody would guess why.

        Args:
            request: The django request.
            sociallogin: The login allauth is about to finish.

        Returns:
            allauth's decision.
        """
        allowed = super().is_auto_signup_allowed(request, sociallogin)
        for address in sociallogin.email_addresses[:1]:
            # the same check allauth does next, internal but the only way to know it
            if assess_unique_email(address.email) is not True:
                logger.warning(
                    f"Provider login of {sociallogin.account.provider} user "
                    f"{sociallogin.account.uid} with email {address.email}: a local account "
                    f"already uses this email, so the user is asked to complete the signup "
                    f"with another email. To sign such users into the local account, see "
                    f"GEORAMA_OIDC_EMAIL_AUTHENTICATION (the provider must mark the email "
                    f"as verified)."
                )
        return allowed
