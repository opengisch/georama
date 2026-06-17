import logging

from django.conf import settings
from django.http import HttpResponseForbidden, HttpResponseNotFound

from georama.core.models.organisation import Organisation


class OrganisationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        hostname = self.remove_www(request.get_host().split(":")[0])
        subdomains = self.derive_subdomain(hostname, settings.DOMAIN)
        print(hostname)
        print(subdomains)
        if subdomains is None:
            request.georama_organisation = None
        else:
            try:
                organisation = Organisation.objects.get(domain=subdomains)
            except Organisation.DoesNotExist:
                return HttpResponseNotFound()
            if not organisation.public_access and not request.user.is_authenticated:
                return HttpResponseForbidden()
            request.georama_organisation = organisation

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
