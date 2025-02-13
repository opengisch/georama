from dataclasses import dataclass

from wfs_2_0_0.net.opengis.ows.pkg_1.metadata_type import MetadataType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class OtherSource(MetadataType):
    """Reference to a source of metadata describing  coverage offerings available
    from this server.

    This  parameter can reference a catalogue server from which dataset
    metadata is available. This ability is expected to be used by
    servers with thousands or millions of datasets, for which searching
    a catalogue is more feasible than fetching a long Capabilities XML
    document. When no DatasetDescriptionSummaries are included, and one
    or more catalogue servers are referenced, this set of catalogues
    shall contain current metadata summaries for all the datasets
    currently available from this OWS server, with the metadata for each
    such dataset referencing this OWS server.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
