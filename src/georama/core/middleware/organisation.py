import logging

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext as _

from georama.core.models import Membership, Organisation


class OrganisationMiddleware:
    """Resolves the organisation of a request from its host and enforces access.

    The organisation is stored on ``request.georama_organisation`` (``None`` for
    the global organisation). Unless access is public, the user must be
    authenticated and a member of the organisation; superusers are always allowed.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path_info.startswith(settings.STATIC_URL):
            # we don't want to handle static URLS at all
            return self.get_response(request)

        if request.path_info == reverse("core:health"):
            # probes and humans need the health also when the database is down, so no
            # organisation lookup and no user, not configurable on purpose
            request.georama_organisation = None
            return self.get_response(request)

        organisation, public_access = self.resolve_organisation(request)
        request.georama_organisation = organisation

        if public_access or request.user.is_superuser or self.is_open_path(request):
            # Membership not required
            return self.get_response(request)

        if not request.user.is_authenticated:
            logging.debug("User was not authenticated, forwarding to login")
            return redirect(reverse(settings.ORGANISATION_NOT_AUTHENTICATED_TARGET))

        try:
            membership: Membership = request.user.memberships.get(organisation=organisation)
        except Membership.DoesNotExist as exc:
            logging.debug(
                "User %s has no membership of the requested organisation %s",
                request.user,
                organisation,
            )
            raise PermissionDenied() from exc

        if not membership.is_active:
            logging.debug(
                "User %s has an inactive membership in the requested organisation %s",
                request.user,
                organisation,
            )
            raise PermissionDenied(
                _(
                    "Your membership of this organisation is not active. "
                    "An administrator needs to approve it."
                )
            )

        return self.get_response(request)

    def resolve_organisation(self, request) -> tuple[Organisation | None, bool]:
        """Returns the organisation for the request host and whether it is publicly accessible.

        The organisation is None for the global organisation. Raises Http404 if
        the subdomain matches no organisation.
        """
        # lowercase first so "WWW." is handled too, then remove the www prefix
        host = self.remove_www(request.get_host().lower())
        # deriving subdomains which distinguish the organisation
        subdomains = self.derive_subdomain(host, settings.ORGANISATION_DOMAIN)
        if subdomains is None:
            logging.debug("Request for global organisation")
            return None, settings.ORGANISATION_GLOBAL_PUBLIC_ACCESS
        try:
            organisation = Organisation.objects.get(domain=subdomains)
        except Organisation.DoesNotExist:
            logging.debug(f"Organisation not found in database. Domain: {subdomains}")
            # raised instead of returned, so django renders its 404 page
            raise Http404(_("Organisation not found")) from None
        return organisation, organisation.public_access

    @staticmethod
    def is_open_path(request) -> bool:
        """Returns whether the path is reachable without membership."""
        path = request.path_info
        if path in (
            reverse(settings.ORGANISATION_NOT_AUTHENTICATED_TARGET),
            # local accounts always need a way in, also when the login page has no local form
            reverse("admin:login"),
            # logged in non-members must be able to leave
            reverse("account_logout"),
            *(reverse(name) for name in settings.ORGANISATION_MEMBERSHIP_EXEMPT_VIEWS),
        ):
            return True
        # allauth flows (OIDC login, callback, ...) for anonymous users only
        return not request.user.is_authenticated and path.startswith("/accounts/oidc/")

    @staticmethod
    def derive_subdomain(hostname: str, domain: str) -> str | None:
        """Returns the organisation subdomain of hostname (port ignored).

        Returns None, meaning the global organisation, if hostname is the bare
        domain or does not belong to domain at all.
        """
        hostname = hostname.rsplit(":", 1)[0].lower().rstrip(".")
        domain = domain.lower().strip(".")
        logging.debug(f"Original hostname: {hostname}, configured domain: {domain}")
        if hostname == domain:
            return None
        suffix = f".{domain}"
        if not hostname.endswith(suffix):
            # Fall back to the global organisation for a unknown host suffix
            # Could happen if the current host is in ALLOWED_HOSTS but different
            # from ORGANISATION_DOMAIN
            return None
        subdomains = hostname.removesuffix(suffix)
        logging.debug(f"Cleaned subdomains: {subdomains}")
        return subdomains

    @staticmethod
    def remove_www(hostname: str) -> str:
        """Removes www. from the beginning of the address. Only for
        routing purposes. www.test.com/login/ and test.com/login/ should
        find the same tenant.
        """
        if hostname.startswith("www."):
            return hostname[4:]
        return hostname
