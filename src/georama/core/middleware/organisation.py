import logging

from django.conf import settings
from django.http import HttpResponseForbidden, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext as _

from georama.core.models.organisation import Organisation


class OrganisationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (
            request.path_info
            not in [
                reverse(settings.ORGANISATION_NOT_AUTHENTICATED_TARGET),
            ]
            + settings.ORGANISATION_GLOBAL_PUBLIC_ACCESS_BYPASS_TARGETS
        ):
            # removing the maybe existing www part of the domain and getting rid of ports
            hostname = self.remove_www(request.get_host().split(":")[0])
            # deriving subdomains which distinguish the organisation
            subdomains = self.derive_subdomain(hostname, settings.ORGANISATION_DOMAIN)
            if subdomains is None:
                logging.debug("Request for global organisation")
                matched_organisation = None
                public_access = settings.ORGANISATION_GLOBAL_PUBLIC_ACCESS
            else:
                try:
                    logging.debug(f"Request for dedicated organisation. Domain: {subdomains}")
                    matched_organisation = Organisation.objects.get(domain=subdomains)
                    public_access = matched_organisation.public_access
                except Organisation.DoesNotExist:
                    logging.debug(f"Organisation not found in database. Domain: {subdomains}")
                    return HttpResponseNotFound(_("Not found"))
            logging.debug(f"Organisation offers public access: {public_access}")
            superuser = request.user.is_superuser if hasattr(request, "user") else False
            logging.debug(f"Requesting user is superuser: {superuser}")

            if not public_access and not superuser:
                if request.user.is_authenticated:
                    if not any(
                        matched_organisation == membership.organisation
                        for membership in request.user.memberships.all()
                    ):
                        logging.debug("user has no membership of the requested organisation")
                        return HttpResponseForbidden(_("No Access"))
                else:
                    logging.debug(
                        f"User was not authenticated, "
                        f"forwarding to {settings.ORGANISATION_NOT_AUTHENTICATED_TARGET}"
                    )
                    return redirect(reverse(settings.ORGANISATION_NOT_AUTHENTICATED_TARGET))

            request.georama_organisation = matched_organisation
            logging.debug("Organisation middleware passed.")

        response = self.get_response(request)

        return response

    @staticmethod
    def derive_subdomain(hostname: str, domain: str) -> str | None:
        delimiter = "."
        logging.debug(f"Original hostname: {hostname}, configured domain: {domain}")
        subdomains = hostname.replace(domain, "")
        subdomain_parts = subdomains.split(delimiter)[:-1]
        subdomains = delimiter.join(subdomain_parts)
        logging.debug(f"Cleaned subdomains: {subdomains}")
        if subdomains:
            return subdomains
        else:
            return None

    @staticmethod
    def remove_www(hostname: str) -> str:
        """
        Removes www. from the beginning of the address. Only for
        routing purposes. www.test.com/login/ and test.com/login/ should
        find the same tenant.
        """
        if hostname.startswith("www."):
            return hostname[4:]

        return hostname
