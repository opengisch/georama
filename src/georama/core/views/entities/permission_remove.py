import json

from django.contrib.auth.models import Group, Permission, User
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.views import View


class GeoramaRemovePermissionToUserOrGroup(View):

    def post(self, request: HttpRequest):
        data = json.load(request)
        principal_id = data["principal_id"]
        permission_ids = data["permission_ids"]
        principal_type = data["principal_type"]
        permissions = Permission.objects.filter(pk__in=permission_ids).all()
        if principal_type == "user":
            user = User.objects.filter(pk=principal_id).get()
            user.user_permissions.remove(*permissions)
            return HttpResponse("OK")
        elif principal_type == "group":
            group = Group.objects.filter(pk=principal_id).get()
            group.permissions.remove(*permissions)
            return HttpResponse("OK")
        return HttpResponseBadRequest()
