from django.urls import path

from georama.qfield_link import views

urlpatterns = [
    path("", views.LinkProjects.as_view(), name="link_projects"),
]
