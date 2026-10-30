import json

import pytest
from rest_framework.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR


class TestPygeoapiServerSchema:
    url = "/features/api"

    @pytest.mark.django_db
    @pytest.mark.parametrize(
        "geometry_type_wkb, expected_format",
        [
            ("Point", "geometry-point"),
            ("PointZ", "geometry-point"),
            ("Point25D", "geometry-point"),
            ("LineStringM", "geometry-linestring"),
            ("Polygon", "geometry-polygon"),
            ("TriangleZ", "geometry-polygon"),
            ("MultiPoint", "geometry-multipoint"),
            ("MultiLineStringZM", "geometry-multilinestring"),
            ("MultiPolygon25D", "geometry-multipolygon"),
            ("GeometryCollection", "geometry-geometrycollection"),
        ],
    )
    def test_succeeds_rewrites_geometry_format(
        self,
        client,
        global_vector_dataset,
        global_feature_layer_public,
        geometry_type_wkb,
        expected_format,
    ):
        global_vector_dataset.geometry_type_wkb = geometry_type_wkb
        global_vector_dataset.save()
        response = client.get(
            f"{self.url}/collections/{global_feature_layer_public.identifier}/schema?f=json"
        )
        assert response.status_code == HTTP_200_OK
        response = json.loads(response.content)
        assert response["properties"]["geometry"]["format"] == expected_format

    @pytest.mark.django_db
    @pytest.mark.parametrize(
        "geometry_type_wkb",
        [
            "Unknown",
            "NoGeometry",
            "CircularString",
            "CompoundCurveZ",
            "CurvePolygonM",
            "MultiCurve",
            "MultiSurfaceZM",
            "PolyhedralSurface",
            "TIN",
            "point",
        ],
    )
    def test_fails_on_unsupported_geometry_type(
        self, client, global_vector_dataset, global_feature_layer_public, geometry_type_wkb
    ):
        global_vector_dataset.geometry_type_wkb = geometry_type_wkb
        global_vector_dataset.save()
        response = client.get(
            f"{self.url}/collections/{global_feature_layer_public.identifier}/schema?f=json"
        )
        assert response.status_code == HTTP_500_INTERNAL_SERVER_ERROR
        response = json.loads(response.content)
        assert f"'{geometry_type_wkb}'" in response["description"]
