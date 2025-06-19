from django.apps import AppConfig


class GeoramaAbstractConfig(AppConfig):
    name = None

    @classmethod
    def get_simple_appname(cls) -> str | None:
        if cls.name is not None:
            return cls.name.split(".")[-1]
        else:
            return None


class CoreConfig(GeoramaAbstractConfig):
    default_auto_field = "django.db.models.BigAutoField"
    verbose_name = "Core"
    name = "georama.core"
