from django.urls import include, path

from georama.features import views

urlpatterns = [
    path("", include(views.PygeoapiServer.urls())),
    path(
        "/publish_as/oapif/<str:vector_dataset_id>",
        views.admin_publish_as_oapif,
        name="publish_as_oapif",
    ),
]
