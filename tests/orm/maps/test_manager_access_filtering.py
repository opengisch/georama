import pytest
from xsdata.formats.dataclass.parsers import XmlParser

from georama.maps.interfaces.ogc.wfs_2_0_0 import WfsCapabilities
from georama.maps.interfaces.ogc.wms_1_3_0.capabilities.capabilities_1_3_0 import WmsCapabilities
from georama.maps.services.wfs_2_0_0 import WfsOperation


class TestOgcService:
    """We test the correct filtering of accessable layers with a full walk from publishing
    a test layer with decent permissions and then analysing the returned capabilities
    content"""

    wms_capabilities_url = "/maps/ows?SERVICE=WMS&REQUEST=GETCAPABILITIES&VERSION=1.3.0"
    wfs_capabilities_url = "/maps/ows?SERVICE=WFS&REQUEST=GETCAPABILITIES&VERSION=2.0.0"

    @pytest.mark.django_db
    def test_anonymous_can_see_public_wms_layer(self, client, global_wms_layer_public_queryable):
        response = client.get(self.wms_capabilities_url)
        capabilities: WmsCapabilities = XmlParser().from_bytes(response.content, WmsCapabilities)
        assert capabilities.capability.layer is not None
        assert len(capabilities.capability.layer.layer) == 1
        assert capabilities.capability.layer.layer[0].name.value == str(
            global_wms_layer_public_queryable.id
        )

    @pytest.mark.django_db
    def test_anonymous_can_see_public_queryable_wfs_layer(
        self, client, global_wms_layer_public_queryable
    ):
        response = client.get(self.wfs_capabilities_url)
        capabilities: WfsCapabilities = XmlParser().from_bytes(response.content, WfsCapabilities)
        assert capabilities.feature_type_list is not None
        assert len(capabilities.feature_type_list.feature_type) == 1
        assert (
            capabilities.feature_type_list.feature_type[0].name
            == f"{WfsOperation.own_namespace}:{str(global_wms_layer_public_queryable.id)}"
        )

    @pytest.mark.django_db
    def test_anonymous_can_see_public_non_queryable_wms_layer(
        self, client, global_wms_layer_public_non_queryable
    ):
        response = client.get(self.wms_capabilities_url)
        capabilities: WmsCapabilities = XmlParser().from_bytes(response.content, WmsCapabilities)
        assert capabilities.capability.layer is not None
        assert len(capabilities.capability.layer.layer) == 1
        assert capabilities.capability.layer.layer[0].name.value == str(
            global_wms_layer_public_non_queryable.id
        )

    @pytest.mark.django_db
    def test_anonymous_cannot_see_public_non_queryable_wfs_layer(
        self, client, global_wms_layer_public_non_queryable
    ):
        response = client.get(self.wfs_capabilities_url)
        capabilities: WfsCapabilities = XmlParser().from_bytes(response.content, WfsCapabilities)
        assert capabilities.feature_type_list is not None
        assert len(capabilities.feature_type_list.feature_type) == 0

    @pytest.mark.django_db
    def test_anonymous_cannot_see_non_public_queryable_wms_layer(
        self, client, global_wms_layer_non_public_queryable
    ):
        response = client.get(self.wms_capabilities_url)
        capabilities: WmsCapabilities = XmlParser().from_bytes(response.content, WmsCapabilities)
        assert capabilities.capability.layer is not None
        assert len(capabilities.capability.layer.layer) == 0

    @pytest.mark.django_db
    def test_anonymous_cannot_see_non_public_queryable_wfs_layer(
        self, client, global_wms_layer_non_public_queryable
    ):
        response = client.get(self.wfs_capabilities_url)
        capabilities: WfsCapabilities = XmlParser().from_bytes(response.content, WfsCapabilities)
        assert capabilities.feature_type_list is not None
        assert len(capabilities.feature_type_list.feature_type) == 0

    @pytest.mark.django_db
    def test_permitted_user_can_see_non_public_queryable_wms_layer(
        self,
        client,
        global_wms_layer_non_public_queryable,
        user_with_membership_global_layer_permission,
    ):
        client.force_login(user_with_membership_global_layer_permission)
        response = client.get(self.wms_capabilities_url)
        capabilities: WmsCapabilities = XmlParser().from_bytes(response.content, WmsCapabilities)
        assert capabilities.capability.layer is not None
        assert len(capabilities.capability.layer.layer) == 1
        assert capabilities.capability.layer.layer[0].name.value == str(
            global_wms_layer_non_public_queryable.id
        )

    @pytest.mark.django_db
    def test_permitted_user_can_see_non_public_queryable_wfs_layer(
        self,
        client,
        global_wms_layer_non_public_queryable,
        user_with_membership_global_layer_permission,
    ):
        client.force_login(user_with_membership_global_layer_permission)
        response = client.get(self.wfs_capabilities_url)
        capabilities: WfsCapabilities = XmlParser().from_bytes(response.content, WfsCapabilities)
        assert capabilities.feature_type_list is not None
        assert len(capabilities.feature_type_list.feature_type) == 1
        assert (
            capabilities.feature_type_list.feature_type[0].name
            == f"{WfsOperation.own_namespace}:{str(global_wms_layer_non_public_queryable.id)}"
        )

    @pytest.mark.django_db
    def test_admin_can_see_all_wms_layer(
        self,
        client,
        global_wms_layer_non_public_queryable,
        global_wms_layer_public_non_queryable,
        global_wms_layer_public_queryable,
        admin_user,
    ):
        client.force_login(admin_user)
        response = client.get(self.wms_capabilities_url)
        capabilities: WmsCapabilities = XmlParser().from_bytes(response.content, WmsCapabilities)
        assert capabilities.capability.layer is not None
        assert len(capabilities.capability.layer.layer) == 3

    @pytest.mark.django_db
    def test_admin_can_see_all_queryable_wfs_layer(
        self,
        client,
        global_wms_layer_non_public_queryable,
        global_wms_layer_public_non_queryable,
        global_wms_layer_public_queryable,
        admin_user,
    ):
        client.force_login(admin_user)
        response = client.get(self.wfs_capabilities_url)
        capabilities: WfsCapabilities = XmlParser().from_bytes(response.content, WfsCapabilities)
        assert capabilities.feature_type_list is not None
        assert len(capabilities.feature_type_list.feature_type) == 2
