import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction

from georama.integration.factories import (
    FieldFactory,
    ProjectFactory,
    VectorFactory,
)
from georama.maps.factories import MetadataFactory, WmsLayerFactory
from georama.maps.models.wms_layer import WmsLayer

User = get_user_model()


class Command(BaseCommand):
    help = "Flushes db content of integration app and adds a lot of demo content"

    @transaction.atomic
    def handle(self, *args, **options):
        current_config = os.environ.get("DJANGO_CONFIGURATION")

        self.stdout.write(self.style.NOTICE(f"Current Environment: {current_config}"))
        # We only allow this command to run when in dev environment
        WmsLayer.objects.all().delete()
        vector = VectorFactory.create(
            qgis_layer_id="TestPointLayer_e7b906c8_9404_4393_b05e_e72af3eb976b",
            name="TestPointLayer_e7b906c8_9404_4393_b05e_e72af3eb976b",
            bbox="6.2305498123169,46.0072288513184,0.0,10.2997055053711,47.7490196228027,0.0",
            bbox_wgs84="6.2305498123169,46.0072288513184,0.0,10.2997055053711,47.7490196228027,0.0",
            source={
                "ogr": {
                    "path": "data/TestPointLayer.gpkg",
                    "subset": None,
                    "layer_id": None,
                    "layer_name": "TestPointLayer",
                    "vsi_prefix": None,
                },
                "wfs": None,
                "wms": None,
                "xyz": None,
                "gdal": None,
                "wmts": None,
                "postgres": None,
                "vector_tile": None,
            },
            styles=[
                {
                    "name": "default",
                    "definition": "eJztW3tv27YW_9-fQvMFbrcLy3r61SkB2qTdLZAs6ZLuYhgGgRYpm6skqhTl1B323e8hKVmS47V2km3dlrSwzUOeQ54Hz_npweCL04uT6x8uXxjvFrQwLt88P3t1YjxZCpE_tayUR9EwYqklO4dY4CfGk6sfrq5fnD857gWKI6XZVYQSctR37Oqvb6TofUWExhIVqvEcFQR_Tws6pwkV65cJWqj-QqwTcoIEWTBOSXHUf5YkV10aDKJpntB4fb6R7PQNVAr2HYk5KZbnDAPtlBZonhDcNxI0J0nxIlNNPc06nbOELdbAQTjJIlIJMp1G_ClHNzRbXLNETVCTzxgMVRROEL7IkrUS2Zr_mqZa2y1J_6WZKDodzxKpk1imiroivKAsO-p7Q98ezsznHAlaJGiF-sc9I4jBSAX8MIJXmGSCxlQqdOwEVqctB3xHUraqe5uG7LoiiEfLuq_Vkp2XnK7A0Md2YNU_YWKrnjkQJM0ZR4lBWsaM6XuCT0u5WLl4aYsoKtMyAXbVTJU_lHcRFy_e52AkrWhFeklJgmULV1IqQkyl92hKxXktgmS4K6BmeZNRcdSHCFRjaolKK7XA71C2UEoagZrzOLD0tyIBCxDkp2SwOhyBVastGyQhKzWh8aHYBB-sJyeROENrwq9UbClylKA0B8cf9a8J50iurViym3PE39bjXmVXJY9RRC4TVgUHeS94WdS2nNMMKxEn4GPOpEU2A3aG9FH_jGakb4h1Dot7BdwrikuUvCRIlFzunw8sjgsiJJtSFyOBTExiYMNmzllOuICNpi1zkStltbRzlCuWhp4hGevyE-IXJSWRPtGDX18JDivvW7s4mml290sRG4kRSxIwL_Tulh1Ymlc77yPqBNCMaUKkhbT9q4hQv42Yw9whV3Hr2NJ_NA8FC8HgYHzlUr06CHrGIxi65Mr4elGJsjtK8iVSY2kRooymIA7Xtq6sHVbLC7es_dv2vovFP23ze1m9a_fa8r-pWpDI3dFkDjBQwqK3VfjCVikg_K9kYiQ6gHNFgT4KQ36Zjd3JGE-ROXMdbPozHJtoFvtmHNlRhCIc-WP71_6BVkQJXWQhRsUyzJEQhGcb7e09jRqhXBWtDWPxrkSc7MtdFoKlcgEb_tHX7sHMYYrysIQMGKqctJHlvX9qDzb_DhcrRW6EnZ_vKaBtz1DnmoPNukPGgyq5S_4dtYXiHtKsoJiEOUvWC3Z4EP3MQEAniuZkRZI9uWXeCWG3Mr5hd_zRYOoO4NMdjQZ8MX9qD0fjKewhf2TPprYHu8gf2EPPddpk3wWaMxn7E3s0nbreyJ35jjdwDlnI1m5giSxZ-7PfUCyazWAPxwcz39GPdwzU3yE27xWOsi-EGgeBfbAu0JmGmAIuAkQcAhq6v4QHNcxt6XezUVeOgoH31FTJ-B111fLvqO0NQW_DbsLLIF_wDK43Dta7LCDXqAoRdsrWvvx6i97LUl3Y8SlE9REwcCdMtQeouh-quqXfJ3CVpYBVBYSLDaoNrJ1gt4bALylcWT84BAbJySMEfgAI_FIZsguBXdeHC0VvZCI8jk1_PPfNmQNgeEIw8QnxoxkeHwyB54xjwsMH2JbbMPIzACT3w1XbiODQAv7ZYAJWil0Y0fYHo9nAc1su8e2x48-86Wjq-h74YQzmd93ZeDKdzCaj6cwGv3jSJe4YXDZybRgycVzf39sl9VruDhNrCdtIcd_Lpg7_HS16wOofq9VB1apbl-pq1b5l9pD1KlVyHyvWA1Ss88qU3ZrlEM-e2G5sQnqfmj7xXHNmO7YZQz63fc8beXF8-G2bbNHafQfcqdnOOgfdqvkM6tmScfqBZQIlEKQRtMIcKlyTv_6YutgJY0xRyrK9c_djSf37l9QHddJDFGu5jDAlYslwJ26Jukmynwz6oaXJAUwPag0l8G5GWMm0Hh2cOB7Ry0HoZQunBNbmcaFscZLBtRbh5sqtntclMu1Wj_1UjVVXY3P9SFkBFo4KiFLV5vXD6qJ5WK3VKqisiHpa_UxPiy_uhpXsR7D0p4Alfzb1xvaUmJiQyPTn9syc-nFk2tEIjyau59ne_K8IllwHaqI98NtlcdrgH4mHxiNZAreRkaR1Kc7krwyWIsqjZF8b_t2xkjsdgDfdDoK2ndnYnkx9z_Em7sifQgDY4-7fRNIqhF1Da-czwEr-I1bahZX2fX73iJX-MViphU0CzoSCR5ZGLeAz5Xrd_Me8mBRYLWgo2wWp5FYvz52SGJWJqLBd3XkiE6pBM1gNVXjD6vY_3i97gLD_YyHg1BkRZ-bPzXjk2vI1J88EpETMcUwmCE1QNPLwXxICQo2X2buu9Y5qPUK5vwWU80YD_b9Bchq_zTZ4Tt3h2ov2pyO5Rxy3C8fteyvwEcf9c3DcLZzRosmWfk9o6xXs3dbqaiTfV19RcmPlnMjv5pX_otbqjBZiC_JVFvj3u5KJr2OK9Y9PI7OtyUk6JxgT_D-KF0QUVsTKbMf7YTKUrB3sK8TVQYxvoVU0gxVG-yjD93KC3Ryt1QbWDqsGwJ5heUhCHt1oGvLUiH7t_3l7wC1arwIuFzmKqFjLkyGdNvQvCIPcwdd6IYXB5akSclrmCewwQb4FMRrG1AMvOYlofYxBKYEgMFbkZEmit4VWK5K_T1gW00V1jMNSKm5NptZHFrBadX7iTJ7nOVPtlj-whsjmCuIPapMSFMtjIB35alpFrqyvzphE7SHyMBKo8i2TP6roJJgKHQ_VbNcAmF8AsQ5BLaGLy-rrB6vVGViNKO1ZtRil9c7VBhAFqKj2jvptxK3TMTVYp3D58F5aQxuwYQoK8JC4hLIYbQ5ByMba0F9wbVH7sN-WrOVsMwe4HnxXibsEBJXvtLCqYZDOOZ-20ijPk_VF9ibH1RGjSnQjRfqjEPLITSW0aXfNx0RWJgmACLgAW4ilqgowcYsAAQbV511JuoNaE8gHQnoF3Vlbk7YS2MeWA3soksrCCuBrW2ZXSNDYR4lQWypAArLcvBQERWIzW2WYZ_qK8i0BF50gyC_N25-_1Of1zB0f9d-vdXDdnqOZV8hUpgPeKBgXF_KBRnUqTI7Woa_O9Ml351l-ym7kuSi2dTKsMlNSpll1wa8bxpJCctZno1o7WGGl9iMRZZM6326xOjvGV7rU-baZuaVvS7fKvbCXgQslCoTWdzRudMtqck1DUP68xRVARucENx7VY2WqgKvw1BAsIRzp6_NjnUIkvT2GAkKytgmRzMqshOt4mfZ_o2eLRz7GypFYHncZNuQdUxwHX_x4cvrs-tmP_zLM_5iwN-SRtadGKWJzKim9fr_fe_3Nqyt5UyEtjAiBM9CKGMi4XANEzYy4zHR0iiUSBpVDAMdg42ZJJI0oRqD3oOoBShn2em8KAh0wsmFlBsJYHY9DcNm9oJEkrUFLPS0wvcgA_ip5MnYMFmvZtQSq5-pXi3oF-m06-z3lymHvWQZTIHkJD2KTBNz9VOkXc5aqk7PDy_VrMXxdZfnCoPL0oDBe63avB9vRSNehXFMo1fkScDksd2ComjswqvL81VNVPmQtNI5q4rAujV9-pXohmgRnCQzQQoYA4vDJkib4y2q-gdE_X8t3gFW5-qr300_Ht0OhRgrKTmWuwrBGCh1a5X3GYa1wnXIMRZjIu0lYt7XkTW81enO-VBfemtS629TUh9b4QB3cvciuWd7ibohbOUDzd3gCTsqCnKFCKHDVktLt2CnpFq-6EDjVMFkdML3cYDDFcVMBRvn7FnA9VpKD24hWjobrpWuat28bgY80cYPNvqkcfw3pSrrmNrEXqLPZx73_A_7Fjjo=",  # noqa: E501
                }
            ],
            driver="ogr",
            crs={
                "auth_id": "EPSG:4326",
                "ogc_uri": "http://www.opengis.net/def/crs/EPSG/0/4326",
                "ogc_urn": "urn:ogc:def:crs:EPSG::4326",
                "postgis_srid": 4326,
            },
            maximum_scale=0,
            minimum_scale=100000000,
            geometry_type_simple="Point",
            geometry_type_wkb="Point",
            project=ProjectFactory(
                name="TestProject", organisation=None, path="TestMandant/TestProject.qgz"
            ),
            fields=[],
        )
        FieldFactory.create(
            name="fid",
            type="Integer64",
            is_primary_key=True,
            type_wfs="long",
            type_oapif="integer",
            type_oapif_format="int64",
            alias="Fid",
            comment="",
            nullable=True,
            length=None,
            precision=None,
            datasource=vector,
        )
        FieldFactory.create(
            name="name",
            type="String",
            is_primary_key=False,
            type_wfs="string",
            type_oapif="string",
            type_oapif_format="string",
            alias="Name",
            comment="",
            nullable=False,
            length=10,
            precision=None,
            datasource=vector,
        )
        WmsLayerFactory.create(
            id="09b56f4c-e0b7-432d-b99e-48a692d12ea4",
            datasource=vector,
            metadata=MetadataFactory(title="TestWmsLayer"),
        )
