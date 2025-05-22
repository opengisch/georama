import logging
from typing import List, Tuple

from xsdata.formats.dataclass.serializers import JsonSerializer, XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.xsd import (
    ComplexContent,
    ComplexType,
    Element,
    Extension,
    Import,
    Schema,
    Sequence,
)

from georama.data_integration.models import VectorDataSet
from georama.maps.models import PublishedAsWms
from georama.maps.services.wfs_2_0_0 import WfsOperation


class WfsDescribeFeatureType(WfsOperation):
    @property
    def allowed_formats(self) -> List[str]:
        return [
            "APPLICATION/GML+XML; VERSION=3.2",
            "TEXT/XML",
            "APPLICATION/JSON",
            "TEXT/JSON",
        ]

    def obtain_accessible_layers(self, layer_names: List[str] | None = None):
        accessible_layers = []
        # we do want only published vector datasets!
        query = PublishedAsWms.objects.exclude(vector_dataset__isnull=True)
        if layer_names:
            query = query.filter(name__in=layer_names)
        for published_as in query:
            if published_as.has_read_permission(self.user, self.appname):
                accessible_layers.append(published_as)
        return accessible_layers

    def prepare_geometry_column(self, dataset: VectorDataSet):
        if dataset.geometry_type_wkb in ["Point", "Point25D"]:
            column_type = "gml:PointPropertyType"
        elif dataset.geometry_type_wkb in ["LineString", "LineString25D"]:
            column_type = "gml:LineStringPropertyType"
        elif dataset.geometry_type_wkb in ["Polygon", "Polygon25D"]:
            column_type = "gml:PolygonPropertyType"
        elif dataset.geometry_type_wkb in ["MultiPoint", "MultiPoint25D"]:
            column_type = "gml:MultiPointPropertyType"
        elif dataset.geometry_type_wkb in [
            "MultiCurve",
            "MultiLineString",
            "MultiLineString25D",
        ]:
            column_type = "gml:MultiCurvePropertyType"
        elif dataset.geometry_type_wkb in ["MultiSurface", "MultiPolygon", "MultiPolygon25D"]:
            column_type = "gml:MultiSurfacePropertyType"
        else:
            logging.debug(
                f"We casted to generic type since no match was available for type: '{dataset.geometry_type_wkb}'"
            )
            column_type = "gml:GeometryPropertyType"
        return Element(
            name=f"{self.own_namespace}:geometry",
            type=column_type,
            min_occurs=0,
            max_occurs=1,
            # TODO: Find out how to set this!
            # alias="Geometry"
        )

    def describe_feature_type(self, type_names: List[str] | None) -> Schema | None:
        # typename is a comma separated list
        if type_names:
            found_layers = self.obtain_accessible_layers(self.sanitized_typenames(type_names))
        else:
            found_layers = self.obtain_accessible_layers()

        dft = Schema(
            imports=[
                Import(
                    schema_location="http://schemas.opengis.net/gml/2.1.2/feature.xsd",
                    namespace="http://www.opengis.net/gml",
                )
            ]
        )

        for layer in found_layers:
            dft.elements.append(
                Element(
                    name=f"{self.own_namespace}:{layer.name}",
                    type=f"{self.own_namespace}:{layer.name}Type",
                    substitution_group="gml:AbstractFeature",
                )
            )
            complex_type = ComplexType(
                name=f"{self.own_namespace}:{layer.name}Type",
                complex_content=ComplexContent(
                    extension=Extension(
                        base="gml:AbstractFeatureType",
                        sequence=Sequence(
                            elements=[
                                # we can directly go for the vector dataset here since we checked it already
                                self.prepare_geometry_column(layer.vector_dataset)
                            ]
                        ),
                    )
                ),
            )
            dft.complex_types.append(complex_type)

            for column in layer.vector_dataset.fields.all():
                el = Element(
                    name=f"{self.own_namespace}:{column.name}",
                    type=column.type_simple,
                    min_occurs=0 if column.nullable else 1,
                    max_occurs=1,
                    nillable=column.nullable
                    # TODO: Find out how to set this!
                    # alias=column.alias
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
    ) -> Tuple[str, str, bool]:
        if requested_format == "TEXT/XML":
            return self.render_xml(described_feature_type), requested_format.lower(), True
        elif requested_format == "APPLICATION/GML+XML; VERSION=3.2":
            return self.render_xml(described_feature_type), requested_format.lower(), True
        elif requested_format == "APPLICATION/JSON":
            return self.render_json(described_feature_type), requested_format.lower(), True
        elif requested_format == "TEXT/JSON":
            return self.render_json(described_feature_type), requested_format.lower(), True
        else:
            logging.debug("No matching Format was found.")
            return (
                self.render_operation_parsing_failed(
                    f"Format {requested_format} is not allowed. Allowed is {self.allowed_formats}"
                ),
                "text/xml",
                False,
            )
