from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.ogc.wfs_2_0_0.code_type import CodeType
from georama.maps.interfaces.ogc.wfs_2_0_0.language_string_type import (
    LanguageStringType,
)

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class KeywordsType:
    """Unordered list of one or more commonly used or formalised word(s) or
    phrase(s) used to describe the subject.

    When needed, the optional "type" can name the type of the associated
    list of keywords that shall all have the same type. Also when
    needed, the codeSpace attribute of that "type" can reference the
    type name authority and/or thesaurus. If the xml:lang attribute is
    not included in a Keyword element, then no language is specified for
    that element unless specified by another means.  All Keyword
    elements in the same Keywords element that share the same xml:lang
    attribute value represent different keywords in that language. For
    OWS use, the optional thesaurusName element was omitted as being
    complex information that could be referenced by the codeSpace
    attribute of the Type element.
    """

    keyword: list[LanguageStringType] = field(
        default_factory=list,
        metadata={
            "name": "Keyword",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
            "min_occurs": 1,
        },
    )
    type_value: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
