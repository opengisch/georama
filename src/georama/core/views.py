from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.template import RequestContext
from django.template.response import TemplateResponse
from django.contrib.auth import logout
from django.views import View
from django.http import HttpResponse
from georama.core.settings import INSTALLED_APPS
from django.apps import apps


class GeoramaLanding(View):

    # TODO: generate Landing Page depending on the installed georama apps.
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponse("TODO: Landingpage")
        else:
            return redirect('login')


class Login(View):

    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, 'login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('landing')
        else:
            return redirect('login')


class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')
