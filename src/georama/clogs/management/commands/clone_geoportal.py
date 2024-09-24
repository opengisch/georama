import json
import logging

from xsdata.formats.dataclass.parsers import DictDecoder
from xsdata.formats.dataclass.parsers.config import ParserConfig

import requests
from django.core.management.base import BaseCommand
from django.db import transaction

from georama.clogs import models
from georama.clogs.interfaces.geomapfish import load_geoportal_config_from_url
from georama.clogs.interfaces.geomapfish.themes_json_2_8.dataclasses import (
    ThemesJson, OgcServer, LinkedLayer, Attribute, Themes
)


def import_layergroups(children, new_theme=None, parent_node=None):
    # List of theme's related layer groups, or layer groups related layer groups...
    for child in children:
        # First level
        if new_theme:
            # TODO: don't create duplicates
            group = models.LayerGroupMp.add_root(name=child["name"])
            new_theme.layergroupmp.add(group)
        # Other levels
        if parent_node:
            # TODO: don't create duplicates
            group = parent_node.add_child(name=child["name"])

            if "layers" in child:
                layer = models.Layer.objects.create(
                    name=child["name"],
                )
                layer.layergroupmp.add(group)
                if child["type"] == "WMS":
                    models.LayerWms.objects.create(
                        layer=layer,
                        ogc_server=models.OgcServer.objects.first(),
                    )

                if "metadata" in child:
                    for key, value in child["metadata"].items():
                        metadata = models.Metadata.objects.create(
                            name=key,
                            value=value,
                        )
                        layer.metadata.add(metadata)

        if len(child.keys()) > 1:
            for key, value in child.items():
                if key == "children":
                    import_layergroups(value, parent_node=group)


def import_ogc_servers(data):

    models.OgcServer.objects.all().delete()
    for key, value in data.items():
        models.OgcServer.objects.get_or_create(
            name=key,
            # description = data[key]["description"],
            url=data[key]["url"],
            url_wfs=data[key]["urlWfs"],
            type=data[key]["type"],
            image_type=data[key]["imageType"],
            # auth = data[key]["auth"],
            wfs_support=data[key]["wfsSupport"],
            is_single_tile=data[key]["isSingleTile"],
            attributes=data[key]["attributes"],
        )


def clone_geoportal(url):

    models.Theme.objects.all().delete()
    models.LayerGroupMp.objects.all().delete()
    models.Layer.objects.all().delete()
    models.LayerWms.objects.all().delete()
    r = requests.get(url)
    data = json.loads(r.content)

    import_ogc_servers(data["ogcServers"])

    for theme in data["themes"]:
        new_theme = models.Theme.objects.create(
            name=theme["name"],
            icon=theme["icon"],
            ordering=1,
            public=True,
        )
        print(f'...Importing theme: {theme["name"]}...')
        if "metadata" in theme:
            for key, value in theme["metadata"].items():
                metadata = models.Metadata.objects.create(
                    name=key,
                    value=value,
                )
                new_theme.metadata.add(metadata)

        import_layergroups(theme["children"], new_theme)


class Command(BaseCommand):
    help = "Import configuration from themes.json data"

    def add_arguments(self, parser):
        parser.add_argument("geoportal_url", type=str)

    @transaction.atomic
    def handle(self, *args, **options):

        geoportal_url = options["geoportal_url"]

        load_geoportal(geoportal_url)

        print(f"👥 import themes from {geoportal_url}!")
