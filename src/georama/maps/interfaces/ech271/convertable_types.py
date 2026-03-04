from georama.maps.interfaces.ech271.INTERLIS import I32OID as INTERLIS_I32OID
from georama.maps.interfaces.ech271.INTERLIS import (
    INTERLIS_1_DATE as INTERLIS_INTERLIS_1_DATE,
)
from georama.maps.interfaces.ech271.INTERLIS import NAME as INTERLIS_NAME
from georama.maps.interfaces.ech271.INTERLIS import STANDARDOID as INTERLIS_STANDARDOID
from georama.maps.interfaces.ech271.INTERLIS import URI as INTERLIS_URI
from georama.maps.interfaces.ech271.INTERLIS import UUIDOID as INTERLIS_UUIDOID
from georama.maps.interfaces.ech271.INTERLIS import (
    GregorianYear as INTERLIS_GregorianYear,
)
from georama.maps.interfaces.ech271.INTERLIS import XMLDate as INTERLIS_XMLDate
from georama.maps.interfaces.ech271.INTERLIS import XMLDateTime as INTERLIS_XMLDateTime
from georama.maps.interfaces.ech271.INTERLIS import XMLTime as INTERLIS_XMLTime


def get_special_int_types() -> list:
    return [
        INTERLIS_I32OID,
        INTERLIS_GregorianYear,
    ]


def get_special_str_types() -> list:
    return [
        INTERLIS_URI,
        INTERLIS_NAME,
        INTERLIS_INTERLIS_1_DATE,
        INTERLIS_STANDARDOID,
        INTERLIS_UUIDOID,
        INTERLIS_XMLTime,
        INTERLIS_XMLDate,
        INTERLIS_XMLDateTime,
    ]


def get_special_float_types() -> list:
    return []


def get_contained_model_names() -> list:
    return [
        "InternationalCodes_V2",
        "Localisation_V2",
        "LocalisationCH_V2",
        "Dictionaries_V2",
        "DictionariesCH_V2",
        "Units",
        "eCH0271_1",
    ]
