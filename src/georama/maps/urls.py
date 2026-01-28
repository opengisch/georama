from django.urls import path

from georama.maps import views
from georama.maps.apps import central_app_label

app_name = central_app_label

urlpatterns = [
    path("/ows", views.OgcServer.as_view(), name="maps_ogc_entry"),
    path(
        "/layers/<str:dataset_type>/<str:dataset_id>/publish",
        views.publish_dataset_as_wms,
        name="publish",
    ),
    path(
        "/",
        views.Index.as_view(),
        name="index",
    ),
    path(
        "/layers/publish",
        views.Publish.as_view(),
        name=views.Publish.name,
    ),
    path(
        "/layers/<str:pk>",
        views.PublishedAsWmsFormView.as_view(),
        name=views.PublishedAsWmsFormView.name,
    ),
]
