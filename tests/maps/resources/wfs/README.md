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
| GetMetadata         | [request=GetMetadata&layer=AF_AbfuhrzoneGemeindeBasel](https://wfs.geo.bs.ch/?request=GetMetadata&layer=AF_AbfuhrzoneGemeindeBasel)                                                                                                                                                                                                                                                                                                                                | [mapserver.bs.get_metadata.xml](mapserver.bs.get_metadata.xml)                               |


## GetFeature with Filter

```
POST https://map.geo.bs.ch/mapserv_proxy?ogcserver=WMS+BS+%281%29
Content-Type: text/xml

<GetFeature xmlns="http://www.opengis.net/wfs" service="WFS" version="1.1.0" maxFeatures="300" xsi:schemaLocation="http://www.opengis.net/wfs http://schemas.opengis.net/wfs/1.1.0/wfs.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><Query typeName="feature:DM_Gebaeudeadresse_DatenmarktAdressen_AdresseFertiggestellt" srsName="EPSG:2056" xmlns:feature="https://mapserver.gis.umn.edu/mapserver"><Filter xmlns="http://www.opengis.net/ogc"><BBOX><PropertyName>the_geom</PropertyName><Envelope xmlns="http://www.opengis.net/gml" srsName="EPSG:2056"><lowerCorner>2612002.1608299157 1267096.978301732</lowerCorner><upperCorner>2612028.6192161655 1267070.519915482</upperCorner></Envelope></BBOX></Filter></Query></GetFeature>
```

filter XML:
```xml
<Filter xmlns="http://www.opengis.net/ogc"><BBOX><PropertyName>the_geom</PropertyName><Envelope xmlns="http://www.opengis.net/gml" srsName="EPSG:2056"><lowerCorner>2612002.1608299157 1267096.978301732</lowerCorner><upperCorner>2612028.6192161655 1267070.519915482</upperCorner></Envelope></BBOX></Filter>
```

pyqgis filter:
```python

project_folder = QgsProject.instance().readPath("./")

xml_filter = '<Filter xmlns="http://www.opengis.net/ogc"><BBOX><PropertyName>the_geom</PropertyName><Envelope xmlns="http://www.opengis.net/gml" srsName="EPSG:2056"><lowerCorner>2612002.1608299157 1267096.978301732</lowerCorner><upperCorner>2612028.6192161655 1267070.519915482</upperCorner></Envelope></BBOX></Filter>' # NOT WORKING, need an actual QDomElement object, possible to parse it from string?
addresses = QgsProject.instance().mapLayersByName('ms:DM_Gebaeudeadresse_DatenmarktAdressen_AdresseFertiggestellt')
v = FilterVersion.FILTER_FES_2_0 
QgsOgcUtils.expressionFromOgcFilter(xml_filter, v, addresses)
```

TODO CREATE QDomElement. Possible to parse from string? if not, create elements programmatically https://doc.qt.io/qt-6/qdomelement.html