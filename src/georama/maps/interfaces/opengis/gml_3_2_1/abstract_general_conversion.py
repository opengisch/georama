from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.sc_crs_property_type import (
    AbstractGeneralConversionType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractGeneralConversion(AbstractGeneralConversionType):
    """Gm:AbstractGeneralConversion is an abstract operation on coordinates that
    does not include any change of datum.

    The best-known example of a coordinate conversion is a map projection. The parameters describing coordinate conversions are defined rather than empirically derived. Note that some conversions have no parameters. The operationVersion, sourceCRS, and targetCRS elements are omitted in a coordinate conversion.
    This abstract complex type is expected to be extended for well-known operation methods with many Conversion instances, in GML Application Schemas that define operation-method-specialized element names and contents. This conversion uses an operation method, usually with associated parameter values. However, operation methods and parameter values are directly associated with concrete subtypes, not with this abstract type. All concrete types derived from this type shall extend this type to include a "usesMethod" element that references the "OperationMethod" element. Similarly, all concrete types derived from this type shall extend this type to include zero or more elements each named "uses...Value" that each use the type of an element substitutable for the "AbstractGeneralParameterValue" element.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
