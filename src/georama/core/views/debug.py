import os
from django.http import HttpResponse
from django.conf import settings


def host_headers(request):
    # application load balancers in cloud providers may not expose easy ways to inspect incoming request headers,
    # so we provide this simple endpoint to return all incoming headers in plain text for quick debugging.
    lines = [f"{key}: {value}" for key, value in sorted(request.headers.items())]

    if not lines:
        lines.append("<no headers>")

    lines.append(f"absolute_uri_dummy: {request.build_absolute_uri('dummy.html')}")

    lines.append(f"DJANGO_CONFIGURATION: {os.environ.get('DJANGO_CONFIGURATION')}")
    lines.append(f"SECURE_PROXY_SSL_HEADER: {settings.SECURE_PROXY_SSL_HEADER}")

    return HttpResponse("\n".join(lines), content_type="text/plain")