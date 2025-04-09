from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.transformation_type import (
    TransformationType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Transformation(TransformationType):
    """Gml:Transformation is a concrete object element derived from
    gml:GeneralTransformation (13.6.2.13).

    This concrete object can be used for all operation methods, without
    using a GML Application Schema that defines operation-method-
    specialized element names and contents, especially for methods with
    only one Transformation instance. The parameterValue elements are an
    unordered list of composition associations to the set of parameter
    values used by this conversion operation.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
