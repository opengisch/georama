# Exemplaric sources

## WFS

The sources were fetched by https://map.geo.bs.ch/mapserv_proxy? and represent the content we need to satisfy
with our WFS too.

The [WFS 2.0.0 specification](Web_Feature_Service_WFS_2.0_ISOFDIS_19142_Geographic_information_-_Web_Feature_Service.pdf)
gives insights to details.

Mainly we will implement the following operations.

Examples from BS Mapserver instance:

-
Link: [DescribeFeatureType](https://map.geo.bs.ch/mapserv_proxy?ogcserver=WMS+BS+%28edit%29&service=WFS&request=DescribeFeatureType&version=2.0.0),
local copy [DescribeFeatureType](mapserver.bs.describe_feature_type.2_0_0.xml)
-
Link: [GetCapabilities](https://map.geo.bs.ch/mapserv_proxy?ogcserver=WMS+BS+%28edit%29&service=WFS&request=GetCapabilities&version=2.0.0),
local copy: [GetCapabilities](mapserver.bs.get_capabilities.2_0_0.xml)
-
Link: [GetFeature](https://map.geo.bs.ch/mapserv_proxy?ogcserver=WMS+BS+%28edit%29&SERVICE=WFS&REQUEST=GetFeature&VERSION=2.0.0&TYPENAMES=ms:DM_Gebaeudeadresse_DatenmarktAdressen_AdresseFertiggestellt&STARTINDEX=0&COUNT=1&SRSNAME=urn:ogc:def:crs:EPSG::2056),
local copy: [GetFeature](mapserver.bs.get_feature.2_0_0.xml)
-
Link: [GetPropertyValue](https://map.geo.bs.ch/mapserv_proxy?ogcserver=WMS+BS+%28edit%29&SERVICE=WFS&REQUEST=getpropertyvalue&VERSION=2.0.0&TYPENAMES=ms:DM_Gebaeudeadresse_DatenmarktAdressen_AdresseFertiggestellt&STARTINDEX=0&COUNT=1&SRSNAME=urn:ogc:def:crs:EPSG::2056&VALUEREFERENCE=ms:dm_gebaeudeadresselaufnummer),
local copy: [GetPropertyValue](mapserver.bs.get_property_value.2_0_0.xml)
