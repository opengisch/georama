from django.apps import AppConfig

appname = "webgis"


class ClogsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = f"georama.{appname}"
