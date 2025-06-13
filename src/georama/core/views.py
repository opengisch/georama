from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.templatetags.static import static
from django.views import View
from georama.core import settings


class GeoramaLanding(View):
    def get(self, request, *args, **kwargs):
        logo_url = static("/core/assets/images/georama.coming_soon.png")
        georama_host = settings.GEORAMA_HOST
        return TemplateResponse(request, context={"logo_url": logo_url, "georama_host": georama_host}, template="home.html")


class Login(View):
    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, "login.html")

    def post(self, request, *args, **kwargs):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("landing")
        else:
            return redirect("login")


class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("login")
