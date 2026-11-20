from adrf import routers
from django.urls import include, path

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
]
