from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.views import View


class Login(View):
    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, "admin/login.html")

    def post(self, request, *args, **kwargs):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("core:index")
        else:
            return redirect("core:login")


class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("core:index")
