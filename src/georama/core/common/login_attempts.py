import logging
from collections.abc import Callable

from allauth.core.internal import ratelimit
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpRequest, HttpResponse
from django.utils.translation import gettext_lazy as _

from georama.core.exceptions.base import GeoramaBaseError

log = logging.getLogger(__name__)


class TooManyLoginAttemptsError(GeoramaBaseError):
    """Raised when a username failed to log in too often in a short time."""


class LoginAttempts:
    """Counts failed password logins with the rate limits of allauth, so every way a
    password reaches Georama (login page, admin login, HTTP Basic) shares one counter
    per username with allauth's own login page.

    allauth's public helper skips GET requests, but HTTP Basic authentication mostly
    arrives as GET (GetMap, GetFeature), so the internal one is used on purpose.
    """

    app = "allauth.account"
    action = "login_failed"

    @classmethod
    def blocked(cls, request: HttpRequest, username: str) -> bool:
        """Asks without counting, so we know before checking a password whether it is
        worth checking at all.

        Args:
            request: The django request.
            username: The username the client tries to log in with.

        Returns:
            True if the username reached the limit.
        """
        return not cls.consume(request, username, dry_run=True)

    @classmethod
    def count_failure(cls, request: HttpRequest, username: str) -> None:
        """Counts one failed login and tells the operator once the limit is reached.

        Args:
            request: The django request.
            username: The username of the failed login.
        """
        cls.consume(request, username, dry_run=False)
        if cls.blocked(request, username):
            # once when the limit is reached, so the reason for a refused login is
            # in the log but blocked requests don't flood it
            log.warning(
                _(
                    "Too many failed login attempts for %s, blocked for up to %s minutes. "
                    "Remote address: %s, X-Forwarded-For: %r"
                ),
                username,
                settings.LOGIN_ATTEMPTS_BLOCKED_MINUTES,
                request.META.get("REMOTE_ADDR"),
                request.headers.get("X-Forwarded-For"),
            )

    @classmethod
    def guard(
        cls, request: HttpRequest, username: str, login: Callable[[], HttpResponse]
    ) -> HttpResponse:
        """Wraps a login view: a blocked username gets the 429 page, a login which ends
        without a logged in user is counted.

        Args:
            request: The django request.
            username: The username sent with the form.
            login: The login view, ready to be called.

        Returns:
            The response of the login view or the 429 page.
        """
        if cls.blocked(request, username):
            return ratelimit.respond_429(request)
        response = login()
        if not request.user.is_authenticated:
            cls.count_failure(request, username)
        return response

    @classmethod
    def consume(cls, request: HttpRequest, username: str, dry_run: bool) -> bool:
        """Hands the attempt to allauth's rate limiting, with Georama's rate.

        Args:
            request: The django request.
            username: The username of the attempt.
            dry_run: Only look, don't count.

        Returns:
            True if the attempt is still within the limit.
        """
        usage = ratelimit.consume(
            request,
            app=cls.app,
            action=cls.action,
            config={cls.action: settings.LOGIN_ATTEMPTS_RATE},
            key=cls.key(request, username),
            limit_get=True,
            dry_run=dry_run,
        )
        return usage is not None

    @staticmethod
    def key(request: HttpRequest, username: str) -> str:
        # same key as allauth's own login, so both count into the same history
        return f"{get_current_site(request).domain}:{username.lower()}"
