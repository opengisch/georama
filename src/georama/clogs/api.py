from ninja import Field, ModelSchema, NinjaAPI, Schema
from ninja.orm.fields import AnyObject
from dataclasses import dataclass, field, fields
from django.db.models import Model

from georama.clogs import models

api = NinjaAPI()


@dataclass
class AbstractSchema:
    # field_mapping: dict
    # django_model_class: Model

    def to_django_model_instance(self):
        raise NotImplementedError
        # TODO: Make a generic mapping function for that
        # dataclass_fields = fields(self)
        # django_model_instance_kwargs = {}
        # for field_name in dataclass_fields:
        #     django_model_instance_kwargs[self.field_mapping[field_name]] = getattr(self, field_name)
        # return self.django_model_class(
        #     **django_model_instance_kwargs
        # )


@dataclass
class OgcServer(AbstractSchema):
    url: str = field(
        metadata={
            "type": "Element",
            "required": False
        }
    )
    type: str = field(
        metadata={
            "type": "Element",
            "required": False
        }
    )
    attributes: dict
    credential: bool = field(
        metadata={
            "type": "Element",
            "required": False
        }
    )
    imageType: str = field(
        metadata={
            "type": "Element",
            "required": False
        }
    )
    wfsSupport: bool = field(
        metadata={
            "type": "Element",
            "required": False
        }
    )
    name: str = field(
        metadata={
            "type": "Element",
            "required": False
        }
    )
    isSingleType: bool = field(
        default=None,
        metadata={
            "type": "Element",
            "required": False
        }
    )
    wfsUrl: str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": False
        }
    )



    namespace: str = field(
        default="",
        metadata={
            "type": "Element",
            "required": False
        }
    )

    def to_django_model_instance(self):
        return models.OgcServer(
            name=self.name,
            type=self.type,
            attributes=self.attributes,
            url_wfs=self.wfsUrl,
            # TODO: Is this the right match?
            url=self.wms,
            # TODO: where to pick this attribute from?
            credential=True,
            image_type=self.imageType,
            wfs_support=self.wfsSupport,
            is_single_tile=self.isSingleType,
            # TODO: Where to pick this attribute value?
            namespace=""
        )



@dataclass
class MetaDataSchema(AbstractSchema):

    name: str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": False
        }
    )
    value: str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": False
        }
    )
    description: str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": False
        }
    )

    def to_django_model_instance(self) -> models.Metadata:
        return models.Metadata(
            name=self.name,
            value=self.value,
            description=self.description
        )


@dataclass
class FunctionalitySchema(AbstractSchema):
    name: str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": False
        }
    )
    value: str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": False
        }
    )
    description: str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": False
        }
    )

    def to_django_model_instance(self) -> models.Metadata:
        return models.Metadata(
            name=self.name,
            value=self.value,
            description=self.description
        )


@dataclass
class InterfaceSchema(AbstractSchema):
    name: str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": False
        }
    )
    description: str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": False
        }
    )

    def to_django_model_instance(self) -> models.Metadata:
        return models.Metadata(
            name=self.name,
            description=self.description
        )


@dataclass
class LayerSchema(AbstractSchema):
    id: int = field(
        metadata={
            "type": "Element",
            "required": False
        }
    )
    name: str = field(
        metadata={
            "type": "Element",
            "required": False
        }
    )
    metadata: dict
    wfsSupport: bool = field(
        default=None,
        metadata={
            "type": "Element",
            "required": False
        }
    )



@dataclass
class LayergroupSchema(AbstractSchema):
    id: int = field(
        metadata={
            "type": "Element",
            "required": False
        }
    )
    name: str = field(
        metadata={
            "type": "Element",
            "required": False
        }
    )
    layers: list[LayerSchema]
    children: list["LayergroupSchema"]


@dataclass
class ThemeSchema(AbstractSchema):
    metadata: list[MetaDataSchema]
    functionality: list[FunctionalitySchema]
    interface: list[InterfaceSchema]





@api.get("/themes")
def themes(request):

    ogcservers: list[models.OgcServer] = models.OgcServer.objects.all()
    ogcservers_dict = {}
    for server in ogcservers:
        ogcservers_dict[server.name] = server.as_dict()
    layergroups_data = [
        LayergroupSchema.from_orm(i).dict()
        for i in LayergroupSchema.from_treebeard_dump(models.LayerGroupMp.dump_bulk())
    ]

    # move layers into children's list to be geogirafe compliant
    # we can't use alias here as the "children" key is already used in Schema
    # FIXME: fix performance leak
    layergroups_data_refactored = []
    for layergroup in layergroups_data:
        if layergroup["layers"]:
            for layer in layergroup["layers"]:
                layergroup["children"].append(layer)
        layergroups_data_refactored.append(layergroup)

    themes = models.Theme.objects.all()
    themes_data = [ThemeSchema.from_orm(i).dict() for i in themes]
    output_themes_data = []
    # Add related groups to themes
    # FIXME: fix performance leak
    for theme in themes_data:
        theme["children"] = []
        for related_group in theme["layergroupmp"]:
            for group in layergroups_data_refactored:
                if group["id"] == related_group:
                    theme["children"].append(group)
        output_themes_data.append(theme)

    return {
        "ogcServers": ogcservers_dict,
        "themes": output_themes_data,
        # TODO: implements optional objects
        "background_layers": [],
        "errors": [],
    }
