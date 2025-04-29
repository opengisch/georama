from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.time_ordinal_reference_system_type import (
    TimeOrdinalReferenceSystemType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TimeOrdinalReferenceSystem(TimeOrdinalReferenceSystemType):
    """In some applications of geographic information — such as geology and
    archaeology — relative position in time is known more precisely than absolute
    time or duration.

    The order of events in time can be well established, but the
    magnitude of the intervals between them cannot be accurately
    determined; in such cases, the use of an ordinal temporal reference
    system is appropriate. An ordinal temporal reference system is
    composed of a sequence of named coterminous eras, which may in turn
    be composed of sequences of member eras at a finer scale, giving the
    whole a hierarchical structure of eras of verying resolution. An
    ordinal temporal reference system whose component eras are not
    further subdivided is effectively a temporal topological complex
    constrained to be a linear graph. An ordinal temporal reference
    system some or all of whose component eras are subdivided is
    effectively a temporal topological complex with the constraint that
    parallel branches may only be constructed in pairs where one is a
    single temporal ordinal era and the other is a sequence of temporal
    ordinal eras that are called "members" of the "group". This
    constraint means that within a single temporal ordinal reference
    system, the relative position of all temporal ordinal eras is
    unambiguous. The positions of the beginning and end of a given era
    may calibrate the relative time scale.
    gml:TimeOrdinalReferenceSystem adds one or more gml:component
    properties to the generic temporal reference system model.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
