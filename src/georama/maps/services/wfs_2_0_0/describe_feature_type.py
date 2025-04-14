import re
import logging
from functools import lru_cache
from typing import List
from xsdata.formats.dataclass.serializers import JsonSerializer, XmlSerializer
from xsdata.formats.dataclass.parsers import DictDecoder
from xsdata.models.xsd import ComplexType, ComplexContent, Extension, Sequence, Element, Schema

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.wfs.pkg_2.describe_feature_type import \
    DescribeFeatureType
from georama.maps.maps_config import Config
from georama.maps.models import PublishedAsWms
from georama.maps.services.wfs_2_0_0 import WfsOperation


@lru_cache(maxsize=None)
class ConvertDBTypesToXML:
    pg_to_xml_map = {
        # Numeric types
        'smallint': 'xs:short',
        'integer': 'xs:int',
        'bigint': 'xs:long',
        'decimal': 'xs:decimal',
        'numeric': 'xs:decimal',
        'real': 'xs:float',
        'double precision': 'xs:double',
        'money': 'xs:decimal',

        # Character types
        'character varying': 'xs:string',
        'varchar': 'xs:string',
        'character': 'xs:string',
        'char': 'xs:string',
        'text': 'xs:string',
        'string': 'xs:string',
        'citext': 'xs:string',

        # Boolean type
        'boolean': 'xs:boolean',

        # Date/time types
        'date': 'xs:date',
        'timestamp': 'xs:dateTime',
        'timestamp without time zone': 'xs:dateTime',
        'timestamp with time zone': 'xs:dateTime',
        'time': 'xs:time',
        'time without time zone': 'xs:time',
        'time with time zone': 'xs:time',
        'interval': 'xs:duration',

        # Binary types
        'bytea': 'xs:base64Binary',

        # UUID
        'uuid': 'xs:string',

        # JSON types
        'json': 'xs:string',  # or 'xs:anyType' for flexibility
        'jsonb': 'xs:string',

        # XML
        'xml': 'xs:string',

        # Network types
        'inet': 'xs:string',
        'cidr': 'xs:string',
        'macaddr': 'xs:string',
        'macaddr8': 'xs:string',

        # Enumerated type
        'enum': 'xs:string',  # can be customized per enum

        # Arrays (map base types, you can detect `_int4`, `_text`, etc.)
        '_int4': 'xs:int',  # integer[]
        '_text': 'xs:string',  # text[]
        '_varchar': 'xs:string',  # varchar[]
        '_bool': 'xs:boolean',  # boolean[]
        '_uuid': 'xs:string',  # uuid[]
        '_float8': 'xs:double',  # double precision[]
        '_numeric': 'xs:decimal',  # numeric[]

        # PostGIS types (GML or xs:string fallback)
        'geometry': 'gml:GeometryPropertyType',
        'geography': 'gml:GeometryPropertyType',
        'point': 'gml:PointPropertyType',
        'linestring': 'gml:LineStringPropertyType',
        'polygon': 'gml:PolygonPropertyType',
        'multipoint': 'gml:MultiPointPropertyType',
        'multilinestring': 'gml:MultiLineStringPropertyType',
        'multipolygon': 'gml:MultiPolygonPropertyType',
        'geometrycollection': 'gml:GeometryCollectionPropertyType',

        # Rasters (could also be GML, or left out if unsupported)
        'raster': 'xs:base64Binary',

        # Range types (stored as string or special representation)
        'int4range': 'xs:string',
        'numrange': 'xs:string',
        'tsrange': 'xs:string',
        'tstzrange': 'xs:string',
        'daterange': 'xs:string',

        # Others
        'name': 'xs:string',
        'oid': 'xs:unsignedLong',
        'regclass': 'xs:string',
        'regtype': 'xs:string',
    }

    @lru_cache(maxsize=None)
    def remove_trailing_numbers(self, s:str) -> str:
        return re.sub(r'\d+$', '', s)

    @lru_cache(maxsize=None)
    def convert(self, db_type:str) -> str:
        print(db_type)
        return self.pg_to_xml_map[self.remove_trailing_numbers(db_type.lower())]

class WfsDescribeFeatureType(WfsOperation):
    @property
    def allowed_formats(self) -> List[str]:
        return ["TEXT/XML", "APPLICATION/JSON"]



    def describe_feature_type(self, layer_name: str) -> Schema | None:
        print("layer_name", layer_name)
        found_layers = self.obtain_accessible_layers([layer_name])
        print(type(found_layers))
        found_layer = found_layers[0]
        print(type(found_layer))

        converter = ConvertDBTypesToXML()

        dft = Schema()

        for layer in found_layers:
            if found_layer.vector_dataset:
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print(found_layer.vector_dataset.name)



                # el = Element(
                #     name=f'{found_layer.name}',
                #     type=f'georama:{found_layer.name}Type',
                #     substitution_group="gml:AbstractFeature"
                # )

                cplxtype = ComplexType(
                    name=f'{layer.name}Type',
                    complex_content=ComplexContent(
                        extension=Extension(
                            base="gml:AbstractFeatureType",
                            sequence=Sequence(
                                elements=[

                                ]
                            )
                        )
                    )
                )

                for column in layer.vector_dataset.fields.all():
                    xml_type = converter.convert(column.type)
                    el = Element(
                        name=column.name,
                        type=xml_type,
                        min_occurs=0,
                        max_occurs=1
                        # Typemapping, type, minouccurs, etc
                    )
                    cplxtype.complex_content.extension.sequence.elements.append(el)

                dft.complex_types = [cplxtype]
            return dft

    @staticmethod
    def render_xml(described_feature_type) -> str:
        serializer = XmlSerializer()
        return serializer.render(
            described_feature_type,
            ns_map={
                "wfs": "http://www.opengis.net/wfs/2.0",
                "xlink": "http://www.w3.org/1999/xlink",
                "fes": "http://www.opengis.net/fes/2.0",
                "ows": "http://www.opengis.net/ows/1.1",
                "xsi": "http://www.w3.org/2001/XMLSchema-instance",
            },
        )

    @staticmethod
    def render_json(described_feature_type) -> str:
        serializer = JsonSerializer()
        return serializer.render(described_feature_type)

    def render(self, requested_format: str, described_feature_type) -> str | None:
        if requested_format == "TEXT/XML":
            return self.render_xml(described_feature_type)
        elif requested_format == "APPLICATION/JSON":
            return self.render_json(described_feature_type)
        else:
            logging.debug("No matching Format was found.")
            return None