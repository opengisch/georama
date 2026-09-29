import json
from unittest.mock import patch

import pytest
from rest_framework.status import HTTP_200_OK

from georama.features.models import FeatureLayer


class TestPygeoapiServer:
    url = "/features/api"

    @pytest.mark.django_db
    def test_anonymous_can_access_public_collections_on_spec(
        self, client, global_feature_layer_public, global_feature_layer_nonpublic
    ):
        assert FeatureLayer.objects.count() == 2
        response = client.get(f"{self.url}/openapi?f=json")
        response = json.loads(response.content)
        assert f"/collections/{global_feature_layer_public.identifier}" in response["paths"]
        assert f"/collections/{global_feature_layer_nonpublic.identifier}" not in response["paths"]

    @pytest.mark.django_db
    def test_permitted_user_can_access_permitted_collections_on_spec(
        self,
        client,
        global_feature_layer_public,
        global_feature_layer_nonpublic,
        user_with_membership_global_feature_layer_view_permission,
    ):
        assert FeatureLayer.objects.count() == 2
        client.force_login(user_with_membership_global_feature_layer_view_permission)
        response = client.get(f"{self.url}/openapi?f=json")
        response = json.loads(response.content)
        assert f"/collections/{global_feature_layer_public.identifier}" in response["paths"]
        assert f"/collections/{global_feature_layer_nonpublic.identifier}" in response["paths"]

    @pytest.mark.django_db
    def test_anonymous_can_list_public_public_collections(
        self, client, global_feature_layer_public, global_feature_layer_nonpublic
    ):
        assert FeatureLayer.objects.count() == 2
        response = client.get(f"{self.url}/collections?f=json")
        response = json.loads(response.content)
        assert len(response["collections"]) == 1
        assert response["collections"][0]["id"] == global_feature_layer_public.identifier

    @pytest.mark.django_db
    def test_permitted_user_list_nonpublic_public_collections(
        self,
        client,
        global_feature_layer_public,
        global_feature_layer_nonpublic,
        user_with_membership_global_feature_layer_view_permission,
    ):
        assert FeatureLayer.objects.count() == 2
        client.force_login(user_with_membership_global_feature_layer_view_permission)
        response = client.get(f"{self.url}/collections?f=json")
        response = json.loads(response.content)
        assert len(response["collections"]) == 2

    @pytest.mark.django_db
    def test_anonymous_can_view_detail_public_collection(
        self, client, global_feature_layer_public, global_feature_layer_nonpublic
    ):
        assert FeatureLayer.objects.count() == 2
        response = client.get(
            f"{self.url}/collections/{global_feature_layer_public.identifier}?f=json"
        )
        assert response.status_code == HTTP_200_OK
        response = json.loads(response.content)
        assert response["id"] == global_feature_layer_public.identifier

    @pytest.mark.django_db
    def test_permitted_user_can_view_detail_nonpublic_collection(
        self,
        client,
        global_feature_layer_public,
        global_feature_layer_nonpublic,
        user_with_membership_global_feature_layer_view_permission,
    ):
        assert FeatureLayer.objects.count() == 2
        client.force_login(user_with_membership_global_feature_layer_view_permission)
        response = client.get(
            f"{self.url}/collections/{global_feature_layer_public.identifier}?f=json"
        )
        assert response.status_code == HTTP_200_OK
        response = json.loads(response.content)
        assert response["id"] == global_feature_layer_public.identifier

        response = client.get(
            f"{self.url}/collections/{global_feature_layer_nonpublic.identifier}?f=json"
        )
        assert response.status_code == HTTP_200_OK
        response = json.loads(response.content)
        assert response["id"] == global_feature_layer_nonpublic.identifier

    @pytest.mark.django_db
    def test_anonymous_can_view_schema_public_collection(
        self, client, global_feature_layer_public, global_feature_layer_nonpublic
    ):
        assert FeatureLayer.objects.count() == 2
        response = client.get(
            f"{self.url}/collections/{global_feature_layer_public.identifier}/schema?f=json"
        )
        assert response.status_code == HTTP_200_OK
        response = json.loads(response.content)
        assert global_feature_layer_public.identifier in response["$id"]

    @pytest.mark.django_db
    def test_permitted_user_can_view_schema_nonpublic_collection(
        self,
        client,
        global_feature_layer_public,
        global_feature_layer_nonpublic,
        user_with_membership_global_feature_layer_view_permission,
    ):
        assert FeatureLayer.objects.count() == 2
        client.force_login(user_with_membership_global_feature_layer_view_permission)
        response = client.get(
            f"{self.url}/collections/{global_feature_layer_public.identifier}/schema?f=json"
        )
        assert response.status_code == HTTP_200_OK
        response = json.loads(response.content)
        assert global_feature_layer_public.identifier in response["$id"]

        response = client.get(
            f"{self.url}/collections/{global_feature_layer_nonpublic.identifier}/schema?f=json"
        )
        assert response.status_code == HTTP_200_OK
        response = json.loads(response.content)
        assert global_feature_layer_nonpublic.identifier in response["$id"]

    @pytest.mark.django_db
    def test_anonymous_can_view_queryables_public_collection(
        self, client, global_feature_layer_public, global_feature_layer_nonpublic
    ):
        assert FeatureLayer.objects.count() == 2
        response = client.get(
            f"{self.url}/collections/{global_feature_layer_public.identifier}/queryables?f=json"
        )
        assert response.status_code == HTTP_200_OK
        response = json.loads(response.content)
        assert global_feature_layer_public.identifier in response["$id"]

    @pytest.mark.django_db
    def test_permitted_user_can_view_queryables_nonpublic_collection(
        self,
        client,
        global_feature_layer_public,
        global_feature_layer_nonpublic,
        user_with_membership_global_feature_layer_view_permission,
    ):
        assert FeatureLayer.objects.count() == 2
        client.force_login(user_with_membership_global_feature_layer_view_permission)
        response = client.get(
            f"{self.url}/collections/{global_feature_layer_public.identifier}/queryables?f=json"
        )
        assert response.status_code == HTTP_200_OK
        response = json.loads(response.content)
        assert global_feature_layer_public.identifier in response["$id"]

        response = client.get(
            f"{self.url}/collections/{global_feature_layer_nonpublic.identifier}/queryables?f=json"
        )
        assert response.status_code == HTTP_200_OK
        response = json.loads(response.content)
        assert global_feature_layer_nonpublic.identifier in response["$id"]

    @pytest.mark.django_db
    def test_anonymous_can_view_items_public_collection(
        self, client, global_feature_layer_public, global_feature_layer_nonpublic
    ):
        assert FeatureLayer.objects.count() == 2
        response = client.get(
            f"{self.url}/collections/{global_feature_layer_public.identifier}/items?f=json"
        )
        assert response.status_code == HTTP_200_OK
        json.loads(response.content)

    @pytest.mark.django_db
    def test_permitted_user_can_view_items_nonpublic_collection(
        self,
        client,
        global_feature_layer_public,
        global_feature_layer_nonpublic,
        user_with_membership_global_feature_layer_view_permission,
    ):
        assert FeatureLayer.objects.count() == 2
        client.force_login(user_with_membership_global_feature_layer_view_permission)
        response = client.get(
            f"{self.url}/collections/{global_feature_layer_public.identifier}/items?f=json"
        )
        assert response.status_code == HTTP_200_OK
        json.loads(response.content)

        response = client.get(
            f"{self.url}/collections/{global_feature_layer_nonpublic.identifier}/items?f=json"
        )
        assert response.status_code == HTTP_200_OK
        json.loads(response.content)

    @pytest.mark.django_db
    def test_anonymous_can_view_item_details_public_collection(
        self, client, global_feature_layer_public, global_feature_layer_nonpublic
    ):
        assert FeatureLayer.objects.count() == 2
        response = client.get(
            f"{self.url}/collections/{global_feature_layer_public.identifier}/items?f=json"
        )
        assert response.status_code == HTTP_200_OK
        items = json.loads(response.content)
        test_item_id = items["features"][0]["id"]
        response = client.get(
            f"{self.url}/collections/{global_feature_layer_public.identifier}/items/{test_item_id}?f=json"
        )
        assert response.status_code == HTTP_200_OK
        item = json.loads(response.content)
        assert test_item_id == item["id"]

    @pytest.mark.django_db
    def test_permitted_user_can_view_item_details_nonpublic_collection(
        self,
        client,
        global_feature_layer_public,
        global_feature_layer_nonpublic,
        user_with_membership_global_feature_layer_view_permission,
    ):
        assert FeatureLayer.objects.count() == 2
        client.force_login(user_with_membership_global_feature_layer_view_permission)
        response = client.get(
            f"{self.url}/collections/{global_feature_layer_public.identifier}/items?f=json"
        )
        assert response.status_code == HTTP_200_OK
        items = json.loads(response.content)
        test_item_id = items["features"][0]["id"]
        response = client.get(
            f"{self.url}/collections/{global_feature_layer_public.identifier}/items/{test_item_id}?f=json"
        )
        assert response.status_code == HTTP_200_OK
        item = json.loads(response.content)
        assert test_item_id == item["id"]

        response = client.get(
            f"{self.url}/collections/{global_feature_layer_nonpublic.identifier}/items?f=json"
        )
        assert response.status_code == HTTP_200_OK
        items = json.loads(response.content)
        test_item_id = items["features"][0]["id"]
        response = client.get(
            f"{self.url}/collections/{global_feature_layer_nonpublic.identifier}/items/{test_item_id}?f=json"
        )
        assert response.status_code == HTTP_200_OK
        item = json.loads(response.content)
        assert test_item_id == item["id"]

    @pytest.mark.django_db
    def test_anonymous_correct_options_public_collection_items(
        self, client, global_feature_layer_public
    ):
        assert FeatureLayer.objects.count() == 1
        response = client.options(
            f"{self.url}/collections/{global_feature_layer_public.identifier}/items?f=json"
        )
        assert response.status_code == HTTP_200_OK
        assert response.headers["Allow"] == "HEAD, GET"

    @pytest.mark.django_db
    def test_permitted_user_correct_options_nonpublic_collection_items(
        self,
        client,
        global_feature_layer_nonpublic,
        user_with_membership_global_feature_layer_view_permission,
    ):
        assert FeatureLayer.objects.count() == 1
        client.force_login(user_with_membership_global_feature_layer_view_permission)
        response = client.options(
            f"{self.url}/collections/{global_feature_layer_nonpublic.identifier}/items?f=json"
        )
        assert response.status_code == HTTP_200_OK
        assert response.headers["Allow"] == "HEAD, GET"

    @pytest.mark.django_db
    def test_permitted_user_allowed_edit_options_nonpublic_collection_items(
        self,
        client,
        global_feature_layer_nonpublic,
        user_with_membership_global_feature_layer_create_permission,
    ):
        assert FeatureLayer.objects.count() == 1
        client.force_login(user_with_membership_global_feature_layer_create_permission)
        response = client.options(
            f"{self.url}/collections/{global_feature_layer_nonpublic.identifier}/items?f=json"
        )
        assert response.status_code == HTTP_200_OK
        assert response.headers["Allow"] == "HEAD, GET, POST"

    @pytest.mark.django_db
    def test_anonymous_correct_options_public_collection_item_details(
        self, client, global_feature_layer_public
    ):
        assert FeatureLayer.objects.count() == 1
        response = client.get(
            f"{self.url}/collections/{global_feature_layer_public.identifier}/items?f=json"
        )
        assert response.status_code == HTTP_200_OK
        items = json.loads(response.content)
        test_item_id = items["features"][0]["id"]
        response = client.options(
            f"{self.url}/collections/{global_feature_layer_public.identifier}/items/{test_item_id}?f=json"
        )
        assert response.status_code == HTTP_200_OK
        assert response.headers["Allow"] == "HEAD, GET"

    @pytest.mark.django_db
    def test_permitted_user_correct_options_nonpublic_collection_item_details(
        self,
        client,
        global_feature_layer_nonpublic,
        user_with_membership_global_feature_layer_view_permission,
    ):
        assert FeatureLayer.objects.count() == 1
        client.force_login(user_with_membership_global_feature_layer_view_permission)
        response = client.get(
            f"{self.url}/collections/{global_feature_layer_nonpublic.identifier}/items?f=json"
        )
        assert response.status_code == HTTP_200_OK
        items = json.loads(response.content)
        test_item_id = items["features"][0]["id"]
        response = client.options(
            f"{self.url}/collections/{global_feature_layer_nonpublic.identifier}/items/{test_item_id}?f=json"
        )
        assert response.status_code == HTTP_200_OK
        assert response.headers["Allow"] == "HEAD, GET"

    @pytest.mark.django_db
    def test_permitted_user_allowed_edit_options_nonpublic_collection_item_details(
        self,
        client,
        global_feature_layer_nonpublic,
        user_with_membership_global_feature_layer_create_permission,
    ):
        assert FeatureLayer.objects.count() == 1
        client.force_login(user_with_membership_global_feature_layer_create_permission)
        response = client.get(
            f"{self.url}/collections/{global_feature_layer_nonpublic.identifier}/items?f=json"
        )
        assert response.status_code == HTTP_200_OK
        items = json.loads(response.content)
        test_item_id = items["features"][0]["id"]
        response = client.options(
            f"{self.url}/collections/{global_feature_layer_nonpublic.identifier}/items/{test_item_id}?f=json"
        )
        assert response.status_code == HTTP_200_OK
        assert response.headers["Allow"] == "HEAD, GET, PUT, DELETE"

    @pytest.mark.django_db
    def test_permitted_user_can_create_item(
        self,
        client,
        global_feature_layer_nonpublic,
        user_with_membership_global_feature_layer_create_permission,
    ):
        with patch(
            "pygeoapi.api.itemtypes.manage_collection_item",
            return_value=({}, 200, "application/json"),
        ) as mocked_method:
            assert FeatureLayer.objects.count() == 1
            client.force_login(user_with_membership_global_feature_layer_create_permission)
            client.post(
                f"{self.url}/collections/{global_feature_layer_nonpublic.identifier}/items?f=json",
                data=json.dumps({}),
                content_type="application/json",
            )
            mocked_method.assert_called_once()

            args, kwargs = mocked_method.call_args
            request = args[1]
            action = args[2]
            dataset = args[3]

            assert action == "create"
            assert dataset == global_feature_layer_nonpublic.identifier
            assert json.loads(request.data) == {}

    @pytest.mark.django_db
    def test_permitted_user_can_update_item(
        self,
        client,
        global_feature_layer_nonpublic,
        user_with_membership_global_feature_layer_update_permission,
    ):
        with patch(
            "pygeoapi.api.itemtypes.manage_collection_item",
            return_value=({}, 200, "application/json"),
        ) as mocked_method:
            assert FeatureLayer.objects.count() == 1
            client.force_login(user_with_membership_global_feature_layer_update_permission)
            response = client.get(
                f"{self.url}/collections/{global_feature_layer_nonpublic.identifier}/items?f=json"
            )
            assert response.status_code == HTTP_200_OK
            items = json.loads(response.content)
            test_item_id = items["features"][0]["id"]
            client.put(
                f"{self.url}/collections/{global_feature_layer_nonpublic.identifier}/items/{test_item_id}?f=json",
                data=json.dumps({}),
                content_type="application/json",
            )
            mocked_method.assert_called_once()

            args, kwargs = mocked_method.call_args
            request = args[1]
            action = args[2]
            dataset = args[3]
            identifier = args[4]

            assert identifier == test_item_id
            assert action == "update"
            assert dataset == global_feature_layer_nonpublic.identifier
            assert json.loads(request.data) == {}

    @pytest.mark.django_db
    def test_permitted_user_can_delete_item(
        self,
        client,
        global_feature_layer_nonpublic,
        user_with_membership_global_feature_layer_delete_permission,
    ):
        with patch(
            "pygeoapi.api.itemtypes.manage_collection_item",
            return_value=({}, 200, "application/json"),
        ) as mocked_method:
            assert FeatureLayer.objects.count() == 1
            client.force_login(user_with_membership_global_feature_layer_delete_permission)
            response = client.get(
                f"{self.url}/collections/{global_feature_layer_nonpublic.identifier}/items?f=json"
            )
            assert response.status_code == HTTP_200_OK
            items = json.loads(response.content)
            test_item_id = items["features"][0]["id"]
            client.delete(
                f"{self.url}/collections/{global_feature_layer_nonpublic.identifier}/items/{test_item_id}?f=json"
            )
            mocked_method.assert_called_once()

            args, kwargs = mocked_method.call_args
            action = args[2]
            dataset = args[3]
            identifier = args[4]

            assert identifier == test_item_id
            assert action == "delete"
            assert dataset == global_feature_layer_nonpublic.identifier
