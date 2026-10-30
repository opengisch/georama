from django.db import models


class UrlShortener(models.Model):
    id = models.CharField(primary_key=True)
    url = models.CharField()
