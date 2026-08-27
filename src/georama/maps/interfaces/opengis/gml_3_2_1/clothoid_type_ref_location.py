from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.affine_placement import AffinePlacement

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ClothoidTypeRefLocation:
    class Meta:
        global_type = False

    affine_placement: AffinePlacement | None = field(
        default=None,
        metadata={
            "name": "AffinePlacement",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
