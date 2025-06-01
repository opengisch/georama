from django.urls import path

from georama.maps import views

urlpatterns = [
    path("", views.OgcServer.as_view(), name="ogc_entry"),
    path(
        "/publish_as/wms/<str:dataset_type>/<str:dataset_id>",
        views.admin_publish_dataset_as_wms,
        name="maps_publish_dataset_as_wms",
    ),
]
