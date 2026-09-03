from guardian.shortcuts import get_objects_for_user
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from georama.maps.interfaces.ogc.wfs_2_0_0 import Exception as Wfs200Exception
from georama.maps.interfaces.ogc.wfs_2_0_0 import ExceptionReport
from georama.maps.models import WmsLayer
from georama.maps.services import OgcOperation


class WfsOperation(OgcOperation):
    own_namespace = "georama"
    own_namespace_domain = "https://www.opengis.ch/georama"

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

    def sanitized_typenames(self, type_names: list[str]) -> list[str]:
        """
        Method to bridge layer names which are configured in Georama and the
        version which is exposed by WFS containing the namespace.
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
            name_parts = name.split(":")
            if len(name_parts) == 1:
                # no namespace as part of the typename we assume that the
                # requested typename is out
                # of the default namespace self.own_namespace
                sanitized_typenames.append(name_parts[0])
            elif len(name_parts) == 2:
                if self.own_namespace != name_parts[0]:
                    # the requested typename belongs not to our namespace, we do
                    # not support that
                    wrong_typenames.append(name)
                else:
                    # the requested typename belongs to our namespace
                    sanitized_typenames.append(
                        name.replace(f"{self.own_namespace}:", "")
                    )
            else:
                wrong_typenames.append(
                    f"typename has unexpected format (expected '<namespace>:<name>') got {name}"
                )
        if len(wrong_typenames) > 0:
            raise AttributeError(
                self.render_exception(
                    f"Unknown feature type (wrong namespace? this server offers namespace "
                    f"'{self.own_namespace}'):"
                    f" wrongTypeName(s) => {', '.join(wrong_typenames)}"
                )
            )
        return sanitized_typenames

    def obtain_accessible_layers(
        self, layer_names: list[str] | None = None
    ) -> list[WmsLayer]:
        return get_objects_for_user(self.user, ["view_wmslayer"], self.model).filter(
            datasource__vector__isnull=False
        )
