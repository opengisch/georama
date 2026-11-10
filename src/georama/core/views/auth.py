from allauth.socialaccount.adapter import get_adapter
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseNotAllowed


class Login(LoginView):
    template_name = "core/login.html"
    next_page = "core:index"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["local_form_enabled"] = self.local_form_enabled()
        return context

    def post(self, request, *args, **kwargs):
        if not self.local_form_enabled():
            return HttpResponseNotAllowed(["GET"])
        return super().post(request, *args, **kwargs)

    def local_form_enabled(self) -> bool:
        if settings.LOGIN_LOCAL_FORM_ENABLED:
            return True
        # without any identity provider the local form is the only way in, so we keep it
        return not get_adapter(self.request).list_providers(self.request)


class Logout(LogoutView):
    next_page = "core:index"
