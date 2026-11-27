from adrf import routers
from django.urls import include, path
from django.utils.translation import gettext as _
from drf_spectacular import views

from georama.processes.api.viewsets import (
    ConformanceView,
    JobViewSet,
    LandingView,
    ManageJobViewSet,
    ManageProcessInputViewSet,
    ManageProcessViewSet,
    ProcessInputViewSet,
    ProcessViewSet,
)

app_name = "processes"

management_router = routers.SimpleRouter()
management_router.register(r"processes", ManageProcessViewSet, basename="process-manager")
management_router.register(r"jobs", ManageJobViewSet, basename="job-manager")
management_router.register(
    r"process_inputs", ManageProcessInputViewSet, basename="process-input-manager"
)

router = routers.SimpleRouter()
router.register(r"processes", ProcessViewSet, basename="process")
router.register(r"jobs", JobViewSet, basename="job")
router.register(r"process_inputs", ProcessInputViewSet, basename="process-input")

urlpatterns = [
    path("", include(router.urls)),
    path("", LandingView.as_view(), name="api-landing"),
    path("conformance/", ConformanceView.as_view(), name="api-conformance"),
    path("manage/", include(management_router.urls)),
    path(
        "manage/schema/",
        views.SpectacularAPIView.as_view(
            urlconf=management_router.urls,
            custom_settings={
                "TITLE": _("Management API of the Processes app."),
                "SCHEMA_PATH_PREFIX": "",
                "SCHEMA_PATH_PREFIX_INSERT": "processes/manage",
            },
        ),
        name="schema",
    ),
    path(
        "manage/schema/swagger/",
        views.SpectacularSwaggerView.as_view(url_name="processes:schema"),
        name="swagger",
    ),
    path(
        "manage/schema/redoc/",
        views.SpectacularRedocView.as_view(url_name="processes:schema"),
        name="redoc",
    ),
]
