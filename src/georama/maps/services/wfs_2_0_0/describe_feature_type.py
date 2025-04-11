import logging
from typing import List
from xsdata.formats.dataclass.serializers import JsonSerializer, XmlSerializer
from xsdata.formats.dataclass.parsers import DictDecoder
from xsdata.models.xsd import ComplexType, ComplexContent, Extension, Sequence, Element, Schema

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.wfs.pkg_2.describe_feature_type import \
    DescribeFeatureType
from georama.maps.maps_config import Config
from georama.maps.models import PublishedAsWms
from georama.maps.services.wfs_2_0_0 import WfsOperation


class WfsDescribeFeatureType(WfsOperation):
    @property
    def allowed_formats(self) -> List[str]:
        return ["TEXT/XML", "APPLICATION/JSON"]



    def describe_feature_type(self, layer_name: str) -> Schema | None:
        found_layer = self.obtain_accessible_layers([layer_name])[0]
        print(type(found_layer))

        if found_layer.vector_dataset:
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(found_layer.vector_dataset.name)

            dft = Schema(
                
            )

            el = Element(
                name=f'{found_layer.name}',
                type=f'georama:{found_layer.name}Type',
                substitution_group="gml:AbstractFeature"
            )
            cplxtype = ComplexType(
                name=f'{found_layer.name}Type',
                complex_content=ComplexContent(
                    extension=Extension(
                        base="gml:AbstractFeatureType",
                        sequence=Sequence(
                            elements=[
                                Element(
                                    name=found_layer.vector_dataset.name,
                                    type="type",
                                    min_occurs=0,
                                    max_occurs=1
                                    # Typemapping, type, minouccurs, etc
                                )
                            ]
                        )
                    )
                )
            )
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