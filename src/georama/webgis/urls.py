from adrf.routers import DefaultRouter, SimpleRouter
from django.urls import include, path

from georama.webgis.api.viewsets import ManageThemeViewSet, ThemeViewSet

app_name = "webgis"

management_router = SimpleRouter()
management_router.register(r"themes", ManageThemeViewSet, basename="theme-manager")

router = DefaultRouter()
router.register(r"themes", ThemeViewSet, basename="theme")

urlpatterns = [
    path("", include(router.urls)),
    path("manage/", include(management_router.urls)),
]
