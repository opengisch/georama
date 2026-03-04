from abc import ABC
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Tuple, Union

from georama.maps.interfaces.ech271.InternationalCodes_V2 import (
    CountryCode_ISO3166_1 as InternationalCodes_V2CountryCode_ISO3166_1,
)
from georama.maps.interfaces.ech271.InternationalCodes_V2 import (
    LanguageCode_ISO639_1 as InternationalCodes_V2LanguageCode_ISO639_1,
)
from georama.maps.interfaces.ech271.Localisation_V2 import (
    MultilingualMText as Localisation_V2MultilingualMText,
)
from georama.maps.interfaces.ech271.Localisation_V2 import (
    MultilingualText as Localisation_V2MultilingualText,
)
from georama.maps.interfaces.ech271.Localisation_V2 import (
    MultilingualUri as Localisation_V2MultilingualUri,
)
from georama.maps.interfaces.ech271.references import Ref

metadata: dict = {"interlis": {"meta_attributes": {}}}


class Angle(float):

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.Angle",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": "Units.Angle_Degree",
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": True,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "precision": 5,
                    "min": 0.0,
                    "max": 360.0,
                },
            }
        }

    @property
    def existence_constraints(self) -> list:
        return []

    @property
    def set_constraints(self) -> list:
        return []

    @property
    def simple_constraints(self) -> list:
        return []

    @property
    def unique_constraints(self) -> list:
        return []


class DateTime(str):

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.DateTime",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": '"Year"-"Month"-"Day"T"Hours/2":"Minutes":"Seconds"',
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": "INTERLIS.XMLDateTime",
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "struct": "INTERLIS.GregorianDateTime",
                    "min": "1582-1-1T0:0:0.0",
                    "max": "2999-12-31T23:59:59.999",
                },
            }
        }

    @property
    def existence_constraints(self) -> list:
        return []

    @property
    def set_constraints(self) -> list:
        return []

    @property
    def simple_constraints(self) -> list:
        return []

    @property
    def unique_constraints(self) -> list:
        return []


class Distance(float):

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.Distance",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": "INTERLIS.m",
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": False,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "precision": 2,
                    "min": 0.0,
                    "max": 9999999999.99,
                },
            }
        }

    @property
    def existence_constraints(self) -> list:
        return []

    @property
    def set_constraints(self) -> list:
        return []

    @property
    def simple_constraints(self) -> list:
        return []

    @property
    def unique_constraints(self) -> list:
        return []


class Real(float):

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.Real",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": False,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "precision": 2,
                    "min": -9999999999.99,
                    "max": 9999999999.99,
                },
            }
        }

    @property
    def existence_constraints(self) -> list:
        return []

    @property
    def set_constraints(self) -> list:
        return []

    @property
    def simple_constraints(self) -> list:
        return []

    @property
    def unique_constraints(self) -> list:
        return []


class Integer(int):

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.Integer",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": False,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "min": -10000000000,
                    "max": 10000000000,
                },
            }
        }

    @property
    def existence_constraints(self) -> list:
        return []

    @property
    def set_constraints(self) -> list:
        return []

    @property
    def simple_constraints(self) -> list:
        return []

    @property
    def unique_constraints(self) -> list:
        return []


class CharacterString(str):

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CharacterString",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "max_length": 256,
                },
            }
        }

    @property
    def existence_constraints(self) -> list:
        return []

    @property
    def set_constraints(self) -> list:
        return []

    @property
    def simple_constraints(self) -> list:
        return []

    @property
    def unique_constraints(self) -> list:
        return []


class CharacterStringLong(str):

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CharacterStringLong",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                },
            }
        }

    @property
    def existence_constraints(self) -> list:
        return []

    @property
    def set_constraints(self) -> list:
        return []

    @property
    def simple_constraints(self) -> list:
        return []

    @property
    def unique_constraints(self) -> list:
        return []


class CHE_AppraisalOfArchivalValueCode(str, Enum):
    A = "A"
    N = "N"
    S = "S"

    @property
    def metadata(self) -> dict:
        return {
            "ili2py": {},
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_AppraisalOfArchivalValueCode",
                "kind": "Enumeration",
                "meta_attributes": {},
            },
        }


class CHE_CI_LegislationTypeCode(str, Enum):
    LAW = "law"
    ORDINANCE = "ordinance"
    OTHERLEGALPROVISION = "otherLegalProvision"

    @property
    def metadata(self) -> dict:
        return {
            "ili2py": {},
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_CI_LegislationTypeCode",
                "kind": "Enumeration",
                "meta_attributes": {},
            },
        }


class CHE_DS_AssociationTypeCode(str, Enum):
    """
    justification for the correlation of two datasets
    """

    CROSSREFERENCE = "crossReference"
    LARGERWORKCITATION = "largerWorkCitation"
    PARTOFSEAMLESSDATABASE = "partOfSeamlessDatabase"
    STEREOMATE = "stereoMate"
    ISCOMPOSEDOF = "isComposedOf"
    COLLECTIVETITLE = "collectiveTitle"
    SERIES = "series"
    DEPENDENCY = "dependency"
    REVISIONOF = "revisionOf"
    ISTEMPORALSTATEOF = "isTemporalStateOf"
    ISDESCRIPTIONOF = "isDescriptionOf"
    ISDESCRIBEDBY = "isDescribedBy"

    @property
    def metadata(self) -> dict:
        return {
            "ili2py": {},
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_DS_AssociationTypeCode",
                "kind": "Enumeration",
                "meta_attributes": {},
            },
        }


class CHE_MD_BasicGeodataAccessLevelCode(str, Enum):
    A = "A"
    B = "B"
    C = "C"

    @property
    def metadata(self) -> dict:
        return {
            "ili2py": {},
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_BasicGeodataAccessLevelCode",
                "kind": "Enumeration",
                "meta_attributes": {},
            },
        }


class CHE_MD_BasicGeodataTypeCode(str, Enum):
    OEREB = "oereb"
    REFERENCEDATA = "referenceData"

    @property
    def metadata(self) -> dict:
        return {
            "ili2py": {},
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_BasicGeodataTypeCode",
                "kind": "Enumeration",
                "meta_attributes": {},
            },
        }


class CHE_MD_LevelCode(str, Enum):
    COMMUNAL = "communal"
    CANTONAL = "cantonal"
    FEDERAL = "federal"
    OTHER = "other"

    @property
    def metadata(self) -> dict:
        return {
            "ili2py": {},
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_LevelCode",
                "kind": "Enumeration",
                "meta_attributes": {},
            },
        }


class CHE_MD_SubTopicCategoryCode(str, Enum):
    IMAGERYBASEMAPSEARTHCOVER_BASEMAPS = "imageryBaseMapsEarthCover_BaseMaps"
    IMAGERYBASEMAPSEARTHCOVER_EARTHCOVER = "imageryBaseMapsEarthCover_EarthCover"
    IMAGERYBASEMAPSEARTHCOVER_IMAGERY = "imageryBaseMapsEarthCover_Imagery"
    PLANNINGCADASTRE_PLANNING = "planningCadastre_Planning"
    PLANNINGCADASTRE_CADASTRE = "planningCadastre_Cadastre"
    GEOSCIENTIFICINFORMATION_GEOLOGY = "geoscientificInformation_Geology"
    GEOSCIENTIFICINFORMATION_SOILS = "geoscientificInformation_Soils"
    GEOSCIENTIFICINFORMATION_NATURALHAZARDS = "geoscientificInformation_NaturalHazards"
    ENVIRONMENT_ENVIRONMENTALPROTECTION = "environment_EnvironmentalProtection"
    ENVIRONMENT_NATUREPROTECTION = "environment_NatureProtection"
    UTILITIESCOMMUNICATION_ENERGY = "utilitiesCommunication_Energy"
    UTILITIESCOMMUNICATION_UTILITIES = "utilitiesCommunication_Utilities"
    UTILITIESCOMMUNICATION_COMMUNICATION = "utilitiesCommunication_Communication"

    @property
    def metadata(self) -> dict:
        return {
            "ili2py": {},
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_SubTopicCategoryCode",
                "kind": "Enumeration",
                "meta_attributes": {},
            },
        }


class CHE_ReasonForArchivingValueCode(str, Enum):
    LEGALRELEVANCE = "legalRelevance"
    QUARANTEEOFLEGALCERTAINTY = "quaranteeOfLegalCertainty"
    EVIDENCEOFBUSINESSPRACTICE = "evidenceOfBusinessPractice"
    BENEFITSFORRESEARCH = "benefitsForResearch"
    CONTEMPORARYINTEREST = "contemporaryInterest"
    SENSITIVITY = "sensitivity"
    DEVELOPMENTSPROGRESSION = "developmentsProgression"
    DEFININGPOWERS = "definingPowers"

    @property
    def metadata(self) -> dict:
        return {
            "ili2py": {},
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_ReasonForArchivingValueCode",
                "kind": "Enumeration",
                "meta_attributes": {},
            },
        }


class DCPList(str, Enum):
    XML_ = "XML_"
    CORBA = "CORBA"
    JAVA = "JAVA"
    COM = "COM"
    SQL = "SQL"
    SOAP = "SOAP"
    Z3950 = "Z3950"
    HTTP = "HTTP"
    FTP = "FTP"
    WEBSERVICES = "webServices"

    @property
    def metadata(self) -> dict:
        return {
            "ili2py": {},
            "interlis": {
                "oid": "eCH0271_1.eCH0271.DCPList",
                "kind": "Enumeration",
                "meta_attributes": {},
            },
        }


class MD_ClassificationCode(str, Enum):
    """
    name of the handling restrictions on the dataset
    """

    UNCLASSIFIED = "unclassified"
    RESTRICTED = "restricted"
    CONFIDENTIAL = "confidential"
    SECRET = "secret"
    TOPSECRET = "topSecret"
    SENSITIVEBUTUNCLASSIFIED = "sensitiveButUnclassified"
    FOROFFICIALUSEONLY = "forOfficialUseOnly"
    PROTECTED = "protected"
    LIMITEDDISTRIBUTION = "limitedDistribution"

    @property
    def metadata(self) -> dict:
        return {
            "ili2py": {},
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_ClassificationCode",
                "kind": "Enumeration",
                "meta_attributes": {},
            },
        }


class MD_KeywordTypeCode(str, Enum):
    """
    methods used to group similar keywords
    """

    DISCIPLINE = "discipline"
    PLACE = "place"
    STRATUM = "stratum"
    TEMPORAL = "temporal"
    THEME = "theme"
    DATACENTRE = "dataCentre"
    FEATURETYPE = "featureType"
    INSTRUMENT = "instrument"
    PLATFORM = "platform"
    PROCESS = "process"
    PROJECT = "project"
    SERVICE = "service"
    PRODUCT = "product"
    SUBTOPICCATEGORY = "subTopicCategory"
    TAXON = "taxon"

    @property
    def metadata(self) -> dict:
        return {
            "ili2py": {},
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_KeywordTypeCode",
                "kind": "Enumeration",
                "meta_attributes": {},
            },
        }


class MD_MaintenanceFrequencyCode(str, Enum):
    """
    frequency with which modifications and deletions are made to the data after it is first produced
    """

    CONTINUAL = "continual"
    DAILY = "daily"
    WEEKLY = "weekly"
    FORTNIGHTLY = "fortnightly"
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    BIANNUALLY = "biannually"
    ANNUALLY = "annually"
    ASNEEDED = "asNeeded"
    IRREGULAR = "irregular"
    NOTPLANNED = "notPlanned"
    UNKNOWN = "unknown"

    @property
    def metadata(self) -> dict:
        return {
            "ili2py": {},
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_MaintenanceFrequencyCode",
                "kind": "Enumeration",
                "meta_attributes": {},
            },
        }


class MD_RestrictionCode(str, Enum):
    """
    limitation(s) placed upon the access or use of the data
    """

    COPYRIGHT = "copyright"
    PATENT = "patent"
    PATENTPENDING = "patentPending"
    TRADEMARK = "trademark"
    LICENSE = "license"
    INTELLECTUALPROPERTYRIGHTS = "intellectualPropertyRights"
    RESTRICTED = "restricted"
    OTHERRESTRICTIONS = "otherRestrictions"
    UNRESTRICTED = "unrestricted"
    LICENCEUNRESTRICTED = "licenceUnrestricted"
    LICENCEENDUSER = "licenceEndUser"
    LICENCEDISTRIBUTOR = "licenceDistributor"
    PRIVATE = "private"
    STATUTORY = "statutory"
    CONFIDENTIAL = "confidential"
    SENSITIVEBUTUNCLASSIFIED = "sensitiveButUnclassified"
    IN_CONFIDENCE = "in_confidence"

    @property
    def metadata(self) -> dict:
        return {
            "ili2py": {},
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_RestrictionCode",
                "kind": "Enumeration",
                "meta_attributes": {},
            },
        }


class MD_ScopeCode(str, Enum):
    """
    class of information to which the referencing entity applies
    """

    ATTRIBUTE = "attribute"
    ATTRIBUTETYPE = "attributeType"
    COLLECTIONHARDWARE = "collectionHardware"
    COLLECTIONSESSION = "collectionSession"
    DATASET = "dataset"
    SERIES = "series"
    NONGEOGRAPHICDATASET = "nonGeographicDataset"
    DIMENSIONGROUP = "dimensionGroup"
    FEATURE = "feature"
    FEATURETYPE = "featureType"
    PROPERTYTYPE = "propertyType"
    FIELDSESSION = "fieldSession"
    SOFTWARE = "software"
    SERVICE = "service"
    MODEL = "model"
    TILE = "tile"
    METADATA = "metadata"
    INITITATIVE = "inititative"
    SAMPLE = "sample"
    DOCUMENT = "document"
    REPOSITORY = "repository"
    AGGREGATE = "aggregate"
    PRODUCT = "product"
    COLLECTION = "collection"
    COVERAGE = "coverage"
    APPLICATION = "application"

    @property
    def metadata(self) -> dict:
        return {
            "ili2py": {},
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_ScopeCode",
                "kind": "Enumeration",
                "meta_attributes": {},
            },
        }


class MD_ProgressCode(str, Enum):
    """
    status of the dataset or progress of a review
    """

    COMPLETED = "completed"
    HISTORICALARCHIVE = "historicalArchive"
    OBSOLETE = "obsolete"
    ONGOING = "onGoing"
    PLANNED = "planned"
    REQUIRED = "required"
    UNDERDEVELOPMENT = "underDevelopment"
    FINAL = "final"
    PENDING = "pending"
    RETIRED = "retired"
    SUPERSEDED = "superseded"
    TENTATIVE = "tentative"
    VALID = "valid"
    ACCEPTED = "accepted"
    NOTACCEPTED = "notAccepted"
    WITHDRAWN = "withDrawn"
    PROPOSED = "proposed"
    DEPRECATED = "deprecated"

    @property
    def metadata(self) -> dict:
        return {
            "ili2py": {},
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_ProgressCode",
                "kind": "Enumeration",
                "meta_attributes": {},
            },
        }


