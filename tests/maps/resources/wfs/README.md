# Exemplaric sources

## WFS

The sources were fetched by https://map.geo.bs.ch/mapserv_proxy? and represent the content we need to satisfy
with our WFS too.

The [WFS 2.0.0 specification](Web_Feature_Service_WFS_2.0_ISOFDIS_19142_Geographic_information_-_Web_Feature_Service.pdf)
gives insights to details.

Mainly we will implement the following operations.

Examples from BS Mapserver instance:

| Operation           | Link                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Local Copy                                                                                   |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| DescribeFeatureType | [service=WFS&request=DescribeFeatureType&version=2.0.0](https://map.geo.bs.ch/mapserv_proxy?ogcserver=WMS+BS+%28edit%29&service=WFS&request=DescribeFeatureType&version=2.0.0)                                                                                                                                                                                                                                                                                     | [mapserver.bs.describe_feature_type.2_0_0.xml](mapserver.bs.describe_feature_type.2_0_0.xml) |
| GetCapabilities     | [service=WFS&request=GetCapabilities&version=2.0.0](https://map.geo.bs.ch/mapserv_proxy?ogcserver=WMS+BS+%28edit%29&service=WFS&request=GetCapabilities&version=2.0.0)                                                                                                                                                                                                                                                                                             | [mapserver.bs.get_capabilities.2_0_0.xml](mapserver.bs.get_capabilities.2_0_0.xml)           |
| GetFeature          | [SERVICE=WFS&REQUEST=GetFeature&VERSION=2.0.0&TYPENAMES=ms:DM_Gebaeudeadresse_DatenmarktAdressen_AdresseFertiggestellt&STARTINDEX=0&COUNT=1](https://map.geo.bs.ch/mapserv_proxy?ogcserver=WMS+BS+%28edit%29&SERVICE=WFS&REQUEST=GetFeature&VERSION=2.0.0&TYPENAMES=ms:DM_Gebaeudeadresse_DatenmarktAdressen_AdresseFertiggestellt&STARTINDEX=0&COUNT=1)                                                                                                           | [mapserver.bs.get_feature.2_0_0.xml](mapserver.bs.get_feature.2_0_0.xml)                     |
| GetPropertyValue    | [SERVICE=WFS&REQUEST=getpropertyvalue&VERSION=2.0.0&TYPENAMES=ms:DM_Gebaeudeadresse_DatenmarktAdressen_AdresseFertiggestellt&STARTINDEX=0&COUNT=1&VALUEREFERENCE=ms:dm_gebaeudeadresselaufnummer](https://map.geo.bs.ch/mapserv_proxy?ogcserver=WMS+BS+%28edit%29&SERVICE=WFS&REQUEST=getpropertyvalue&VERSION=2.0.0&TYPENAMES=ms:DM_Gebaeudeadresse_DatenmarktAdressen_AdresseFertiggestellt&STARTINDEX=0&COUNT=1&VALUEREFERENCE=ms:dm_gebaeudeadresselaufnummer) | [mapserver.bs.get_property_value.2_0_0.xml](mapserver.bs.get_property_value.2_0_0.xml)       |
