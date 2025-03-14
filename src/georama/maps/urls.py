from django.urls import path

from georama.maps import views

urlpatterns = [
    path("", views.global_aggregated, name="wms_entry"),
    path("/<str:mandant>", views.global_mandant_aggregated, name="wms_entry_mandant"),
    path(
        "/<str:mandant>/<str:project>",
        views.global_mandant_and_project_aggregated,
        name="wms_entry_mandant_and_project",
    ),
    path(
        "/publish_as/wms/raster/<str:dataset_id>",
        views.admin_publish_raster_as_wms,
        name="publish_raster_as_wms",
    ),
    path(
        "/publish_as/wms/vector/<str:dataset_id>",
        views.admin_publish_vector_as_wms,
        name="publish_vector_as_wms",
    ),
    path(
        "/publish_as/wms/custom/<str:dataset_id>",
        views.admin_publish_custom_as_wms,
        name="publish_custom_as_wms",
    ),
]
