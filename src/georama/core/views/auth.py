from django.contrib.auth.views import LoginView, LogoutView


class Login(LoginView):
    template_name = "core/login.html"
    next_page = "core:index"


class Logout(LogoutView):
    next_page = "core:index"
