from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_feature_type import (
    AbstractFeatureType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractFeature(AbstractFeatureType):
    """This abstract element serves as the head of a substitution group which may
    contain any elements whose content model is derived from
    gml:AbstractFeatureType.

    This may be used as a variable in the construction of content
    models. gml:AbstractFeature may be thought of as "anything that is a
    GML feature" and may be used to define variables or templates in
    which the value of a GML property is "any feature". This occurs in
    particular in a GML feature collection where the feature member
    properties contain one or multiple copies of gml:AbstractFeature
    respectively.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
