import logging
from typing import List

from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from georama.data_integration.models import VectorDataSet
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1 import (
    Exception as Wfs200Exception,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1 import ExceptionReport
from georama.maps.models import PublishedAsWms
from georama.maps.services import OgcOperation


class WfsOperation(OgcOperation):
    own_namespace = "georama"

    @staticmethod
    def create_exception(message: str) -> ExceptionReport:
        return ExceptionReport(
            version="2.0.0",
            exception=[
                Wfs200Exception(
                    exception_code="OperationParsingFailed",
                    exception_text=["It was not possible to process the request"],
                    locator="GetFeature",
                ),
                Wfs200Exception(
                    exception_code="InvalidParameterValue", exception_text=[message]
                ),
            ],
        )

    @staticmethod
    def render_exception(message: str) -> str:
        config = SerializerConfig(
            xml_declaration=True,
            xml_version="1.0",
            ignore_default_attributes=True,
            schema_location=" ".join(
                [
                    "http://www.opengis.net/ows/1.1",
                    "http://schemas.opengis.net/ows/1.1.0/owsAll.xsd",
                ]
            ),
        )
        return XmlSerializer(config=config).render(
            WfsOperation.create_exception(message),
            ns_map={
                "": "http://www.opengis.net/ows/1.1",
                "xsi": "http://www.w3.org/2001/XMLSchema-instance",
            },
        )

    def sanitized_typenames(self, type_names: List[str]) -> List[str]:
        """
        Method to bridge layer names which are configured in Georama and the version which is exposed by WFS
        containing the namespace.
        Args:
            type_names: The names which should be sanitized.

        Returns:
            The sanitized names.
        Raises:
            AttributeError: In case namespace is not in all typenames.
        """
        sanitized_typenames = []
        wrong_typenames = []
        for name in type_names:
            if f"{self.own_namespace}:" not in name:
                wrong_typenames.append(name)
            sanitized_typenames.append(name.replace(f"{self.own_namespace}:", ""))
        if len(wrong_typenames) > 0:
            raise AttributeError(
                self.render_exception(
                    f"Unknown feature type (namespace missing? this server offers namespace "
                    f"'{self.own_namespace}'): wrongTypeName(s) => {wrong_typenames}"
                )
            )
        return sanitized_typenames

    def obtain_accessible_layers(
        self, layer_names: List[str] | None = None
    ) -> List[PublishedAsWms]:
        accessible_layers = []
        for published_as in PublishedAsWms.objects.all():
            if (
                published_as.has_read_permission(self.user, self.appname)
                and published_as.queryable
            ):
                if isinstance(published_as.vector_dataset, VectorDataSet):
                    accessible_layers.append(published_as)
                else:
                    logging.debug(
                        "linked dataset has to be VectorDataSet for WFS 2.0.0, all others are ignored!"
                    )
        return accessible_layers