class MD_SpatialRepresentationTypeCode(str, Enum):
    """
    method used to represent geographic information in the dataset
    """

    VECTOR = "vector"
    GRID = "grid"
    TEXTTABLE = "textTable"
    TIN = "tin"
    STEREOMODEL = "stereoModel"
    VIDEO = "video"

    @property
    def metadata(self) -> dict:
        return {
            "ili2py": {},
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_SpatialRepresentationTypeCode",
                "kind": "Enumeration",
                "meta_attributes": {},
            },
        }


class MD_CharacterSetCode(str, Enum):
    """
    name of the character coding standard used for the resource
    """

    UCS2 = "ucs2"
    UCS4 = "ucs4"
    UTF7 = "utf7"
    UTF8 = "utf8"
    UTF16 = "utf16"
    A8859PART1 = "a8859part1"
    A8859PART2 = "a8859part2"
    A8859PART3 = "a8859part3"
    A8859PART4 = "a8859part4"
    A8859PART5 = "a8859part5"
    A8859PART6 = "a8859part6"
    A8859PART7 = "a8859part7"
    A8859PART8 = "a8859part8"
    A8859PART9 = "a8859part9"
    A8859PART10 = "a8859part10"
    A8859PART11 = "a8859part11"
    A8859PART13 = "a8859part13"
    A8859PART14 = "a8859part14"
    A8859PART15 = "a8859part15"
    A8859PART16 = "a8859part16"
    JIS = "jis"
    SHIFTJIS = "shiftJIS"
    EUCJP = "eucJP"
    USASCII = "usAscii"
    EBCDIC = "ebcdic"
    EUCKR = "eucKR"
    BIG5 = "big5"
    GB2312 = "GB2312"

    @property
    def metadata(self) -> dict:
        return {
            "ili2py": {},
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_CharacterSetCode",
                "kind": "Enumeration",
                "meta_attributes": {},
            },
        }


class MD_TopicCategoryCode(str, Enum):
    """
    high-level geographic data thematic classification to assist in the grouping and search of available geographic data sets. Can be used to group keywords as well. Listed examples are not exhaustive.  NOTE It is understood there are overlaps between general
    """

    FARMING = "farming"
    BIOTA = "biota"
    BOUNDARIES = "boundaries"
    CLIMATOLOGYMETEOROLOGYATMOSPHERE = "climatologyMeteorologyAtmosphere"
    ECONOMY = "economy"
    ELEVATION = "elevation"
    INLANDWATERS = "inlandWaters"
    ENVIRONMENT = "environment"
    GEOSCIENTIFICINFORMATION = "geoscientificInformation"
    HEALTH = "health"
    IMAGERYBASEMAPSEARTHCOVER = "imageryBaseMapsEarthCover"
    INTELLIGENCEMILITARY = "intelligenceMilitary"
    LOCATION = "location"
    OCEANS = "oceans"
    PLANNINGCADASTRE = "planningCadastre"
    SOCIETY = "society"
    STRUCTURE = "structure"
    TRANSPORTATION = "transportation"
    EXTRATERRESTRIAL = "extraTerrestrial"
    DISASTER = "disaster"
    UTILITIESCOMMUNICATION = "utilitiesCommunication"

    @property
    def metadata(self) -> dict:
        return {
            "ili2py": {},
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_TopicCategoryCode",
                "kind": "Enumeration",
                "meta_attributes": {},
            },
        }


class CI_DateTypeCode(str, Enum):
    """
    identification of when a given event occurred
    """

    CREATION = "creation"
    PUBLICATION = "publication"
    REVISION = "revision"
    EXPIRY = "expiry"
    LASTUPDATE = "lastUpdate"
    LASTREVISION = "lastRevision"
    NEXTUPDATE = "nextUpdate"
    UNAVAILABLE = "unavailable"
    INFORCE = "inForce"
    ADOPTED = "adopted"
    DEPRECATED = "deprecated"
    SUPERSEDED = "superseded"
    VALIDITYBEGINS = "validityBegins"
    VALIDITYEXPIRES = "validityExpires"
    RELEASED = "released"
    DISTRIBUTION = "distribution"

    @property
    def metadata(self) -> dict:
        return {
            "ili2py": {},
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_DateTypeCode",
                "kind": "Enumeration",
                "meta_attributes": {},
            },
        }


class CI_TelephoneTypeCode(str, Enum):
    VOICE = "voice"
    FACSIMILE = "facsimile"
    SMS = "sms"

    @property
    def metadata(self) -> dict:
        return {
            "ili2py": {},
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_TelephoneTypeCode",
                "kind": "Enumeration",
                "meta_attributes": {},
            },
        }


class CI_OnLineFunctionCode(str, Enum):
    """
    function performed by the resource
    """

    DOWNLOAD = "download"
    INFORMATION = "information"
    OFFLINEACCESS = "offlineAccess"
    ORDER = "order"
    SEARCH = "search"
    COMPLETEMETADATA = "completeMetadata"
    BROWSEGRAPHIC = "browseGraphic"
    UPLOAD = "upload"
    EMAILSERVICE = "emailService"
    BROWSING = "browsing"
    FILEACCESS = "fileAccess"

    @property
    def metadata(self) -> dict:
        return {
            "ili2py": {},
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_OnLineFunctionCode",
                "kind": "Enumeration",
                "meta_attributes": {},
            },
        }


class CI_RoleCode(str, Enum):
    """
    function performed by the responsible party
    """

    RESOURCEPROVIDER = "resourceProvider"
    CUSTODIAN = "custodian"
    OWNER = "owner"
    USER = "user"
    DISTRIBUTOR = "distributor"
    ORIGINATOR = "originator"
    POINTOFCONTACT = "pointOfContact"
    PRINCIPALINVESTIGATOR = "principalInvestigator"
    PROCESSOR = "processor"
    PUBLISHER = "publisher"
    AUTHOR = "author"
    SPONSOR = "sponsor"
    COAUTHOR = "coAuthor"
    COLLABORATOR = "collaborator"
    EDITOR = "editor"
    MEDIATOR = "mediator"
    RIGHTSHOLDER = "rightsHolder"
    CONTRIBUTOR = "contributor"
    FUNDER = "funder"
    STAKEHOLDER = "stakeholder"

    @property
    def metadata(self) -> dict:
        return {
            "ili2py": {},
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_RoleCode",
                "kind": "Enumeration",
                "meta_attributes": {},
            },
        }


@dataclass
class GM_PointType:

    c1: "float | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/geometry/1.0",
            "interlis": {
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": "Units.Angle_Degree",
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": False,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                    "precision": 5,
                    "min": -180.0,
                    "max": 180.0,
                },
            },
        },
    )
    c2: "float | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/geometry/1.0",
            "interlis": {
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": "Units.Angle_Degree",
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": False,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                    "precision": 5,
                    "min": -90.0,
                    "max": 90.0,
                },
            },
        },
    )


@dataclass
class GM_Point:
    class Meta:
        namespace = "http://www.interlis.ch/geometry/1.0"

    coord: GM_PointType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/geometry/1.0",
            "interlis": {},
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.GM_Point",
                "kind": "Enumeration",
                "meta_attributes": {},
            }
        }


@dataclass
class GM_PointARCType(GM_PointType):
    class Meta:
        namespace = "http://www.interlis.ch/geometry/1.0"

    """
    This is an intermediate class which simplifies parsing of XTF later.
    """
    a1: float | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/geometry/1.0",
            "interlis": {"meta_attributes": {}, "type_restrictions": {}},
        },
    )
    a2: float | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/geometry/1.0",
            "interlis": {"meta_attributes": {}, "type_restrictions": {}},
        },
    )
    r: float | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/geometry/1.0",
            "interlis": {"meta_attributes": {}, "type_restrictions": {}},
        },
    )


@dataclass
class GM_PointARC:
    class Meta:
        namespace = "http://www.interlis.ch/geometry/1.0"

    """
    This is an intermediate class which simplifies parsing of XTF later.
    """
    arc: GM_PointARCType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/geometry/1.0",
            "interlis": {"meta_attributes": {}, "type_restrictions": {}},
        },
    )


@dataclass
class GM_Object:
    class Meta:
        namespace = "http://www.interlis.ch/geometry/1.0"

    """
    """

    @dataclass
    class GM_ObjectBoundary:
        class Meta:
            namespace = "http://www.interlis.ch/geometry/1.0"

        @dataclass
        class GM_ObjectPolyline:
            class Meta:
                namespace = "http://www.interlis.ch/geometry/1.0"

            @dataclass
            class Segment:
                class Meta:
                    namespace = "http://www.interlis.ch/geometry/1.0"

                vertices: "list[GM_PointType | GM_PointARCType]" = field(
                    default_factory=list,
                    metadata={
                        "type": "Elements",
                        "choices": (
                            {
                                "name": "coord",
                                "type": GM_PointType,
                                "namespace": "http://www.interlis.ch/geometry/1.0",
                            },
                            {
                                "name": "arc",
                                "type": GM_PointARCType,
                                "namespace": "http://www.interlis.ch/geometry/1.0",
                            },
                        ),
                        "interlis": {"meta_attributes": {}},
                    },
                )

            polyline: Segment | None = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.interlis.ch/geometry/1.0",
                    "interlis": {"meta_attributes": {}},
                },
            )

        @dataclass
        class GM_ObjectPolylineInterior(GM_ObjectPolyline):
            pass

        @dataclass
        class GM_ObjectPolylineExterior(GM_ObjectPolyline):
            pass

        boundaries: list[GM_ObjectPolyline] = field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "type": GM_ObjectPolylineExterior,
                        "name": "exterior",
                        "namespace": "http://www.interlis.ch/geometry/1.0",
                    },
                    {
                        "type": GM_ObjectPolylineInterior,
                        "name": "interior",
                        "namespace": "http://www.interlis.ch/geometry/1.0",
                    },
                ),
                "interlis": {"meta_attributes": {}},
            },
        )

    surface: GM_ObjectBoundary | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/geometry/1.0",
            "interlis": {"meta_attributes": {}},
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.GM_Object",
                "kind": "LineType",
                "meta_attributes": {},
                "max_overlap": 1e-06,
                "straights": True,
                "arcs": True,
            }
        }


