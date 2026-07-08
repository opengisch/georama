import logging

from guardian.shortcuts import get_objects_for_user
from xsdata.formats.dataclass.serializers import JsonSerializer, XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.enums import FormType
from xsdata.models.xsd import (
    ComplexContent,
    ComplexType,
    Element,
    Extension,
    Import,
    Schema,
    Sequence,
)

from georama.integration.models import Vector
from georama.integration.models.datasource import VectorField
from georama.maps.services.wfs_2_0_0 import WfsOperation


class WfsDescribeFeatureType(WfsOperation):
    @property
    def allowed_formats(self) -> list[str]:
        return [
            "APPLICATION/GML+XML; VERSION=3.2",
            "GML3TEXT/XML",
            "APPLICATION/JSON",
            "TEXT/JSON",
        ]

    def obtain_accessible_layers(self, layer_names: list[str] | None = None):
        return get_objects_for_user(self.user, ["view_wmslayer"], self.model).filter(
            datasource__vector__isnull=False
        )

    def prepare_geometry_column(self, datasource: Vector):
        if datasource.geometry_type_wkb in ["Point", "Point25D"]:
            column_type = "gml:PointPropertyType"
        elif datasource.geometry_type_wkb in ["LineString", "LineString25D"]:
            column_type = "gml:LineStringPropertyType"
        elif datasource.geometry_type_wkb in ["Polygon", "Polygon25D"]:
            column_type = "gml:PolygonPropertyType"
        elif datasource.geometry_type_wkb in ["MultiPoint", "MultiPoint25D"]:
            column_type = "gml:MultiPointPropertyType"
        elif datasource.geometry_type_wkb in [
            "MultiCurve",
            "MultiLineString",
            "MultiLineString25D",
        ]:
            column_type = "gml:MultiCurvePropertyType"
        elif datasource.geometry_type_wkb in ["MultiSurface", "MultiPolygon", "MultiPolygon25D"]:
            column_type = "gml:MultiSurfacePropertyType"
        else:
            logging.debug(
                f"We casted to generic type since no match was"
                f" available for type: '{datasource.geometry_type_wkb}'"
            )
            column_type = "gml:GeometryPropertyType"
        return Element(
            name="geometry",
            type=column_type,
            min_occurs=0,
            max_occurs=1,
            # TODO: Find out how to set this!
            # alias="Geometry"
        )

    def describe_feature_type(self, type_names: list[str] | None) -> Schema | None:
        # typename is a comma separated list
        if type_names:
            found_layers = self.obtain_accessible_layers(self.sanitized_typenames(type_names))
        else:
            found_layers = self.obtain_accessible_layers()
        logging.debug(found_layers)
        dft = Schema(
            imports=[
                Import(
                    schema_location="http://schemas.opengis.net/gml/3.2.1/gml.xsd",
                    namespace="http://www.opengis.net/gml/3.2",
                )
            ],
            target_namespace="https://www.opengis.ch/georama",
            element_form_default=FormType.QUALIFIED,
            version="0.1",
        )

        for layer in found_layers:
            dft.elements.append(
                Element(
                    name=f"{layer.name}",
                    type=f"{self.own_namespace}:{layer.name}Type",
                    substitution_group="gml:AbstractFeature",
                )
            )
            complex_type = ComplexType(
                name=f"{layer.name}Type",
                complex_content=ComplexContent(
                    extension=Extension(
                        base="gml:AbstractFeatureType",
                        sequence=Sequence(
                            elements=[
                                # we can directly go for the vector datasource here
                                # since we checked it already
                                self.prepare_geometry_column(layer.datasource.vector)
                            ]
                        ),
                    )
                ),
            )
            dft.complex_types.append(complex_type)

            for field in layer.datasource.vector.fields.all():
                field: VectorField
                el = Element(
                    name=f"{field.name}",
                    # we do not prefix this with namespace, because http://www.w3.org/2001/XMLSchema
                    # is the default namespace
                    type=field.type_wfs,
                    min_occurs=0 if field.nullable else 1,
                    max_occurs=1,
                    nillable=field.nullable,
                    # TODO: Find out how to set this!
                    # alias=field.alias
                )
                complex_type.complex_content.extension.sequence.elements.append(el)
        return dft

    def render_xml(self, described_feature_type) -> str:
        serializer = XmlSerializer(
            config=SerializerConfig(
                xml_declaration=True, xml_version="1.0", ignore_default_attributes=True
            )
        )
        return serializer.render(
            described_feature_type,
            ns_map={
                "wfs": "http://www.opengis.net/wfs/2.0",
                "xlink": "http://www.w3.org/1999/xlink",
                "fes": "http://www.opengis.net/fes/2.0",
                "ows": "http://www.opengis.net/ows/1.1",
                "xsi": "http://www.w3.org/2001/XMLSchema-instance",
                "georama": "https://www.opengis.ch/georama",
                "gml": "http://www.opengis.net/gml/3.2",
                # make this the default namespace, to avoid confusion in xml responses
                "": "http://www.w3.org/2001/XMLSchema",
            },
        )

    @staticmethod
    def render_json(described_feature_type) -> str:
        serializer = JsonSerializer(
            SerializerConfig(ignore_default_attributes=True, pretty_print=True)
        )
        return serializer.render(described_feature_type)

    def render(
        self, requested_format: str, described_feature_type: Schema
    ) -> tuple[str, str, bool]:
        if requested_format == "TEXT/XML" or requested_format == "APPLICATION/GML+XML; VERSION=3.2":
            return self.render_xml(described_feature_type), requested_format.lower(), True
        elif requested_format == "GML3":
            return (
                self.render_xml(described_feature_type),
                "APPLICATION/GML+XML; VERSION=3.2".lower(),
                True,
            )
        elif requested_format == "APPLICATION/JSON" or requested_format == "TEXT/JSON":
            return self.render_json(described_feature_type), requested_format.lower(), True
        else:
            logging.debug("No matching Format was found.")
            return (
                self.render_operation_parsing_failed(
                    f"Format {requested_format} is not allowed.Allowed is {self.allowed_formats}"
                ),
                "text/xml",
                False,
            )
