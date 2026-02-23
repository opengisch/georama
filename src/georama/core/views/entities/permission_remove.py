from django.contrib.auth.models import Group, Permission, User
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.views import View


class GeoramaRemovePermissionToUserOrGroup(View):

    def post(self, request: HttpRequest):
        principal_id = request.GET["principal_id"]
        permission_id = request.GET["permission_id"]
        principal_type = request.GET["principal_type"]
        permission = Permission.objects.filter(pk=permission_id).get()
        if principal_type == "user":
            user = User.objects.filter(pk=principal_id).get()
            user.user_permissions.remove(permission)
            return HttpResponse("OK")
        elif principal_type == "group":
            group = Group.objects.filter(pk=principal_id).get()
            group.permissions.remove(permission)
            return HttpResponse("OK")
        return HttpResponseBadRequest()