@dataclass
class DQ_DataQuality:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    MD_Metadata: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "MD_Metadata",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_MetadatadataQualityInfo.MD_Metadata",
                "reference_targets": ["eCH0271_1.eCH0271.CHE_MD_Metadata"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    scope: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "scope",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.DQ_DataQualityscope.scope",
                "reference_targets": ["eCH0271_1.eCH0271.MD_Scope"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.DQ_DataQuality",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class LI_Lineage:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    information about the events or source data used in constructing the data specified by the scope or lack of knowledge about lineage

    Args:
        statement:
        MD_Metadata:
    """

    @dataclass
    class LI_LineagestatementStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "Localisation_V2MultilingualMText | None" = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
                "name": "MultilingualMText",
                "interlis": {
                    "oid": "ili2py.Localisation_V2.MultilingualMText",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.LI_Lineage.statement.TYPE",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    statement: "LI_LineagestatementStruct | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "statement",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.LI_Lineage.statement",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    MD_Metadata: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "MD_Metadata",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_MetadataresourceLineage.MD_Metadata",
                "reference_targets": ["eCH0271_1.eCH0271.CHE_MD_Metadata"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                    "association_strongness": "Comp",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.LI_Lineage",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class MD_Constraints:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    restrictions on the access and use of a resource or metadata

    Args:
        useLimitation:
        MD_BrowseGraphic:
    """

    @dataclass
    class MD_ConstraintsuseLimitationStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "list[Localisation_V2MultilingualMText]" = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
                "name": "MultilingualMText",
                "interlis": {
                    "oid": "ili2py.Localisation_V2.MultilingualMText",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.MD_Constraints.useLimitation.TYPE",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    useLimitation: "list[MD_ConstraintsuseLimitationStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "useLimitation",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_Constraints.useLimitation",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    MD_BrowseGraphic: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "MD_BrowseGraphic",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_BrowseGraphicimageConstraints.MD_BrowseGraphic",
                "reference_targets": ["eCH0271_1.eCH0271.MD_BrowseGraphic"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "association_strongness": "Comp",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_Constraints",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class CHE_MD_LegalConstraints(MD_Constraints):

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    restrictions and legal prerequisites for accessing and using the resource

    Args:
        accessConstraints: access constraints applied to assure the protection of privacy or intellectual property, and any special restrictions or limitations on obtaining the resource
        useConstraints: constraints applied to assure the protection of privacy or intellectual property, and any special restrictions or limitations or warnings on using the resource
        otherConstraints:
    """

    @dataclass
    class CHE_MD_LegalConstraintsaccessConstraintsStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "MD_RestrictionCode | None" = field(
            default=None,
            metadata={
                "type": "Text",
                "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                "name": "struct_content",
                "interlis": {
                    "oid": "ili2py.eCH0271_1.eCH0271.MD_RestrictionCode",
                    "meta_attributes": {},
                    "type_restrictions": {
                        "mandatory": False,
                        "kind": None,
                        "format": None,
                        "unit": None,
                        "ref_sys": None,
                        "clockwise": None,
                        "circular": None,
                        "abstract": False,
                        "final": False,
                        "generic": None,
                        "super": None,
                        "type_related_type": False,
                        "multiplicity": {"min": 0, "max": 1},
                    },
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CHE_MD_LegalConstraints.accessConstraints.MVT",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    @dataclass
    class CHE_MD_LegalConstraintsuseConstraintsStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "MD_RestrictionCode | None" = field(
            default=None,
            metadata={
                "type": "Text",
                "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                "name": "struct_content",
                "interlis": {
                    "oid": "ili2py.eCH0271_1.eCH0271.MD_RestrictionCode",
                    "meta_attributes": {},
                    "type_restrictions": {
                        "mandatory": False,
                        "kind": None,
                        "format": None,
                        "unit": None,
                        "ref_sys": None,
                        "clockwise": None,
                        "circular": None,
                        "abstract": False,
                        "final": False,
                        "generic": None,
                        "super": None,
                        "type_related_type": False,
                        "multiplicity": {"min": 0, "max": 1},
                    },
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CHE_MD_LegalConstraints.useConstraints.MVT",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    @dataclass
    class CHE_MD_LegalConstraintsotherConstraintsStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "list[Localisation_V2MultilingualMText]" = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
                "name": "MultilingualMText",
                "interlis": {
                    "oid": "ili2py.Localisation_V2.MultilingualMText",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CHE_MD_LegalConstraints.otherConstraints.TYPE",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    accessConstraints: "list[CHE_MD_LegalConstraintsaccessConstraintsStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "accessConstraints",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_LegalConstraints.accessConstraints",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": None,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": None,
                    "final": None,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    useConstraints: "list[CHE_MD_LegalConstraintsuseConstraintsStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "useConstraints",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_LegalConstraints.useConstraints",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": None,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": None,
                    "final": None,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    otherConstraints: "list[CHE_MD_LegalConstraintsotherConstraintsStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "otherConstraints",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_LegalConstraints.otherConstraints",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_LegalConstraints",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class CHE_MD_MaintenanceInformation:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    information about the scope and frequency of updating

    Args:
        maintenanceAndUpdateFrequency: frequency with which changes and additions are made to the resource after the initial resource is completed
        maintenanceNote:
        MD_Identification:
    """

    @dataclass
    class CHE_MD_MaintenanceInformationmaintenanceNoteStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "list[Localisation_V2MultilingualMText]" = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
                "name": "MultilingualMText",
                "interlis": {
                    "oid": "ili2py.Localisation_V2.MultilingualMText",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CHE_MD_MaintenanceInformation.maintenanceNote.TYPE",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    maintenanceAndUpdateFrequency: "MD_MaintenanceFrequencyCode | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "maintenanceAndUpdateFrequency",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_MaintenanceInformation.maintenanceAndUpdateFrequency",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    maintenanceNote: "list[CHE_MD_MaintenanceInformationmaintenanceNoteStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "maintenanceNote",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_MaintenanceInformation.maintenanceNote",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    MD_Identification: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "MD_Identification",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.resourceMaintenanceMD_Identification.MD_Identification",
                "reference_targets": ["eCH0271_1.eCH0271.MD_Identification"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "association_strongness": "Comp",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_MaintenanceInformation",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class MD_ContentInformation(ABC):

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    description of the content of a dataset

    Args:
        MD_Metadata:
    """
    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    MD_Metadata: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "MD_Metadata",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.contentInfoMD_Metadata.MD_Metadata",
                "reference_targets": ["eCH0271_1.eCH0271.CHE_MD_Metadata"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "association_strongness": "Comp",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_ContentInformation",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class MD_DigitalTransferOptions:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    technical means and media by which a resource is obtained from the distributor

    Args:
        MD_Distribution:
    """
    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    MD_Distribution: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "MD_Distribution",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_DistributiontransferOptions.MD_Distribution",
                "reference_targets": ["eCH0271_1.eCH0271.MD_Distribution"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "association_strongness": "Comp",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_DigitalTransferOptions",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class TM_Primitive:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    begin: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "begin",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.TM_Primitive.begin",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": '"Year"-"Month"-"Day"T"Hours/2":"Minutes":"Seconds"',
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": "eCH0271_1.eCH0271.DateTime",
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                    "struct": "INTERLIS.GregorianDateTime",
                    "min": "1582-1-1T0:0:0.0",
                    "max": "2999-12-31T23:59:59.999",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    end: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "end",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.TM_Primitive.end",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": '"Year"-"Month"-"Day"T"Hours/2":"Minutes":"Seconds"',
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": "INTERLIS.XMLDateTime",
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "struct": "INTERLIS.GregorianDateTime",
                    "min": "1582-1-1T0:0:0.0",
                    "max": "2999-12-31T23:59:59.999",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.TM_Primitive",
                "kind": "Structure",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class EX_TemporalExtent:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    time period covered by the content of the dataset

    Args:
        extent:
    """

    @dataclass
    class EX_TemporalExtentextentStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "TM_Primitive | None" = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                "name": "TM_Primitive",
                "interlis": {
                    "oid": "ili2py.eCH0271_1.eCH0271.TM_Primitive",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.EX_TemporalExtent.extent.TYPE",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    extent: "EX_TemporalExtentextentStruct | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "extent",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.EX_TemporalExtent.extent",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.EX_TemporalExtent",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class MD_Distributor:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    information about the distributor

    Args:
        distributorContact: party from whom the resource may be obtained. This list need not be exhaustive
    """
    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    distributorContact: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "distributorContact",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_DistributordistributorContact.distributorContact",
                "reference_targets": ["eCH0271_1.eCH0271.CI_Responsibility"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_Distributor",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class MD_FeatureCatalogueDescription(MD_ContentInformation):

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    information identifying the feature catalogue

    """
    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_FeatureCatalogueDescription",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class CHE_MD_Appraisal_AAP:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    class CHE_MD_Appraisal_AAPappraisalOfArchivalValueEnum(str, Enum):
        A = "A"
        N = "N"
        S = "S"

        @property
        def metadata(self) -> dict:
            return {
                "ili2py": {},
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CHE_MD_Appraisal_AAP.appraisalOfArchivalValue_ENUM",
                    "kind": "Enumeration",
                    "meta_attributes": {},
                },
            }

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    durationOfConservation: "int | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "durationOfConservation",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_Appraisal_AAP.durationOfConservation",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": False,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": "eCH0271_1.eCH0271.Integer",
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                    "min": -10000000000,
                    "max": 10000000000,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    commentOnDurationOfConservation: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "commentOnDurationOfConservation",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_Appraisal_AAP.commentOnDurationOfConservation",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "max_length": 256,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    appraisalOfArchivalValue: "CHE_MD_Appraisal_AAPappraisalOfArchivalValueEnum | None" = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                "name": "appraisalOfArchivalValue",
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CHE_MD_Appraisal_AAP.appraisalOfArchivalValue",
                    "meta_attributes": {},
                    "type_restrictions": {
                        "mandatory": True,
                        "kind": None,
                        "format": None,
                        "unit": None,
                        "ref_sys": None,
                        "clockwise": None,
                        "circular": None,
                        "abstract": False,
                        "final": False,
                        "generic": False,
                        "super": "eCH0271_1.eCH0271.CHE_AppraisalOfArchivalValueCode",
                        "type_related_type": False,
                        "multiplicity": {"min": 1, "max": 1},
                    },
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )
    )
    reasonForArchivingValue: "CHE_ReasonForArchivingValueCode | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "reasonForArchivingValue",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_Appraisal_AAP.reasonForArchivingValue",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    commentOnArchivalValue: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "commentOnArchivalValue",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_Appraisal_AAP.commentOnArchivalValue",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "max_length": 256,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_Appraisal_AAP",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class CHE_MD_BasicGeodataInformation:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    @dataclass
    class CHE_MD_BasicGeodataInformationbasicGeodataTypeStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "CHE_MD_BasicGeodataTypeCode | None" = field(
            default=None,
            metadata={
                "type": "Text",
                "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                "name": "struct_content",
                "interlis": {
                    "oid": "ili2py.eCH0271_1.eCH0271.CHE_MD_BasicGeodataTypeCode",
                    "meta_attributes": {},
                    "type_restrictions": {
                        "mandatory": False,
                        "kind": None,
                        "format": None,
                        "unit": None,
                        "ref_sys": None,
                        "clockwise": None,
                        "circular": None,
                        "abstract": False,
                        "final": False,
                        "generic": None,
                        "super": None,
                        "type_related_type": False,
                        "multiplicity": {"min": 0, "max": 1},
                    },
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CHE_MD_BasicGeodataInformation.basicGeodataType.MVT",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    basicGeodataID: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "basicGeodataID",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_BasicGeodataInformation.basicGeodataID",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": "eCH0271_1.eCH0271.CharacterString",
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                    "max_length": 256,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    basicGeodataLegalLevel: "CHE_MD_LevelCode | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "basicGeodataLegalLevel",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_BasicGeodataInformation.basicGeodataLegalLevel",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    basicGeodataResponsibilityLevel: "CHE_MD_LevelCode | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "basicGeodataResponsibilityLevel",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_BasicGeodataInformation.basicGeodataResponsibilityLevel",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    basicGeodataAccessLevel: "CHE_MD_BasicGeodataAccessLevelCode | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "basicGeodataAccessLevel",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_BasicGeodataInformation.basicGeodataAccessLevel",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    basicGeodataType: "list[CHE_MD_BasicGeodataInformationbasicGeodataTypeStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "basicGeodataType",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_BasicGeodataInformation.basicGeodataType",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": None,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": None,
                    "final": None,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_BasicGeodataInformation",
                "kind": "Structure",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class CHE_MD_Legislation:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    @dataclass
    class CHE_MD_LegislationcountryStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "InternationalCodes_V2CountryCode_ISO3166_1 | None" = field(
            default=None,
            metadata={
                "type": "Text",
                "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                "name": "struct_content",
                "interlis": {
                    "oid": "ili2py.InternationalCodes_V2.CountryCode_ISO3166_1",
                    "meta_attributes": {},
                    "type_restrictions": {
                        "mandatory": False,
                        "kind": None,
                        "format": None,
                        "unit": None,
                        "ref_sys": None,
                        "clockwise": None,
                        "circular": None,
                        "abstract": False,
                        "final": False,
                        "generic": None,
                        "super": None,
                        "type_related_type": False,
                        "multiplicity": {"min": 0, "max": 1},
                    },
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CHE_MD_Legislation.country.MVT",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    @dataclass
    class CHE_MD_LegislationlanguageStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "InternationalCodes_V2LanguageCode_ISO639_1 | None" = field(
            default=None,
            metadata={
                "type": "Text",
                "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                "name": "struct_content",
                "interlis": {
                    "oid": "ili2py.InternationalCodes_V2.LanguageCode_ISO639_1",
                    "meta_attributes": {},
                    "type_restrictions": {
                        "mandatory": False,
                        "kind": None,
                        "format": None,
                        "unit": None,
                        "ref_sys": None,
                        "clockwise": None,
                        "circular": None,
                        "abstract": False,
                        "final": False,
                        "generic": None,
                        "super": None,
                        "type_related_type": False,
                        "multiplicity": {"min": 0, "max": 1},
                    },
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CHE_MD_Legislation.language.MVT",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    @dataclass
    class CHE_MD_LegislationlegislationTypeStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "CHE_CI_LegislationTypeCode | None" = field(
            default=None,
            metadata={
                "type": "Text",
                "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                "name": "struct_content",
                "interlis": {
                    "oid": "ili2py.eCH0271_1.eCH0271.CHE_CI_LegislationTypeCode",
                    "meta_attributes": {},
                    "type_restrictions": {
                        "mandatory": False,
                        "kind": None,
                        "format": None,
                        "unit": None,
                        "ref_sys": None,
                        "clockwise": None,
                        "circular": None,
                        "abstract": False,
                        "final": False,
                        "generic": None,
                        "super": None,
                        "type_related_type": False,
                        "multiplicity": {"min": 0, "max": 1},
                    },
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CHE_MD_Legislation.legislationType.MVT",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    @dataclass
    class CHE_MD_LegislationinternalReferenceStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "str | None" = field(
            default=None,
            metadata={
                "type": "Text",
                "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                "name": "struct_content",
                "interlis": {
                    "oid": "ili2py.eCH0271_1.eCH0271.CharacterString",
                    "meta_attributes": {},
                    "type_restrictions": {
                        "mandatory": False,
                        "kind": None,
                        "format": None,
                        "unit": None,
                        "ref_sys": None,
                        "clockwise": None,
                        "circular": None,
                        "abstract": False,
                        "final": False,
                        "generic": None,
                        "super": None,
                        "type_related_type": False,
                        "multiplicity": {"min": 0, "max": 1},
                        "max_length": 256,
                    },
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CHE_MD_Legislation.internalReference.MVT",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    @dataclass
    class CHE_MD_LegislationlegislationLevelStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "CHE_MD_LevelCode | None" = field(
            default=None,
            metadata={
                "type": "Text",
                "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                "name": "struct_content",
                "interlis": {
                    "oid": "ili2py.eCH0271_1.eCH0271.CHE_MD_LevelCode",
                    "meta_attributes": {},
                    "type_restrictions": {
                        "mandatory": False,
                        "kind": None,
                        "format": None,
                        "unit": None,
                        "ref_sys": None,
                        "clockwise": None,
                        "circular": None,
                        "abstract": False,
                        "final": False,
                        "generic": None,
                        "super": None,
                        "type_related_type": False,
                        "multiplicity": {"min": 0, "max": 1},
                    },
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CHE_MD_Legislation.legislationLevel.MVT",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    @dataclass
    class CHE_MD_LegislationlegislationAcronymStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "str | None" = field(
            default=None,
            metadata={
                "type": "Text",
                "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                "name": "struct_content",
                "interlis": {
                    "oid": "ili2py.eCH0271_1.eCH0271.CharacterString",
                    "meta_attributes": {},
                    "type_restrictions": {
                        "mandatory": False,
                        "kind": None,
                        "format": None,
                        "unit": None,
                        "ref_sys": None,
                        "clockwise": None,
                        "circular": None,
                        "abstract": False,
                        "final": False,
                        "generic": None,
                        "super": None,
                        "type_related_type": False,
                        "multiplicity": {"min": 0, "max": 1},
                        "max_length": 256,
                    },
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CHE_MD_Legislation.legislationAcronym.MVT",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    country: "list[CHE_MD_LegislationcountryStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "country",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_Legislation.country",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": None,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": None,
                    "final": None,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": None},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    language: "list[CHE_MD_LegislationlanguageStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "language",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_Legislation.language",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": None,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": None,
                    "final": None,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    legislationType: "list[CHE_MD_LegislationlegislationTypeStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "legislationType",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_Legislation.legislationType",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": None,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": None,
                    "final": None,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    internalReference: "list[CHE_MD_LegislationinternalReferenceStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "internalReference",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_Legislation.internalReference",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": None,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": None,
                    "final": None,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    legislationLevel: "list[CHE_MD_LegislationlegislationLevelStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "legislationLevel",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_Legislation.legislationLevel",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": None,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": None,
                    "final": None,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    legislationAcronym: "list[CHE_MD_LegislationlegislationAcronymStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "legislationAcronym",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_Legislation.legislationAcronym",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": None,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": None,
                    "final": None,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_Legislation",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class CI_Address:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    location of the responsible individual or organization

    Args:
        deliveryPoint:
        postalCode: ZIP or other postal code
        city: city of the location
        administrativeArea: state, province of the location
        country: country of the physical address
        electronicMailAddress:
        CI_ResponsibleParty:
    """

    @dataclass
    class CI_AddressdeliveryPointStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "str | None" = field(
            default=None,
            metadata={
                "type": "Text",
                "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                "name": "struct_content",
                "interlis": {
                    "oid": "ili2py.eCH0271_1.eCH0271.CharacterString",
                    "meta_attributes": {},
                    "type_restrictions": {
                        "mandatory": False,
                        "kind": None,
                        "format": None,
                        "unit": None,
                        "ref_sys": None,
                        "clockwise": None,
                        "circular": None,
                        "abstract": False,
                        "final": False,
                        "generic": None,
                        "super": None,
                        "type_related_type": False,
                        "multiplicity": {"min": 0, "max": 1},
                        "max_length": 256,
                    },
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CI_Address.deliveryPoint.MVT",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    @dataclass
    class CI_AddresselectronicMailAddressStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "str | None" = field(
            default=None,
            metadata={
                "type": "Text",
                "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                "name": "struct_content",
                "interlis": {
                    "oid": "ili2py.eCH0271_1.eCH0271.CharacterString",
                    "meta_attributes": {},
                    "type_restrictions": {
                        "mandatory": False,
                        "kind": None,
                        "format": None,
                        "unit": None,
                        "ref_sys": None,
                        "clockwise": None,
                        "circular": None,
                        "abstract": False,
                        "final": False,
                        "generic": None,
                        "super": None,
                        "type_related_type": False,
                        "multiplicity": {"min": 0, "max": 1},
                        "max_length": 256,
                    },
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CI_Address.electronicMailAddress.MVT",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    deliveryPoint: "list[CI_AddressdeliveryPointStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "deliveryPoint",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Address.deliveryPoint",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": None,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": None,
                    "final": None,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    postalCode: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "postalCode",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Address.postalCode",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "max_length": 256,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    city: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "city",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Address.city",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "max_length": 256,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    administrativeArea: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "administrativeArea",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Address.administrativeArea",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "max_length": 256,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    country: "InternationalCodes_V2CountryCode_ISO3166_1 | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "country",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Address.country",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    electronicMailAddress: "list[CI_AddresselectronicMailAddressStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "electronicMailAddress",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Address.electronicMailAddress",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": None,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": None,
                    "final": None,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    CI_ResponsibleParty: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "CI_ResponsibleParty",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_ResponsiblePartyaddress.CI_ResponsibleParty",
                "reference_targets": ["eCH0271_1.eCH0271.CI_Contact"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "association_strongness": "Comp",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Address",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class MD_ApplicationSchemaInformation:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    Information about the application schema used to build the dataset

    Args:
        schemaLanguage:
        constraintLanguage:
    """
    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    schemaLanguage: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "schemaLanguage",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_ApplicationSchemaInformation.schemaLanguage",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": "eCH0271_1.eCH0271.CharacterString",
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                    "max_length": 256,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    constraintLanguage: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "constraintLanguage",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_ApplicationSchemaInformation.constraintLanguage",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": "eCH0271_1.eCH0271.CharacterString",
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                    "max_length": 256,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_ApplicationSchemaInformation",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class MD_BrowseGraphic:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    graphic that provides an illustration of the dataset (should include a legend for the graphic)

    Args:
        fileName:
        fileType:
        fileDescription:
        MD_Identification:
        CI_Organisation:
    """

    @dataclass
    class MD_BrowseGraphicfileDescriptionStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "Localisation_V2MultilingualMText | None" = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
                "name": "MultilingualMText",
                "interlis": {
                    "oid": "ili2py.Localisation_V2.MultilingualMText",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.MD_BrowseGraphic.fileDescription.TYPE",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    fileName: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "fileName",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_BrowseGraphic.fileName",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": "eCH0271_1.eCH0271.CharacterString",
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                    "max_length": 256,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    fileType: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "fileType",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_BrowseGraphic.fileType",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "max_length": 256,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    fileDescription: "MD_BrowseGraphicfileDescriptionStruct | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "fileDescription",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_BrowseGraphic.fileDescription",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    MD_Identification: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "MD_Identification",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.graphicOverviewMD_Identification.MD_Identification",
                "reference_targets": ["eCH0271_1.eCH0271.MD_Identification"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "association_strongness": "Comp",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    CI_Organisation: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "CI_Organisation",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Organisationlogo.CI_Organisation",
                "reference_targets": ["eCH0271_1.eCH0271.CHE_CI_Organisation"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "association_strongness": "Comp",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_BrowseGraphic",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class MD_Format:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    description of the computer language construct that specifies the representation of data objects in a record, file, message, storage device or transmission channel

    Args:
        amendmentNumber:
        MD_DigitalTransferOptions:
        formatSpecificationCitation:
    """
    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    amendmentNumber: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "amendmentNumber",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_Format.amendmentNumber",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "max_length": 256,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    MD_DigitalTransferOptions: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "MD_DigitalTransferOptions",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_DigitalTransferOptionsdistributionFormat.MD_DigitalTransferOptions",
                "reference_targets": ["eCH0271_1.eCH0271.MD_DigitalTransferOptions"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "association_strongness": "Comp",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    formatSpecificationCitation: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "formatSpecificationCitation",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_FormatformatSpecificationCitation.formatSpecificationCitation",
                "reference_targets": ["eCH0271_1.eCH0271.CI_Citation"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_Format",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class MD_Identification(ABC):

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    basic information required to uniquely identify a resource or resources

    Args:
        status: status of the resource(s)
        spatialRepresentationType:
        topicCategory:
        abstract: brief narrative summary of the content of the resource(s)
        MD_Metadata:
    """

    @dataclass
    class MD_IdentificationstatusStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "MD_ProgressCode | None" = field(
            default=None,
            metadata={
                "type": "Text",
                "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                "name": "struct_content",
                "interlis": {
                    "oid": "ili2py.eCH0271_1.eCH0271.MD_ProgressCode",
                    "meta_attributes": {},
                    "type_restrictions": {
                        "mandatory": False,
                        "kind": None,
                        "format": None,
                        "unit": None,
                        "ref_sys": None,
                        "clockwise": None,
                        "circular": None,
                        "abstract": False,
                        "final": False,
                        "generic": None,
                        "super": None,
                        "type_related_type": False,
                        "multiplicity": {"min": 0, "max": 1},
                    },
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.MD_Identification.status.MVT",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    @dataclass
    class MD_IdentificationspatialRepresentationTypeStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "MD_SpatialRepresentationTypeCode | None" = field(
            default=None,
            metadata={
                "type": "Text",
                "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                "name": "struct_content",
                "interlis": {
                    "oid": "ili2py.eCH0271_1.eCH0271.MD_SpatialRepresentationTypeCode",
                    "meta_attributes": {},
                    "type_restrictions": {
                        "mandatory": False,
                        "kind": None,
                        "format": None,
                        "unit": None,
                        "ref_sys": None,
                        "clockwise": None,
                        "circular": None,
                        "abstract": False,
                        "final": False,
                        "generic": None,
                        "super": None,
                        "type_related_type": False,
                        "multiplicity": {"min": 0, "max": 1},
                    },
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.MD_Identification.spatialRepresentationType.MVT",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    @dataclass
    class MD_IdentificationtopicCategoryStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "MD_TopicCategoryCode | None" = field(
            default=None,
            metadata={
                "type": "Text",
                "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                "name": "struct_content",
                "interlis": {
                    "oid": "ili2py.eCH0271_1.eCH0271.MD_TopicCategoryCode",
                    "meta_attributes": {},
                    "type_restrictions": {
                        "mandatory": False,
                        "kind": None,
                        "format": None,
                        "unit": None,
                        "ref_sys": None,
                        "clockwise": None,
                        "circular": None,
                        "abstract": False,
                        "final": False,
                        "generic": None,
                        "super": None,
                        "type_related_type": False,
                        "multiplicity": {"min": 0, "max": 1},
                    },
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.MD_Identification.topicCategory.MVT",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    @dataclass
    class MD_IdentificationabstractStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "Localisation_V2MultilingualMText | None" = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
                "name": "MultilingualMText",
                "interlis": {
                    "oid": "ili2py.Localisation_V2.MultilingualMText",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.MD_Identification.abstract.TYPE",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    status: "list[MD_IdentificationstatusStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "status",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_Identification.status",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": None,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": None,
                    "final": None,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    spatialRepresentationType: "list[MD_IdentificationspatialRepresentationTypeStruct]" = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                "name": "spatialRepresentationType",
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.MD_Identification.spatialRepresentationType",
                    "meta_attributes": {},
                    "type_restrictions": {
                        "mandatory": None,
                        "kind": None,
                        "format": None,
                        "unit": None,
                        "ref_sys": None,
                        "clockwise": None,
                        "circular": None,
                        "abstract": None,
                        "final": None,
                        "generic": None,
                        "super": None,
                        "type_related_type": False,
                        "multiplicity": {"min": 0, "max": None},
                    },
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )
    )
    topicCategory: "list[MD_IdentificationtopicCategoryStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "topicCategory",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_Identification.topicCategory",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": None,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": None,
                    "final": None,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    abstract: "MD_IdentificationabstractStruct | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "abstract",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_Identification.abstract",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    MD_Metadata: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "MD_Metadata",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_MetadataidentificationInfo.MD_Metadata",
                "reference_targets": ["eCH0271_1.eCH0271.CHE_MD_Metadata"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "association_strongness": "Comp",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_Identification",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class MD_SecurityConstraints(MD_Constraints):

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    handling restrictions imposed on the resource for national security or similar security concerns

    Args:
        classification: name of the handling restrictions on the resource
        classificationSystem: name of the classification system
    """

    class MD_SecurityConstraintsclassificationEnum(str, Enum):
        UNCLASSIFIED = "unclassified"
        RESTRICTED = "restricted"
        CONFIDENTIAL = "confidential"
        SECRET = "secret"
        TOPSECRET = "topSecret"
        SENSITIVEBUTUNCLASSIFIED = "sensitiveButUnclassified"
        FOROFFICIALUSEONLY = "forOfficialUseOnly"
        PROTECTED = "protected"
        LIMITEDDISTRIBUTION = "limitedDistribution"

        @property
        def metadata(self) -> dict:
            return {
                "ili2py": {},
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.MD_SecurityConstraints.classification_ENUM",
                    "kind": "Enumeration",
                    "meta_attributes": {},
                },
            }

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    classification: "MD_SecurityConstraintsclassificationEnum | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "classification",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_SecurityConstraints.classification",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": "eCH0271_1.eCH0271.MD_ClassificationCode",
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    classificationSystem: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "classificationSystem",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_SecurityConstraints.classificationSystem",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "max_length": 256,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_SecurityConstraints",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class PT_Locale:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    class PT_LocalelanguageEnum(str, Enum):
        DE = "de"
        FR = "fr"
        IT = "it"
        RM = "rm"
        EN = "en"
        AA = "aa"
        AB = "ab"
        AF = "af"
        AM = "am"
        AR = "ar"
        AS = "as"
        AY = "ay"
        AZ = "az"
        BA = "ba"
        BE = "be"
        BG = "bg"
        BH = "bh"
        BI = "bi"
        BN = "bn"
        BO = "bo"
        BR = "br"
        CA = "ca"
        CO = "co"
        CS = "cs"
        CY = "cy"
        DA = "da"
        DZ = "dz"
        EL = "el"
        EO = "eo"
        ES = "es"
        ET = "et"
        EU = "eu"
        FA = "fa"
        FI = "fi"
        FJ = "fj"
        FO = "fo"
        FY = "fy"
        GA = "ga"
        GD = "gd"
        GL = "gl"
        GN = "gn"
        GU = "gu"
        HA = "ha"
        HE = "he"
        HI = "hi"
        HR = "hr"
        HU = "hu"
        HY = "hy"
        IA = "ia"
        ID = "id"
        IE = "ie"
        IK = "ik"
        IS = "is"
        IU = "iu"
        JA = "ja"
        JW = "jw"
        KA = "ka"
        KK = "kk"
        KL = "kl"
        KM = "km"
        KN = "kn"
        KO = "ko"
        KS = "ks"
        KU = "ku"
        KY = "ky"
        LA = "la"
        LN = "ln"
        LO = "lo"
        LT = "lt"
        LV = "lv"
        MG = "mg"
        MI = "mi"
        MK = "mk"
        ML = "ml"
        MN = "mn"
        MO = "mo"
        MR = "mr"
        MS = "ms"
        MT = "mt"
        MY = "my"
        NA = "na"
        NE = "ne"
        NL = "nl"
        NO = "no"
        OC = "oc"
        OM = "om"
        OR = "or"
        PA = "pa"
        PL = "pl"
        PS = "ps"
        PT = "pt"
        QU = "qu"
        RN = "rn"
        RO = "ro"
        RU = "ru"
        RW = "rw"
        SA = "sa"
        SD = "sd"
        SG = "sg"
        SH = "sh"
        SI = "si"
        SK = "sk"
        SL = "sl"
        SM = "sm"
        SN = "sn"
        SO = "so"
        SQ = "sq"
        SR = "sr"
        SS = "ss"
        ST = "st"
        SU = "su"
        SV = "sv"
        SW = "sw"
        TA = "ta"
        TE = "te"
        TG = "tg"
        TH = "th"
        TI = "ti"
        TK = "tk"
        TL = "tl"
        TN = "tn"
        TO = "to"
        TR = "tr"
        TS = "ts"
        TT = "tt"
        TW = "tw"
        UG = "ug"
        UK = "uk"
        UR = "ur"
        UZ = "uz"
        VI = "vi"
        VO = "vo"
        WO = "wo"
        XH = "xh"
        YI = "yi"
        YO = "yo"
        ZA = "za"
        ZH = "zh"
        ZU = "zu"

        @property
        def metadata(self) -> dict:
            return {
                "ili2py": {},
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.PT_Locale.language_ENUM",
                    "kind": "Enumeration",
                    "meta_attributes": {},
                },
            }

    language: "PT_LocalelanguageEnum | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "language",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.PT_Locale.language",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": "InternationalCodes_V2.LanguageCode_ISO639_1",
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    country: "InternationalCodes_V2CountryCode_ISO3166_1 | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "country",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.PT_Locale.country",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    characterEncoding: "MD_CharacterSetCode | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "characterEncoding",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.PT_Locale.characterEncoding",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.PT_Locale",
                "kind": "Structure",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class SV_OperationMetadata:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    @dataclass
    class SV_OperationMetadatadistributedComputingPlatformStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "DCPList | None" = field(
            default=None,
            metadata={
                "type": "Text",
                "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                "name": "struct_content",
                "interlis": {
                    "oid": "ili2py.eCH0271_1.eCH0271.DCPList",
                    "meta_attributes": {},
                    "type_restrictions": {
                        "mandatory": False,
                        "kind": None,
                        "format": None,
                        "unit": None,
                        "ref_sys": None,
                        "clockwise": None,
                        "circular": None,
                        "abstract": False,
                        "final": False,
                        "generic": None,
                        "super": None,
                        "type_related_type": False,
                        "multiplicity": {"min": 0, "max": 1},
                    },
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.SV_OperationMetadata.distributedComputingPlatform.MVT",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    @dataclass
    class SV_OperationMetadataoperationDescriptionStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "Localisation_V2MultilingualMText | None" = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
                "name": "MultilingualMText",
                "interlis": {
                    "oid": "ili2py.Localisation_V2.MultilingualMText",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.SV_OperationMetadata.operationDescription.TYPE",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    operationName: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "operationName",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.SV_OperationMetadata.operationName",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": "eCH0271_1.eCH0271.CharacterString",
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                    "max_length": 256,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    distributedComputingPlatform: (
        "list[SV_OperationMetadatadistributedComputingPlatformStruct]"
    ) = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "distributedComputingPlatform",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.SV_OperationMetadata.distributedComputingPlatform",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": None,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": None,
                    "final": None,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": None},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    invocationName: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "invocationName",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.SV_OperationMetadata.invocationName",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "max_length": 256,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    operationDescription: "SV_OperationMetadataoperationDescriptionStruct | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "operationDescription",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.SV_OperationMetadata.operationDescription",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.SV_OperationMetadata",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class MD_AssociatedResource:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    class MD_AssociatedResourceassociationTypeEnum(str, Enum):
        CROSSREFERENCE = "crossReference"
        LARGERWORKCITATION = "largerWorkCitation"
        PARTOFSEAMLESSDATABASE = "partOfSeamlessDatabase"
        STEREOMATE = "stereoMate"
        ISCOMPOSEDOF = "isComposedOf"
        COLLECTIVETITLE = "collectiveTitle"
        SERIES = "series"
        DEPENDENCY = "dependency"
        REVISIONOF = "revisionOf"
        ISTEMPORALSTATEOF = "isTemporalStateOf"
        ISDESCRIPTIONOF = "isDescriptionOf"
        ISDESCRIBEDBY = "isDescribedBy"

        @property
        def metadata(self) -> dict:
            return {
                "ili2py": {},
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.MD_AssociatedResource.associationType_ENUM",
                    "kind": "Enumeration",
                    "meta_attributes": {},
                },
            }

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    associationType: "MD_AssociatedResourceassociationTypeEnum | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "associationType",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_AssociatedResource.associationType",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": "eCH0271_1.eCH0271.CHE_DS_AssociationTypeCode",
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_AssociatedResource",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class MD_Identifier:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    class providing the unique coded value within a namespace

    Args:
        code:
        codeSpace:
        version:
        description:
        authority: the person or party responsible for maintenance of that namespace
    """

    @dataclass
    class MD_IdentifiercodeStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "Localisation_V2MultilingualMText | None" = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
                "name": "MultilingualMText",
                "interlis": {
                    "oid": "ili2py.Localisation_V2.MultilingualMText",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.MD_Identifier.code.TYPE",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    @dataclass
    class MD_IdentifierdescriptionStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "Localisation_V2MultilingualText | None" = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
                "name": "MultilingualText",
                "interlis": {
                    "oid": "ili2py.Localisation_V2.MultilingualText",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.MD_Identifier.description.TYPE",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    code: "MD_IdentifiercodeStruct | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "code",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_Identifier.code",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    codeSpace: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "codeSpace",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_Identifier.codeSpace",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "max_length": 256,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    version: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "version",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_Identifier.version",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "max_length": 256,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    description: "MD_IdentifierdescriptionStruct | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "description",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_Identifier.description",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    authority: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "authority",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.authorityMD_Identifier.authority",
                "reference_targets": ["eCH0271_1.eCH0271.CI_Citation"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_Identifier",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class MD_StandardOrderProcess:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    common ways in which the resource may be obtained or received, and related instructions and fee information

    Args:
        fees: fees and terms for retrieving the resource.  Include monetary units (as specified in ISO 4217)
    """
    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    fees: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "fees",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_StandardOrderProcess.fees",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "max_length": 256,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_StandardOrderProcess",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class CI_Date:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    reference date and event used to describe it

    Args:
        date: reference date for the cited resource
        dateType: event used for reference date
    """

    class CI_DatedateTypeEnum(str, Enum):
        CREATION = "creation"
        PUBLICATION = "publication"
        REVISION = "revision"
        EXPIRY = "expiry"
        LASTUPDATE = "lastUpdate"
        LASTREVISION = "lastRevision"
        NEXTUPDATE = "nextUpdate"
        UNAVAILABLE = "unavailable"
        INFORCE = "inForce"
        ADOPTED = "adopted"
        DEPRECATED = "deprecated"
        SUPERSEDED = "superseded"
        VALIDITYBEGINS = "validityBegins"
        VALIDITYEXPIRES = "validityExpires"
        RELEASED = "released"
        DISTRIBUTION = "distribution"

        @property
        def metadata(self) -> dict:
            return {
                "ili2py": {},
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CI_Date.dateType_ENUM",
                    "kind": "Enumeration",
                    "meta_attributes": {},
                },
            }

    date: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "date",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Date.date",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": '"Year"-"Month"-"Day"T"Hours/2":"Minutes":"Seconds"',
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": "eCH0271_1.eCH0271.DateTime",
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                    "struct": "INTERLIS.GregorianDateTime",
                    "min": "1582-1-1T0:0:0.0",
                    "max": "2999-12-31T23:59:59.999",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    dateType: "CI_DatedateTypeEnum | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "dateType",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Date.dateType",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": "eCH0271_1.eCH0271.CI_DateTypeCode",
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Date",
                "kind": "Structure",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class CHE_MD_Metadata:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    root entity which defines metadata about a resource or resources

    Args:
        defaultLocale: language used for documenting metadata
        otherLocale:
        dateInfo:
        parentMetadata:
    """

    @dataclass
    class CHE_MD_MetadatadefaultLocaleStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "PT_Locale | None" = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                "name": "PT_Locale",
                "interlis": {
                    "oid": "ili2py.eCH0271_1.eCH0271.PT_Locale",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CHE_MD_Metadata.defaultLocale.TYPE",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    @dataclass
    class CHE_MD_MetadataotherLocaleStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "list[PT_Locale]" = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                "name": "PT_Locale",
                "interlis": {
                    "oid": "ili2py.eCH0271_1.eCH0271.PT_Locale",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CHE_MD_Metadata.otherLocale.TYPE",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    @dataclass
    class CHE_MD_MetadatadateInfoStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "list[CI_Date]" = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                "name": "CI_Date",
                "interlis": {
                    "oid": "ili2py.eCH0271_1.eCH0271.CI_Date",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CHE_MD_Metadata.dateInfo.TYPE",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    defaultLocale: "CHE_MD_MetadatadefaultLocaleStruct | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "defaultLocale",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_Metadata.defaultLocale",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    otherLocale: "list[CHE_MD_MetadataotherLocaleStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "otherLocale",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_Metadata.otherLocale",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    dateInfo: "list[CHE_MD_MetadatadateInfoStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "dateInfo",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_Metadata.dateInfo",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": None},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    parentMetadata: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "parentMetadata",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.parentIdentifierMD_Metadata.parentMetadata",
                "reference_targets": ["eCH0271_1.eCH0271.CI_Citation"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_Metadata",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class CI_Responsibility:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    identification of, and means of communication with, person(s) and organizations associated with the dataset

    Args:
        role:
    """

    class CI_ResponsibilityroleEnum(str, Enum):
        RESOURCEPROVIDER = "resourceProvider"
        CUSTODIAN = "custodian"
        OWNER = "owner"
        USER = "user"
        DISTRIBUTOR = "distributor"
        ORIGINATOR = "originator"
        POINTOFCONTACT = "pointOfContact"
        PRINCIPALINVESTIGATOR = "principalInvestigator"
        PROCESSOR = "processor"
        PUBLISHER = "publisher"
        AUTHOR = "author"
        SPONSOR = "sponsor"
        COAUTHOR = "coAuthor"
        COLLABORATOR = "collaborator"
        EDITOR = "editor"
        MEDIATOR = "mediator"
        RIGHTSHOLDER = "rightsHolder"
        CONTRIBUTOR = "contributor"
        FUNDER = "funder"
        STAKEHOLDER = "stakeholder"

        @property
        def metadata(self) -> dict:
            return {
                "ili2py": {},
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CI_Responsibility.role_ENUM",
                    "kind": "Enumeration",
                    "meta_attributes": {},
                },
            }

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    role: "CI_ResponsibilityroleEnum | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "role",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Responsibility.role",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": "eCH0271_1.eCH0271.CI_RoleCode",
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Responsibility",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class CI_Telephone:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    telephone numbers for contacting the responsible individual or organization

    Args:
        number: telephone number by which individuals can speak to the responsible organization or individual
        numberType: telephone number of a facsimile machine for the responsible organization or individual
        CI_ResponsibleParty:
    """
    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    number: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "number",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Telephone.number",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": "eCH0271_1.eCH0271.CharacterString",
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                    "max_length": 256,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    numberType: "CI_TelephoneTypeCode | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "numberType",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Telephone.numberType",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    CI_ResponsibleParty: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "CI_ResponsibleParty",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_ResponsiblePartyphone.CI_ResponsibleParty",
                "reference_targets": ["eCH0271_1.eCH0271.CI_Contact"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "association_strongness": "Comp",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Telephone",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class EX_GeographicExtent(ABC):

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    geographic area of the dataset

    Args:
        extentTypeCode: indication of whether  the bounding polygon encompasses an area covered by the data or an area where data is not present
    """
    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    extentTypeCode: "bool | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "extentTypeCode",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.EX_GeographicExtent.extentTypeCode",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.EX_GeographicExtent",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class EX_BoundingPolygon(EX_GeographicExtent):

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    boundary enclosing the dataset, expressed as the closed set of (x,y) coordinates of  the polygon (last point replicates first point)

    Args:
        polygon: sets of points defining the bounding polygon
    """

    @dataclass
    class EX_BoundingPolygonpolygonStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "GM_Object | None" = field(
            default=None,
            metadata={
                "type": "Text",
                "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                "name": "struct_content",
                "interlis": {
                    "oid": "ili2py.eCH0271_1.eCH0271.GM_Object",
                    "meta_attributes": {},
                    "type_restrictions": {
                        "mandatory": False,
                        "kind": None,
                        "format": None,
                        "unit": None,
                        "ref_sys": None,
                        "clockwise": None,
                        "circular": None,
                        "abstract": False,
                        "final": False,
                        "generic": None,
                        "super": None,
                        "type_related_type": False,
                        "multiplicity": {"min": 0, "max": 1},
                    },
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.EX_BoundingPolygon.polygon.MVT",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    polygon: "list[EX_BoundingPolygonpolygonStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "polygon",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.EX_BoundingPolygon.polygon",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": None,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": None,
                    "final": None,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": None},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.EX_BoundingPolygon",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class EX_VerticalExtent:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    vertical domain of dataset

    Args:
        minimumValue: lowest vertical extent contained in the dataset
        maximumValue: highest vertical extent contained in the dataset
        verticalCRSId:
    """
    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    minimumValue: "float | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "minimumValue",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.EX_VerticalExtent.minimumValue",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": False,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": "eCH0271_1.eCH0271.Real",
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                    "precision": 2,
                    "min": -9999999999.99,
                    "max": 9999999999.99,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    maximumValue: "float | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "maximumValue",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.EX_VerticalExtent.maximumValue",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": False,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": "eCH0271_1.eCH0271.Real",
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                    "precision": 2,
                    "min": -9999999999.99,
                    "max": 9999999999.99,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    verticalCRSId: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "verticalCRSId",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.verticalCRSIdEX_VerticalExtent.verticalCRSId",
                "reference_targets": ["eCH0271_1.eCH0271.MD_ReferenceSystem"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.EX_VerticalExtent",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class EX_GeographicBoundingBox(EX_GeographicExtent):

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    geographic position of the dataset NOTE This is only an approximate reference so specifying the co-ordinate system is unnecessary

    Args:
        northBoundLatitude: northern-most, coordinate of the limit of the dataset extent expressed in latitude in decimal degrees (positive north)
        southBoundLatitude: southern-most coordinate of the limit of the dataset extent, expressed in latitude in decimal degrees (positive north)
        eastBoundLongitude: eastern-most coordinate of the limit of the dataset extent, expressed in longitude in decimal degrees (positive east)
        westBoundLongitude: western-most coordinate of the limit of the dataset extent, expressed in longitude in decimal degrees (positive east)
    """
    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    northBoundLatitude: "float | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "northBoundLatitude",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.EX_GeographicBoundingBox.northBoundLatitude",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": "Units.Angle_Degree",
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": True,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": "eCH0271_1.eCH0271.Angle",
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                    "precision": 5,
                    "min": 0.0,
                    "max": 360.0,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    southBoundLatitude: "float | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "southBoundLatitude",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.EX_GeographicBoundingBox.southBoundLatitude",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": "Units.Angle_Degree",
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": True,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": "eCH0271_1.eCH0271.Angle",
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                    "precision": 5,
                    "min": 0.0,
                    "max": 360.0,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    eastBoundLongitude: "float | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "eastBoundLongitude",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.EX_GeographicBoundingBox.eastBoundLongitude",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": "Units.Angle_Degree",
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": True,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": "eCH0271_1.eCH0271.Angle",
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                    "precision": 5,
                    "min": 0.0,
                    "max": 360.0,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    westBoundLongitude: "float | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "westBoundLongitude",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.EX_GeographicBoundingBox.westBoundLongitude",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": "Units.Angle_Degree",
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": True,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": "eCH0271_1.eCH0271.Angle",
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                    "precision": 5,
                    "min": 0.0,
                    "max": 360.0,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.EX_GeographicBoundingBox",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class MD_Distribution:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    information about the distributor of and options for obtaining the resource

    Args:
        description:
        MD_Metadata:
    """
    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    description: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "description",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_Distribution.description",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "max_length": 256,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    MD_Metadata: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "MD_Metadata",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.distributionInfoMD_Metadata.MD_Metadata",
                "reference_targets": ["eCH0271_1.eCH0271.CHE_MD_Metadata"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "association_strongness": "Comp",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_Distribution",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class MD_MetadataScope:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    class MD_MetadataScoperesourceScopeEnum(str, Enum):
        ATTRIBUTE = "attribute"
        ATTRIBUTETYPE = "attributeType"
        COLLECTIONHARDWARE = "collectionHardware"
        COLLECTIONSESSION = "collectionSession"
        DATASET = "dataset"
        SERIES = "series"
        NONGEOGRAPHICDATASET = "nonGeographicDataset"
        DIMENSIONGROUP = "dimensionGroup"
        FEATURE = "feature"
        FEATURETYPE = "featureType"
        PROPERTYTYPE = "propertyType"
        FIELDSESSION = "fieldSession"
        SOFTWARE = "software"
        SERVICE = "service"
        MODEL = "model"
        TILE = "tile"
        METADATA = "metadata"
        INITITATIVE = "inititative"
        SAMPLE = "sample"
        DOCUMENT = "document"
        REPOSITORY = "repository"
        AGGREGATE = "aggregate"
        PRODUCT = "product"
        COLLECTION = "collection"
        COVERAGE = "coverage"
        APPLICATION = "application"

        @property
        def metadata(self) -> dict:
            return {
                "ili2py": {},
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.MD_MetadataScope.resourceScope_ENUM",
                    "kind": "Enumeration",
                    "meta_attributes": {},
                },
            }

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    resourceScope: "MD_MetadataScoperesourceScopeEnum | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "resourceScope",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_MetadataScope.resourceScope",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": "eCH0271_1.eCH0271.MD_ScopeCode",
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    name: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "name",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_MetadataScope.name",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "max_length": 256,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_MetadataScope",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class MD_ReferenceSystem:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    information about the reference system.

    Args:
        referenceSystemIdentifier: name of reference system
    """
    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    referenceSystemIdentifier: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "referenceSystemIdentifier",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_ReferenceSystemreferenceSystemIdentifier.referenceSystemIdentifier",
                "reference_targets": ["eCH0271_1.eCH0271.MD_Identifier"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_ReferenceSystem",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class MD_RepresentativeFraction:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    derived from Scale where MD_RepresentativeFraction.denominator = 1 / Scale.measure And Scale.targetUnits = Scale.sourceUnits

    Args:
        denominator: the number below the line in a vulgar fraction
    """
    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    denominator: "int | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "denominator",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_RepresentativeFraction.denominator",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": False,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": "eCH0271_1.eCH0271.Integer",
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                    "min": -10000000000,
                    "max": 10000000000,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_RepresentativeFraction",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class CI_Citation:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    standardized resource reference

    Args:
        date: reference date for the cited resource
        title: name by which the cited resource is known
        edition: version of the cited resource
        alternateTitle:
        documentationOfIdentification:
        MD_FeatureCatalogueDescription:
        standardUsedBy:
        profileUsedBy:
        SV_ServiceIdentification:
    """

    @dataclass
    class CI_CitationdateStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "list[CI_Date]" = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                "name": "CI_Date",
                "interlis": {
                    "oid": "ili2py.eCH0271_1.eCH0271.CI_Date",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CI_Citation.date.TYPE",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    @dataclass
    class CI_CitationtitleStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "Localisation_V2MultilingualMText | None" = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
                "name": "MultilingualMText",
                "interlis": {
                    "oid": "ili2py.Localisation_V2.MultilingualMText",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CI_Citation.title.TYPE",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    @dataclass
    class CI_CitationalternateTitleStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "Localisation_V2MultilingualMText | None" = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
                "name": "MultilingualMText",
                "interlis": {
                    "oid": "ili2py.Localisation_V2.MultilingualMText",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CI_Citation.alternateTitle.TYPE",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    date: "list[CI_CitationdateStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "date",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Citation.date",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    title: "CI_CitationtitleStruct | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "title",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Citation.title",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    edition: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "edition",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Citation.edition",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "max_length": 256,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    alternateTitle: "CI_CitationalternateTitleStruct | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "alternateTitle",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Citation.alternateTitle",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    documentationOfIdentification: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "documentationOfIdentification",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.documentationOfIdentificationadditionalDocumentation.documentationOfIdentification",
                "reference_targets": ["eCH0271_1.eCH0271.MD_Identification"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "association_strongness": "Comp",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    MD_FeatureCatalogueDescription: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "MD_FeatureCatalogueDescription",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.featureCatalogueCitationCI_Citation.MD_FeatureCatalogueDescription",
                "reference_targets": ["eCH0271_1.eCH0271.MD_FeatureCatalogueDescription"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "association_strongness": "Comp",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    standardUsedBy: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "standardUsedBy",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.standardUsedBymetadataStandard.standardUsedBy",
                "reference_targets": ["eCH0271_1.eCH0271.CHE_MD_Metadata"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "association_strongness": "Comp",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    profileUsedBy: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "profileUsedBy",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.profileUsedBymetadataProfile.profileUsedBy",
                "reference_targets": ["eCH0271_1.eCH0271.CHE_MD_Metadata"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "association_strongness": "Comp",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    SV_ServiceIdentification: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "SV_ServiceIdentification",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.SV_ServiceIdentificationserviceStandard.SV_ServiceIdentification",
                "reference_targets": ["eCH0271_1.eCH0271.SV_ServiceIdentification"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "association_strongness": "Comp",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Citation",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class MD_Resolution:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    level of detail expressed as a scale factor or a ground distance

    Args:
        distance: ground sample distance
        vertical:
        angularDistance:
        levelOfDetail:
        MD_DataIdentification:
    """
    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    distance: "float | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "distance",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_Resolution.distance",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": "INTERLIS.m",
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": False,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "precision": 2,
                    "min": 0.0,
                    "max": 9999999999.99,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    vertical: "float | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "vertical",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_Resolution.vertical",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": "INTERLIS.m",
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": False,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "precision": 2,
                    "min": 0.0,
                    "max": 9999999999.99,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    angularDistance: "float | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "angularDistance",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_Resolution.angularDistance",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": "Units.Angle_Degree",
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": True,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "precision": 5,
                    "min": 0.0,
                    "max": 360.0,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    levelOfDetail: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "levelOfDetail",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_Resolution.levelOfDetail",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "max_length": 256,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    MD_DataIdentification: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "MD_DataIdentification",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_DataIdentificationspatialResolution.MD_DataIdentification",
                "reference_targets": ["eCH0271_1.eCH0271.MD_Identification"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "association_strongness": "Comp",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_Resolution",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class CI_Contact:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    information required to enable contact with the responsible person and/or organization

    Args:
        CI_ResponsibleParty:
    """
    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    CI_ResponsibleParty: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "CI_ResponsibleParty",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_ResponsiblePartycontactInfo.CI_ResponsibleParty",
                "reference_targets": ["eCH0271_1.eCH0271.CI_Party"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "association_strongness": "Comp",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Contact",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class MD_Scope:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    description of the data specified by the scope

    Args:
        level: hierarchical level of the data specified by the scope
    """

    class MD_ScopelevelEnum(str, Enum):
        ATTRIBUTE = "attribute"
        ATTRIBUTETYPE = "attributeType"
        COLLECTIONHARDWARE = "collectionHardware"
        COLLECTIONSESSION = "collectionSession"
        DATASET = "dataset"
        SERIES = "series"
        NONGEOGRAPHICDATASET = "nonGeographicDataset"
        DIMENSIONGROUP = "dimensionGroup"
        FEATURE = "feature"
        FEATURETYPE = "featureType"
        PROPERTYTYPE = "propertyType"
        FIELDSESSION = "fieldSession"
        SOFTWARE = "software"
        SERVICE = "service"
        MODEL = "model"
        TILE = "tile"
        METADATA = "metadata"
        INITITATIVE = "inititative"
        SAMPLE = "sample"
        DOCUMENT = "document"
        REPOSITORY = "repository"
        AGGREGATE = "aggregate"
        PRODUCT = "product"
        COLLECTION = "collection"
        COVERAGE = "coverage"
        APPLICATION = "application"

        @property
        def metadata(self) -> dict:
            return {
                "ili2py": {},
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.MD_Scope.level_ENUM",
                    "kind": "Enumeration",
                    "meta_attributes": {},
                },
            }

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    level: "MD_ScopelevelEnum | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "level",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_Scope.level",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": "eCH0271_1.eCH0271.MD_ScopeCode",
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_Scope",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class CI_OnlineResource:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    @dataclass
    class CI_OnlineResourcedescriptionStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "Localisation_V2MultilingualMText | None" = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
                "name": "MultilingualMText",
                "interlis": {
                    "oid": "ili2py.Localisation_V2.MultilingualMText",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CI_OnlineResource.description.TYPE",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    @dataclass
    class CI_OnlineResourcenameStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "Localisation_V2MultilingualMText | None" = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
                "name": "MultilingualMText",
                "interlis": {
                    "oid": "ili2py.Localisation_V2.MultilingualMText",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CI_OnlineResource.name.TYPE",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    @dataclass
    class CI_OnlineResourcelinkageStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "Localisation_V2MultilingualUri | None" = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
                "name": "MultilingualUri",
                "interlis": {
                    "oid": "ili2py.Localisation_V2.MultilingualUri",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CI_OnlineResource.linkage.TYPE",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    protocol: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "protocol",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_OnlineResource.protocol",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "max_length": 256,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    function: "CI_OnLineFunctionCode | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "function",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_OnlineResource.function",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    description: "CI_OnlineResourcedescriptionStruct | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "description",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_OnlineResource.description",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    name: "CI_OnlineResourcenameStruct | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "name",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_OnlineResource.name",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    linkage: "CI_OnlineResourcelinkageStruct | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "linkage",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_OnlineResource.linkage",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    CI_Contact: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "CI_Contact",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_ContactonlineResource.CI_Contact",
                "reference_targets": ["eCH0271_1.eCH0271.CI_Contact"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "association_strongness": "Comp",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    MD_BrowseGraphic: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "MD_BrowseGraphic",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_BrowseGraphiclinkage.MD_BrowseGraphic",
                "reference_targets": ["eCH0271_1.eCH0271.MD_BrowseGraphic"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "association_strongness": "Comp",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    SV_OperationMetadata: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "SV_OperationMetadata",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.SV_OperationMetadataconnectPoint.SV_OperationMetadata",
                "reference_targets": ["eCH0271_1.eCH0271.SV_OperationMetadata"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "association_strongness": "Comp",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    CI_Citation: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "CI_Citation",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_CitationonlineResource.CI_Citation",
                "reference_targets": ["eCH0271_1.eCH0271.CI_Citation"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "association_strongness": "Comp",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    MD_DigitalTransferOptions: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "MD_DigitalTransferOptions",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_DigitalTransferOptionsonLine.MD_DigitalTransferOptions",
                "reference_targets": ["eCH0271_1.eCH0271.MD_DigitalTransferOptions"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "association_strongness": "Comp",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_OnlineResource",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class MD_Keywords:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    keywords, their type and reference source

    Args:
        type: subject matter used to group similar keywords
        keyword: commonly used word(s) or formalised word(s) or phrase(s) used to describe the subject
        thesaurusName:
    """

    @dataclass
    class MD_KeywordskeywordStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "list[Localisation_V2MultilingualMText]" = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
                "name": "MultilingualMText",
                "interlis": {
                    "oid": "ili2py.Localisation_V2.MultilingualMText",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.MD_Keywords.keyword.TYPE",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    type: "MD_KeywordTypeCode | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "type",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_Keywords.type",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    keyword: "list[MD_KeywordskeywordStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "keyword",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_Keywords.keyword",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": None},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    thesaurusName: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "thesaurusName",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_keywordsthesaurusName.thesaurusName",
                "reference_targets": ["eCH0271_1.eCH0271.CI_Citation"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_Keywords",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class CI_Party:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    @dataclass
    class CI_PartynameStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "Localisation_V2MultilingualMText | None" = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
                "name": "MultilingualMText",
                "interlis": {
                    "oid": "ili2py.Localisation_V2.MultilingualMText",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CI_Party.name.TYPE",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    name: "CI_PartynameStruct | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "name",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Party.name",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Party",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class EX_Extent:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    information about spatial, vertical, and temporal extent

    Args:
        description:
        MD_DataIdentification:
    """

    @dataclass
    class EX_ExtentdescriptionStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "Localisation_V2MultilingualMText | None" = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
                "name": "MultilingualMText",
                "interlis": {
                    "oid": "ili2py.Localisation_V2.MultilingualMText",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.EX_Extent.description.TYPE",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    description: "EX_ExtentdescriptionStruct | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "description",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.EX_Extent.description",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    MD_DataIdentification: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "MD_DataIdentification",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_DataIdentificationextent.MD_DataIdentification",
                "reference_targets": ["eCH0271_1.eCH0271.MD_Identification"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "association_strongness": "Comp",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.EX_Extent",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class CI_Individual(CI_Party):

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    @dataclass
    class CI_IndividualpositionNameStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "Localisation_V2MultilingualMText | None" = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
                "name": "MultilingualMText",
                "interlis": {
                    "oid": "ili2py.Localisation_V2.MultilingualMText",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CI_Individual.positionName.TYPE",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    individualFirstName: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "individualFirstName",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Individual.individualFirstName",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "max_length": 256,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    positionName: "CI_IndividualpositionNameStruct | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "positionName",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Individual.positionName",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Individual",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class CHE_CI_Organisation(CI_Party):

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    @dataclass
    class CHE_CI_OrganisationorganisationAcronymStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "Localisation_V2MultilingualMText | None" = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
                "name": "MultilingualMText",
                "interlis": {
                    "oid": "ili2py.Localisation_V2.MultilingualMText",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CHE_CI_Organisation.organisationAcronym.TYPE",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    organisationAcronym: "CHE_CI_OrganisationorganisationAcronymStruct | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "organisationAcronym",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_CI_Organisation.organisationAcronym",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_CI_Organisation",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class CHE_MD_DataIdentification(MD_Identification):

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    information required to identify a dataset
citation/identifier/code shall be only one language (the unique identifier of the dataset)

    Args:
        defaultLocale: language(s) used within the dataset
        supplementalInformation:
        otherLocale:
        subTopicCategory:
        basicGeodata:
        basicGeodataInformation:
    """

    @dataclass
    class CHE_MD_DataIdentificationdefaultLocaleStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "PT_Locale | None" = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                "name": "PT_Locale",
                "interlis": {
                    "oid": "ili2py.eCH0271_1.eCH0271.PT_Locale",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CHE_MD_DataIdentification.defaultLocale.TYPE",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    @dataclass
    class CHE_MD_DataIdentificationsupplementalInformationStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "Localisation_V2MultilingualMText | None" = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
                "name": "MultilingualMText",
                "interlis": {
                    "oid": "ili2py.Localisation_V2.MultilingualMText",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CHE_MD_DataIdentification.supplementalInformation.TYPE",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    @dataclass
    class CHE_MD_DataIdentificationotherLocaleStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "list[PT_Locale]" = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                "name": "PT_Locale",
                "interlis": {
                    "oid": "ili2py.eCH0271_1.eCH0271.PT_Locale",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CHE_MD_DataIdentification.otherLocale.TYPE",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    @dataclass
    class CHE_MD_DataIdentificationsubTopicCategoryStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "CHE_MD_SubTopicCategoryCode | None" = field(
            default=None,
            metadata={
                "type": "Text",
                "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                "name": "struct_content",
                "interlis": {
                    "oid": "ili2py.eCH0271_1.eCH0271.CHE_MD_SubTopicCategoryCode",
                    "meta_attributes": {},
                    "type_restrictions": {
                        "mandatory": False,
                        "kind": None,
                        "format": None,
                        "unit": None,
                        "ref_sys": None,
                        "clockwise": None,
                        "circular": None,
                        "abstract": False,
                        "final": False,
                        "generic": None,
                        "super": None,
                        "type_related_type": False,
                        "multiplicity": {"min": 0, "max": 1},
                    },
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CHE_MD_DataIdentification.subTopicCategory.MVT",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    @dataclass
    class CHE_MD_DataIdentificationbasicGeodataInformationStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "list[CHE_MD_BasicGeodataInformation]" = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                "name": "CHE_MD_BasicGeodataInformation",
                "interlis": {
                    "oid": "ili2py.eCH0271_1.eCH0271.CHE_MD_BasicGeodataInformation",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CHE_MD_DataIdentification.basicGeodataInformation.TYPE",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    defaultLocale: "CHE_MD_DataIdentificationdefaultLocaleStruct | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "defaultLocale",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_DataIdentification.defaultLocale",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    supplementalInformation: (
        "CHE_MD_DataIdentificationsupplementalInformationStruct | None"
    ) = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "supplementalInformation",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_DataIdentification.supplementalInformation",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    otherLocale: "list[CHE_MD_DataIdentificationotherLocaleStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "otherLocale",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_DataIdentification.otherLocale",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    subTopicCategory: "list[CHE_MD_DataIdentificationsubTopicCategoryStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "subTopicCategory",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_DataIdentification.subTopicCategory",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": None,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": None,
                    "final": None,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    basicGeodata: "bool | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "basicGeodata",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_DataIdentification.basicGeodata",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    basicGeodataInformation: "list[CHE_MD_DataIdentificationbasicGeodataInformationStruct]" = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                "name": "basicGeodataInformation",
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CHE_MD_DataIdentification.basicGeodataInformation",
                    "meta_attributes": {},
                    "type_restrictions": {
                        "mandatory": False,
                        "kind": None,
                        "format": None,
                        "unit": None,
                        "ref_sys": None,
                        "clockwise": None,
                        "circular": None,
                        "abstract": False,
                        "final": False,
                        "generic": False,
                        "super": None,
                        "type_related_type": False,
                        "multiplicity": {"min": 0, "max": None},
                    },
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CHE_MD_DataIdentification",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class CI_Series:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    information about the series, or aggregate dataset, to which a dataset belongs

    Args:
        name:
    """

    @dataclass
    class CI_SeriesnameStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "Localisation_V2MultilingualMText | None" = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
                "name": "MultilingualMText",
                "interlis": {
                    "oid": "ili2py.Localisation_V2.MultilingualMText",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.CI_Series.name.TYPE",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    name: "CI_SeriesnameStruct | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "name",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Series.name",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Series",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class QualityResult(ABC):

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    DQ_Element: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "DQ_Element",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.resultDQ_Element.DQ_Element",
                "reference_targets": ["eCH0271_1.eCH0271.QualityElement"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "association_strongness": "Comp",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.QualityResult",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class DQ_ConformanceResult(QualityResult):

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    explanation: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "explanation",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.DQ_ConformanceResult.explanation",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "max_length": 256,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    pass_: "bool | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "pass",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.DQ_ConformanceResult.pass",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": "eCH0271_1.eCH0271.Boolean",
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.DQ_ConformanceResult",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class gml_CodeType:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    code: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "code",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.gml_CodeType.code",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": "eCH0271_1.eCH0271.CharacterString",
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                    "max_length": 256,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    codeSpace: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "codeSpace",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.gml_CodeType.codeSpace",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "max_length": 1023,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.gml_CodeType",
                "kind": "Structure",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class LI_ProcessStep:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    information about an event in the creation process for the data specified by the scope

    Args:
        description: description of the event, including related parameters or tolerances
        stepDateTime: date and time or range of date and time on or over which the process step occurred
        rationale:
        LI_Lineage:
    """

    @dataclass
    class LI_ProcessStepstepDateTimeStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "TM_Primitive | None" = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                "name": "TM_Primitive",
                "interlis": {
                    "oid": "ili2py.eCH0271_1.eCH0271.TM_Primitive",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.LI_ProcessStep.stepDateTime.TYPE",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    @dataclass
    class LI_ProcessSteprationaleStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "str | None" = field(
            default=None,
            metadata={
                "type": "Text",
                "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                "name": "struct_content",
                "interlis": {
                    "oid": "ili2py.eCH0271_1.eCH0271.CharacterString",
                    "meta_attributes": {},
                    "type_restrictions": {
                        "mandatory": False,
                        "kind": None,
                        "format": None,
                        "unit": None,
                        "ref_sys": None,
                        "clockwise": None,
                        "circular": None,
                        "abstract": False,
                        "final": False,
                        "generic": None,
                        "super": None,
                        "type_related_type": False,
                        "multiplicity": {"min": 0, "max": 1},
                        "max_length": 256,
                    },
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.LI_ProcessStep.rationale.MVT",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    description: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "description",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.LI_ProcessStep.description",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": "eCH0271_1.eCH0271.CharacterStringLong",
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    stepDateTime: "LI_ProcessStepstepDateTimeStruct | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "stepDateTime",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.LI_ProcessStep.stepDateTime",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    rationale: "list[LI_ProcessSteprationaleStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "rationale",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.LI_ProcessStep.rationale",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": None,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": None,
                    "final": None,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    LI_Lineage: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "LI_Lineage",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.processStepLI_Lineage.LI_Lineage",
                "reference_targets": ["eCH0271_1.eCH0271.LI_Lineage"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "association_strongness": "Comp",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.LI_ProcessStep",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class QualityElement(ABC):

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.QualityElement",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class SV_ServiceIdentification(MD_Identification):

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    See 19119 for further info

    Args:
        credit:
        serviceTypeVersion:
        serviceType:
    """

    @dataclass
    class SV_ServiceIdentificationcreditStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "str | None" = field(
            default=None,
            metadata={
                "type": "Text",
                "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                "name": "struct_content",
                "interlis": {
                    "oid": "ili2py.eCH0271_1.eCH0271.CharacterString",
                    "meta_attributes": {},
                    "type_restrictions": {
                        "mandatory": False,
                        "kind": None,
                        "format": None,
                        "unit": None,
                        "ref_sys": None,
                        "clockwise": None,
                        "circular": None,
                        "abstract": False,
                        "final": False,
                        "generic": None,
                        "super": None,
                        "type_related_type": False,
                        "multiplicity": {"min": 0, "max": 1},
                        "max_length": 256,
                    },
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.SV_ServiceIdentification.credit.MVT",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    @dataclass
    class SV_ServiceIdentificationserviceTypeStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "gml_CodeType | None" = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                "name": "gml_CodeType",
                "interlis": {
                    "oid": "ili2py.eCH0271_1.eCH0271.gml_CodeType",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.SV_ServiceIdentification.serviceType.TYPE",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    credit: "list[SV_ServiceIdentificationcreditStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "credit",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.SV_ServiceIdentification.credit",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": None,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": None,
                    "final": None,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    serviceTypeVersion: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "serviceTypeVersion",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.SV_ServiceIdentification.serviceTypeVersion",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "max_length": 256,
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    serviceType: "SV_ServiceIdentificationserviceTypeStruct | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "serviceType",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.SV_ServiceIdentification.serviceType",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.SV_ServiceIdentification",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class DQ_LogicalConsistency(QualityElement):

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.DQ_LogicalConsistency",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class LI_Source:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    """
    information about the source data used in creating the data specified by the scope

    Args:
        description:
    """

    @dataclass
    class LI_SourcedescriptionStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "Localisation_V2MultilingualMText | None" = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
                "name": "MultilingualMText",
                "interlis": {
                    "oid": "ili2py.Localisation_V2.MultilingualMText",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
                },
                "geometric": {
                    "is_geometric": False,
                    "multi": False,
                    "point_like": False,
                    "line_like": False,
                    "polygon_like": False,
                },
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "eCH0271_1.eCH0271.LI_Source.description.TYPE",
                    "kind": "None",
                    "meta_attributes": {},
                }
            }

        @property
        def existence_constraints(self) -> list:
            """
            Delivers the existence constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def set_constraints(self) -> list:
            """
            Delivers the set constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def simple_constraints(self) -> list:
            """
            Delivers the simple constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def unique_constraints(self) -> list:
            """
            Delivers the unique constraints applying to this object.

            Returns:
                The list of constraints as dict. They can be deserialized with the
                corresponding classes.
            """
            return []

        @property
        def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for point like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for line like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
            """
            Gives back a list of tuples which contain the name of the attribute and
            the corresponding value for polygon like geometries.

            Returns:
                Tuple, first element is the attribute name, second the geometry value.
            """
            return []

        @property
        def geom_attributes(self) -> list[str]:
            """
            Delivers a list of attributes names which contain geometric information.

            Returns:
                The list of geometry attribute names. Empty list when no geometry attributes at this class.
            """
            return []

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    description: "LI_SourcedescriptionStruct | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "description",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.LI_Source.description",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.LI_Source",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class DQ_DomainConsistency(DQ_LogicalConsistency):

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.DQ_DomainConsistency",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class legislationConstraintsMD_LegalConstraints:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    legislationConstraints: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "legislationConstraints",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.legislationConstraintsMD_LegalConstraints.legislationConstraints",
                "reference_targets": ["eCH0271_1.eCH0271.CHE_MD_Legislation"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    MD_LegalConstraints: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "MD_LegalConstraints",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.legislationConstraintsMD_LegalConstraints.MD_LegalConstraints",
                "reference_targets": ["eCH0271_1.eCH0271.CHE_MD_LegalConstraints"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Aggr",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.legislationConstraintsMD_LegalConstraints",
                "kind": "Association",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class aggregationInfo_MD_Identification:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    aggregationInfo: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "aggregationInfo",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.aggregationInfo_MD_Identification.aggregationInfo",
                "reference_targets": ["eCH0271_1.eCH0271.MD_AssociatedResource"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    MD_Identification: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "MD_Identification",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.aggregationInfo_MD_Identification.MD_Identification",
                "reference_targets": ["eCH0271_1.eCH0271.MD_Identification"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Aggr",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.aggregationInfo_MD_Identification",
                "kind": "Association",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class distributionOrderProcessMD_Distributor:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    distributionOrderProcess: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "distributionOrderProcess",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.distributionOrderProcessMD_Distributor.distributionOrderProcess",
                "reference_targets": ["eCH0271_1.eCH0271.MD_StandardOrderProcess"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    MD_Distributor: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "MD_Distributor",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.distributionOrderProcessMD_Distributor.MD_Distributor",
                "reference_targets": ["eCH0271_1.eCH0271.MD_Distributor"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Aggr",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.distributionOrderProcessMD_Distributor",
                "kind": "Association",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class distributorTransferOptionsMD_Distributor:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    distributorTransferOptions: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "distributorTransferOptions",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.distributorTransferOptionsMD_Distributor.distributorTransferOptions",
                "reference_targets": ["eCH0271_1.eCH0271.MD_DigitalTransferOptions"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    MD_Distributor: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "MD_Distributor",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.distributorTransferOptionsMD_Distributor.MD_Distributor",
                "reference_targets": ["eCH0271_1.eCH0271.MD_Distributor"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.distributorTransferOptionsMD_Distributor",
                "kind": "Association",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class applicationSchemaInfoMD_Metadata:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    applicationSchemaInfo: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "applicationSchemaInfo",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.applicationSchemaInfoMD_Metadata.applicationSchemaInfo",
                "reference_targets": ["eCH0271_1.eCH0271.MD_ApplicationSchemaInformation"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    MD_Metadata: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "MD_Metadata",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.applicationSchemaInfoMD_Metadata.MD_Metadata",
                "reference_targets": ["eCH0271_1.eCH0271.CHE_MD_Metadata"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Aggr",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.applicationSchemaInfoMD_Metadata",
                "kind": "Association",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class formatDistributordistributorFormat:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    formatDistributor: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "formatDistributor",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.formatDistributordistributorFormat.formatDistributor",
                "reference_targets": ["eCH0271_1.eCH0271.MD_Distributor"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    distributorFormat: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "distributorFormat",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.formatDistributordistributorFormat.distributorFormat",
                "reference_targets": ["eCH0271_1.eCH0271.MD_Format"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.formatDistributordistributorFormat",
                "kind": "Association",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class MD_DistributiondistributionFormat:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    MD_Distribution: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "MD_Distribution",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_DistributiondistributionFormat.MD_Distribution",
                "reference_targets": ["eCH0271_1.eCH0271.MD_Distribution"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Aggr",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    distributionFormat: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "distributionFormat",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_DistributiondistributionFormat.distributionFormat",
                "reference_targets": ["eCH0271_1.eCH0271.MD_Format"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_DistributiondistributionFormat",
                "kind": "Association",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class MD_Distributiondistributor:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    distributor: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "distributor",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_Distributiondistributor.distributor",
                "reference_targets": ["eCH0271_1.eCH0271.MD_Distributor"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    MD_Distribution: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "MD_Distribution",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_Distributiondistributor.MD_Distribution",
                "reference_targets": ["eCH0271_1.eCH0271.MD_Distribution"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Aggr",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_Distributiondistributor",
                "kind": "Association",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class CI_CitationcitedResponsibleParty:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    citedResponsibleParty: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "citedResponsibleParty",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_CitationcitedResponsibleParty.citedResponsibleParty",
                "reference_targets": ["eCH0271_1.eCH0271.CI_Responsibility"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    CI_Citation: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "CI_Citation",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_CitationcitedResponsibleParty.CI_Citation",
                "reference_targets": ["eCH0271_1.eCH0271.CI_Citation"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Aggr",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_CitationcitedResponsibleParty",
                "kind": "Association",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class CI_Citationidentifier:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    identifier: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "identifier",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Citationidentifier.identifier",
                "reference_targets": ["eCH0271_1.eCH0271.MD_Identifier"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    CI_Citation: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "CI_Citation",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Citationidentifier.CI_Citation",
                "reference_targets": ["eCH0271_1.eCH0271.CI_Citation"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Aggr",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Citationidentifier",
                "kind": "Association",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class MD_MetadatalegislationInformation:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    MD_Metadata: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "MD_Metadata",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_MetadatalegislationInformation.MD_Metadata",
                "reference_targets": ["eCH0271_1.eCH0271.CHE_MD_Metadata"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Aggr",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    legislationInformation: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "legislationInformation",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_MetadatalegislationInformation.legislationInformation",
                "reference_targets": ["eCH0271_1.eCH0271.CHE_MD_Legislation"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_MetadatalegislationInformation",
                "kind": "Association",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class MD_MetadatametadataScope:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    MD_Metadata: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "MD_Metadata",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_MetadatametadataScope.MD_Metadata",
                "reference_targets": ["eCH0271_1.eCH0271.CHE_MD_Metadata"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Aggr",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    metadataScope: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "metadataScope",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_MetadatametadataScope.metadataScope",
                "reference_targets": ["eCH0271_1.eCH0271.MD_MetadataScope"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_MetadatametadataScope",
                "kind": "Association",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class CI_Responsibilityparty:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    CI_Responsibility: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "CI_Responsibility",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Responsibilityparty.CI_Responsibility",
                "reference_targets": ["eCH0271_1.eCH0271.CI_Responsibility"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Aggr",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    party: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "party",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Responsibilityparty.party",
                "reference_targets": ["eCH0271_1.eCH0271.CI_Party"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": None},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_Responsibilityparty",
                "kind": "Association",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class MD_Metadatacontact:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    contact: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "contact",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_Metadatacontact.contact",
                "reference_targets": ["eCH0271_1.eCH0271.CI_Responsibility"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": None},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    MD_Metadata: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "MD_Metadata",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_Metadatacontact.MD_Metadata",
                "reference_targets": ["eCH0271_1.eCH0271.CHE_MD_Metadata"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Aggr",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_Metadatacontact",
                "kind": "Association",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class descriptiveKeywordsMD_Identification:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    descriptiveKeywords: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "descriptiveKeywords",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.descriptiveKeywordsMD_Identification.descriptiveKeywords",
                "reference_targets": ["eCH0271_1.eCH0271.MD_Keywords"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    MD_Identification: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "MD_Identification",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.descriptiveKeywordsMD_Identification.MD_Identification",
                "reference_targets": ["eCH0271_1.eCH0271.MD_Identification"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Aggr",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.descriptiveKeywordsMD_Identification",
                "kind": "Association",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class referenceSystemInfoMD_Metadata:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    referenceSystemInfo: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "referenceSystemInfo",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.referenceSystemInfoMD_Metadata.referenceSystemInfo",
                "reference_targets": ["eCH0271_1.eCH0271.MD_ReferenceSystem"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    MD_Metadata: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "MD_Metadata",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.referenceSystemInfoMD_Metadata.MD_Metadata",
                "reference_targets": ["eCH0271_1.eCH0271.CHE_MD_Metadata"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Aggr",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.referenceSystemInfoMD_Metadata",
                "kind": "Association",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class resourceFormatMD_Identification:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    resourceFormat: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "resourceFormat",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.resourceFormatMD_Identification.resourceFormat",
                "reference_targets": ["eCH0271_1.eCH0271.MD_Format"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    MD_Identification: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "MD_Identification",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.resourceFormatMD_Identification.MD_Identification",
                "reference_targets": ["eCH0271_1.eCH0271.MD_Identification"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Aggr",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.resourceFormatMD_Identification",
                "kind": "Association",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class EX_ExtentgeographicElement:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    EX_Extent: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "EX_Extent",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.EX_ExtentgeographicElement.EX_Extent",
                "reference_targets": ["eCH0271_1.eCH0271.EX_Extent"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Aggr",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    geographicElement: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "geographicElement",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.EX_ExtentgeographicElement.geographicElement",
                "reference_targets": ["eCH0271_1.eCH0271.EX_GeographicExtent"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.EX_ExtentgeographicElement",
                "kind": "Association",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class EX_ExtenttemporalElement:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    EX_Extent: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "EX_Extent",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.EX_ExtenttemporalElement.EX_Extent",
                "reference_targets": ["eCH0271_1.eCH0271.EX_Extent"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Aggr",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    temporalElement: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "temporalElement",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.EX_ExtenttemporalElement.temporalElement",
                "reference_targets": ["eCH0271_1.eCH0271.EX_TemporalExtent"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.EX_ExtenttemporalElement",
                "kind": "Association",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class CI_ResponsiblePartyparentinfo:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    parentResponsibleParty: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "parentResponsibleParty",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_ResponsiblePartyparentinfo.parentResponsibleParty",
                "reference_targets": ["eCH0271_1.eCH0271.CHE_CI_Organisation"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Aggr",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    parentOrganisation: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "parentOrganisation",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_ResponsiblePartyparentinfo.parentOrganisation",
                "reference_targets": ["eCH0271_1.eCH0271.CI_Responsibility"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.CI_ResponsiblePartyparentinfo",
                "kind": "Association",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class EX_ExtentverticalElement:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    EX_Extent: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "EX_Extent",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.EX_ExtentverticalElement.EX_Extent",
                "reference_targets": ["eCH0271_1.eCH0271.EX_Extent"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Aggr",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    verticalElement: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "verticalElement",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.EX_ExtentverticalElement.verticalElement",
                "reference_targets": ["eCH0271_1.eCH0271.EX_VerticalExtent"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.EX_ExtentverticalElement",
                "kind": "Association",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class individualorganisation:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    individual: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "individual",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.individualorganisation.individual",
                "reference_targets": ["eCH0271_1.eCH0271.CI_Individual"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    organisation: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "organisation",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.individualorganisation.organisation",
                "reference_targets": ["eCH0271_1.eCH0271.CHE_CI_Organisation"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Aggr",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.individualorganisation",
                "kind": "Association",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class MD_IdentificationpointOfContact:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    pointOfContact: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "pointOfContact",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_IdentificationpointOfContact.pointOfContact",
                "reference_targets": ["eCH0271_1.eCH0271.CI_Responsibility"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    MD_Identification: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "MD_Identification",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_IdentificationpointOfContact.MD_Identification",
                "reference_targets": ["eCH0271_1.eCH0271.MD_Identification"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Aggr",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.MD_IdentificationpointOfContact",
                "kind": "Association",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class containsOperationsSV_ServiceIdentification:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    containsOperations: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "containsOperations",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.containsOperationsSV_ServiceIdentification.containsOperations",
                "reference_targets": ["eCH0271_1.eCH0271.SV_OperationMetadata"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    SV_ServiceIdentification: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "SV_ServiceIdentification",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.containsOperationsSV_ServiceIdentification.SV_ServiceIdentification",
                "reference_targets": ["eCH0271_1.eCH0271.SV_ServiceIdentification"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Aggr",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.containsOperationsSV_ServiceIdentification",
                "kind": "Association",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class reportDQ_DataQuality:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    report: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "report",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.reportDQ_DataQuality.report",
                "reference_targets": ["eCH0271_1.eCH0271.QualityElement"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": None},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    DQ_Qualitiy: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "DQ_Qualitiy",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.reportDQ_DataQuality.DQ_Qualitiy",
                "reference_targets": ["eCH0271_1.eCH0271.DQ_DataQuality"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Aggr",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.reportDQ_DataQuality",
                "kind": "Association",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class SV_ServiceIdentificationoperatesOn:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    SV_ServiceIdentification: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "SV_ServiceIdentification",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.SV_ServiceIdentificationoperatesOn.SV_ServiceIdentification",
                "reference_targets": ["eCH0271_1.eCH0271.SV_ServiceIdentification"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Aggr",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    operatesOn: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "operatesOn",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.SV_ServiceIdentificationoperatesOn.operatesOn",
                "reference_targets": ["eCH0271_1.eCH0271.CHE_MD_DataIdentification"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.SV_ServiceIdentificationoperatesOn",
                "kind": "Association",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class resourceConstraintsMD_Identification:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    resourceConstraints: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "resourceConstraints",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.resourceConstraintsMD_Identification.resourceConstraints",
                "reference_targets": ["eCH0271_1.eCH0271.MD_Constraints"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    MD_Identification: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "MD_Identification",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.resourceConstraintsMD_Identification.MD_Identification",
                "reference_targets": ["eCH0271_1.eCH0271.MD_Identification"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Aggr",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.resourceConstraintsMD_Identification",
                "kind": "Association",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class sourceLI_Lineage:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    source: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "source",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.sourceLI_Lineage.source",
                "reference_targets": ["eCH0271_1.eCH0271.LI_Source"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    LI_Lineage: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "LI_Lineage",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.sourceLI_Lineage.LI_Lineage",
                "reference_targets": ["eCH0271_1.eCH0271.LI_Lineage"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Aggr",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.sourceLI_Lineage",
                "kind": "Association",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class sourceStepsource:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/eCH0271_1"

    sourceStep: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "sourceStep",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.sourceStepsource.sourceStep",
                "reference_targets": ["eCH0271_1.eCH0271.LI_ProcessStep"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )
    source: "Ref | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
            "name": "source",
            "interlis": {
                "oid": "eCH0271_1.eCH0271.sourceStepsource.source",
                "reference_targets": ["eCH0271_1.eCH0271.LI_Source"],
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                    "association_strongness": "Assoc",
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "eCH0271_1.eCH0271.sourceStepsource",
                "kind": "Association",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class eCH0271TOPIC:
    class Meta:
        name = "eCH0271"

    elements: list[
        Union[
            DQ_DataQuality,
            LI_Lineage,
            MD_Constraints,
            CHE_MD_LegalConstraints,
            CHE_MD_MaintenanceInformation,
            MD_DigitalTransferOptions,
            EX_TemporalExtent,
            MD_Distributor,
            MD_FeatureCatalogueDescription,
            CHE_MD_Appraisal_AAP,
            CHE_MD_Legislation,
            CI_Address,
            MD_ApplicationSchemaInformation,
            MD_BrowseGraphic,
            MD_Format,
            MD_SecurityConstraints,
            SV_OperationMetadata,
            MD_AssociatedResource,
            MD_Identifier,
            MD_StandardOrderProcess,
            legislationConstraintsMD_LegalConstraints,
            aggregationInfo_MD_Identification,
            distributionOrderProcessMD_Distributor,
            distributorTransferOptionsMD_Distributor,
            CHE_MD_Metadata,
            applicationSchemaInfoMD_Metadata,
            CI_Responsibility,
            formatDistributordistributorFormat,
            CI_Telephone,
            EX_BoundingPolygon,
            EX_VerticalExtent,
            EX_GeographicBoundingBox,
            MD_Distribution,
            MD_MetadataScope,
            MD_DistributiondistributionFormat,
            MD_Distributiondistributor,
            MD_ReferenceSystem,
            MD_RepresentativeFraction,
            CI_Citation,
            MD_Resolution,
            CI_Contact,
            MD_Scope,
            CI_CitationcitedResponsibleParty,
            CI_OnlineResource,
            MD_Keywords,
            CI_Citationidentifier,
            MD_MetadatalegislationInformation,
            CI_Party,
            MD_MetadatametadataScope,
            EX_Extent,
            CI_Responsibilityparty,
            MD_Metadatacontact,
            descriptiveKeywordsMD_Identification,
            referenceSystemInfoMD_Metadata,
            resourceFormatMD_Identification,
            CI_Individual,
            EX_ExtentgeographicElement,
            CHE_CI_Organisation,
            EX_ExtenttemporalElement,
            CHE_MD_DataIdentification,
            CI_ResponsiblePartyparentinfo,
            EX_ExtentverticalElement,
            individualorganisation,
            MD_IdentificationpointOfContact,
            CI_Series,
            DQ_ConformanceResult,
            LI_ProcessStep,
            SV_ServiceIdentification,
            LI_Source,
            containsOperationsSV_ServiceIdentification,
            reportDQ_DataQuality,
            SV_ServiceIdentificationoperatesOn,
            DQ_DomainConsistency,
            resourceConstraintsMD_Identification,
            sourceLI_Lineage,
            sourceStepsource,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DQ_DataQuality",
                    "type": DQ_DataQuality,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "LI_Lineage",
                    "type": LI_Lineage,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "MD_Constraints",
                    "type": MD_Constraints,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "CHE_MD_LegalConstraints",
                    "type": CHE_MD_LegalConstraints,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "CHE_MD_MaintenanceInformation",
                    "type": CHE_MD_MaintenanceInformation,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "MD_DigitalTransferOptions",
                    "type": MD_DigitalTransferOptions,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "EX_TemporalExtent",
                    "type": EX_TemporalExtent,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "MD_Distributor",
                    "type": MD_Distributor,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "MD_FeatureCatalogueDescription",
                    "type": MD_FeatureCatalogueDescription,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "CHE_MD_Appraisal_AAP",
                    "type": CHE_MD_Appraisal_AAP,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "CHE_MD_Legislation",
                    "type": CHE_MD_Legislation,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "CI_Address",
                    "type": CI_Address,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "MD_ApplicationSchemaInformation",
                    "type": MD_ApplicationSchemaInformation,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "MD_BrowseGraphic",
                    "type": MD_BrowseGraphic,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "MD_Format",
                    "type": MD_Format,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "MD_SecurityConstraints",
                    "type": MD_SecurityConstraints,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "SV_OperationMetadata",
                    "type": SV_OperationMetadata,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "MD_AssociatedResource",
                    "type": MD_AssociatedResource,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "MD_Identifier",
                    "type": MD_Identifier,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "MD_StandardOrderProcess",
                    "type": MD_StandardOrderProcess,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "legislationConstraintsMD_LegalConstraints",
                    "type": legislationConstraintsMD_LegalConstraints,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "aggregationInfo_MD_Identification",
                    "type": aggregationInfo_MD_Identification,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "distributionOrderProcessMD_Distributor",
                    "type": distributionOrderProcessMD_Distributor,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "distributorTransferOptionsMD_Distributor",
                    "type": distributorTransferOptionsMD_Distributor,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "CHE_MD_Metadata",
                    "type": CHE_MD_Metadata,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "applicationSchemaInfoMD_Metadata",
                    "type": applicationSchemaInfoMD_Metadata,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "CI_Responsibility",
                    "type": CI_Responsibility,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "formatDistributordistributorFormat",
                    "type": formatDistributordistributorFormat,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "CI_Telephone",
                    "type": CI_Telephone,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "EX_BoundingPolygon",
                    "type": EX_BoundingPolygon,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "EX_VerticalExtent",
                    "type": EX_VerticalExtent,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "EX_GeographicBoundingBox",
                    "type": EX_GeographicBoundingBox,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "MD_Distribution",
                    "type": MD_Distribution,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "MD_MetadataScope",
                    "type": MD_MetadataScope,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "MD_DistributiondistributionFormat",
                    "type": MD_DistributiondistributionFormat,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "MD_Distributiondistributor",
                    "type": MD_Distributiondistributor,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "MD_ReferenceSystem",
                    "type": MD_ReferenceSystem,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "MD_RepresentativeFraction",
                    "type": MD_RepresentativeFraction,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "CI_Citation",
                    "type": CI_Citation,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "MD_Resolution",
                    "type": MD_Resolution,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "CI_Contact",
                    "type": CI_Contact,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "MD_Scope",
                    "type": MD_Scope,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "CI_CitationcitedResponsibleParty",
                    "type": CI_CitationcitedResponsibleParty,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "CI_OnlineResource",
                    "type": CI_OnlineResource,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "MD_Keywords",
                    "type": MD_Keywords,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "CI_Citationidentifier",
                    "type": CI_Citationidentifier,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "MD_MetadatalegislationInformation",
                    "type": MD_MetadatalegislationInformation,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "CI_Party",
                    "type": CI_Party,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "MD_MetadatametadataScope",
                    "type": MD_MetadatametadataScope,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "EX_Extent",
                    "type": EX_Extent,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "CI_Responsibilityparty",
                    "type": CI_Responsibilityparty,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "MD_Metadatacontact",
                    "type": MD_Metadatacontact,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "descriptiveKeywordsMD_Identification",
                    "type": descriptiveKeywordsMD_Identification,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "referenceSystemInfoMD_Metadata",
                    "type": referenceSystemInfoMD_Metadata,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "resourceFormatMD_Identification",
                    "type": resourceFormatMD_Identification,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "CI_Individual",
                    "type": CI_Individual,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "EX_ExtentgeographicElement",
                    "type": EX_ExtentgeographicElement,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "CHE_CI_Organisation",
                    "type": CHE_CI_Organisation,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "EX_ExtenttemporalElement",
                    "type": EX_ExtenttemporalElement,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "CHE_MD_DataIdentification",
                    "type": CHE_MD_DataIdentification,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "CI_ResponsiblePartyparentinfo",
                    "type": CI_ResponsiblePartyparentinfo,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "EX_ExtentverticalElement",
                    "type": EX_ExtentverticalElement,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "individualorganisation",
                    "type": individualorganisation,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "MD_IdentificationpointOfContact",
                    "type": MD_IdentificationpointOfContact,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "CI_Series",
                    "type": CI_Series,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "DQ_ConformanceResult",
                    "type": DQ_ConformanceResult,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "LI_ProcessStep",
                    "type": LI_ProcessStep,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "SV_ServiceIdentification",
                    "type": SV_ServiceIdentification,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "LI_Source",
                    "type": LI_Source,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "containsOperationsSV_ServiceIdentification",
                    "type": containsOperationsSV_ServiceIdentification,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "reportDQ_DataQuality",
                    "type": reportDQ_DataQuality,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "SV_ServiceIdentificationoperatesOn",
                    "type": SV_ServiceIdentificationoperatesOn,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "DQ_DomainConsistency",
                    "type": DQ_DomainConsistency,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "resourceConstraintsMD_Identification",
                    "type": resourceConstraintsMD_Identification,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "sourceLI_Lineage",
                    "type": sourceLI_Lineage,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
                {
                    "name": "sourceStepsource",
                    "type": sourceStepsource,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
            ),
        },
    )
    bid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
        },
    )
    kind: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
        },
    )
