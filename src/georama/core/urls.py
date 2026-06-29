from adrf import routers
from django.urls import include, path

from georama.core.api import views
from georama.core.api.view_sets import (
    FenceViewSet,
    GroupViewSet,
    MembershipViewSet,
    OrganisationViewSet,
    PermissionViewSet,
    UserViewSet,
)
from georama.core.views import auth
from georama.core.views.index import Index

app_name = "core"

management_router = routers.SimpleRouter()
management_router.register(r"users", UserViewSet)
management_router.register(r"groups", GroupViewSet)
management_router.register(r"permissions", PermissionViewSet)
management_router.register(r"organisations", OrganisationViewSet)
management_router.register(r"fences", FenceViewSet)
management_router.register(r"memberships", MembershipViewSet)
urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("login/", auth.Login.as_view(), name="login"),
    path("logout/", auth.Logout.as_view(), name="logout"),
    path("manage/", include(management_router.urls)),
    path(
        "manage/schema/",
        views.GeoramaAdminSchemaView.as_view(urlconf=management_router.urls),
        name="schema",
    ),
    path(
        "manage/schema/swagger-ui/",
        views.GeoramaAdminSwaggerView.as_view(url_name="core:schema"),
        name="swagger",
    ),
    path(
        "manage/schema/redoc/",
        views.GeoramaAdminRedocView.as_view(url_name="core:schema"),
        name="redoc",
    ),
]
