from django.urls import path

from georama.integration.views.index import Index

app_name = "integration"

urlpatterns = [
    path("", Index.as_view()),
]
