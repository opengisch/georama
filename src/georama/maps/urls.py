from django.urls import path

from georama.maps import views

urlpatterns = [
    path("", views.OgcServer.as_view(), name="ogc_entry"),
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
