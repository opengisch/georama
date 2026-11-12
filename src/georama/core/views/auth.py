from allauth.socialaccount.adapter import get_adapter
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.views import LoginView, LogoutView, redirect_to_login
from django.http import HttpResponseNotAllowed
from django.urls import reverse


class Login(LoginView):
    """The login page of Georama. It shows the local username/password form and one
    button per configured identity provider.

    With `LOGIN_LOCAL_FORM_ENABLED` switched off, the page only shows the provider
    buttons and refuses the local login. It never locks everybody out though: as long
    as no provider exists, the local form stays.
    """

    template_name = "core/login.html"
    next_page = "core:index"

    def get_context_data(self, **kwargs):
        """Adds the decision about the local form, so the template doesn't need to
        know how it is made.

        Args:
            **kwargs: The keyword arguments django passes through.

        Returns:
            The context of the login page including `local_form_enabled`.
        """
        context = super().get_context_data(**kwargs)
        context["local_form_enabled"] = self.local_form_enabled()
        return context

    def post(self, request, *args, **kwargs):
        """Handles the submitted local form. If the local form is disabled, the view
        answers with 405, so the setting really disables the local login on this page
        instead of only hiding the form.

        Args:
            request: The django request.
            *args: The positional arguments django passes through.
            **kwargs: The keyword arguments django passes through.

        Returns:
            The response of the django login view or 405 if the local form is disabled.
        """
        if not self.local_form_enabled():
            return HttpResponseNotAllowed(["GET"])
        return super().post(request, *args, **kwargs)

    def local_form_enabled(self) -> bool:
        """Decides if the local form is offered. The setting wins, unless there is no
        identity provider at all, then the local form is the only way in and stays.

        Returns:
            True if the local form is offered on the login page.
        """
        if settings.LOGIN_LOCAL_FORM_ENABLED:
            return True
        # without any identity provider the local form is the only way in, so we keep it
        return not get_adapter(self.request).list_providers(self.request)


class AdminLogin(Login):
    """The admin login of django, put under the same rule as the login page. Otherwise
    it would be an open back door for passwords as soon as the local form is switched
    off.

    It borrows the decision from `Login`, so both pages always agree on whether a local
    password is accepted.
    """

    def dispatch(self, request, *args, **kwargs):
        """Hands the request to the admin login as long as the local form is offered,
        otherwise the admin is sent to the login page of Georama. The admin keeps the
        page they wanted to reach, so after the provider login they end up there.

        Args:
            request: The django request.
            *args: The positional arguments django passes through.
            **kwargs: The keyword arguments django passes through.

        Returns:
            The response of the admin login or a redirect to the login page.
        """
        if self.local_form_enabled():
            return admin.site.login(request)
        return redirect_to_login(
            request.GET.get(REDIRECT_FIELD_NAME, reverse("admin:index")), "core:login"
        )


class Logout(LogoutView):
    next_page = "core:index"
