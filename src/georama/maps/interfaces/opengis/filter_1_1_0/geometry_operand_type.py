from enum import Enum
from xml.etree.ElementTree import QName

__NAMESPACE__ = "http://www.opengis.net/ogc"


class GeometryOperandType(Enum):
    GML_ENVELOPE = QName("{http://www.opengis.net/gml}Envelope")
    GML_POINT = QName("{http://www.opengis.net/gml}Point")
    GML_LINE_STRING = QName("{http://www.opengis.net/gml}LineString")
    GML_POLYGON = QName("{http://www.opengis.net/gml}Polygon")
    GML_ARC_BY_CENTER_POINT = QName("{http://www.opengis.net/gml}ArcByCenterPoint")
    GML_CIRCLE_BY_CENTER_POINT = QName(
        "{http://www.opengis.net/gml}CircleByCenterPoint"
    )
    GML_ARC = QName("{http://www.opengis.net/gml}Arc")
    GML_CIRCLE = QName("{http://www.opengis.net/gml}Circle")
    GML_ARC_BY_BULGE = QName("{http://www.opengis.net/gml}ArcByBulge")
    GML_BEZIER = QName("{http://www.opengis.net/gml}Bezier")
    GML_CLOTHOID = QName("{http://www.opengis.net/gml}Clothoid")
    GML_CUBIC_SPLINE = QName("{http://www.opengis.net/gml}CubicSpline")
    GML_GEODESIC = QName("{http://www.opengis.net/gml}Geodesic")
    GML_OFFSET_CURVE = QName("{http://www.opengis.net/gml}OffsetCurve")
    GML_TRIANGLE = QName("{http://www.opengis.net/gml}Triangle")
    GML_POLYHEDRAL_SURFACE = QName("{http://www.opengis.net/gml}PolyhedralSurface")
    GML_TRIANGULATED_SURFACE = QName("{http://www.opengis.net/gml}TriangulatedSurface")
    GML_TIN = QName("{http://www.opengis.net/gml}Tin")
    GML_SOLID = QName("{http://www.opengis.net/gml}Solid")
