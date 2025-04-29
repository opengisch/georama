from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.file_type import FileType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class File(FileType):
    """For efficiency reasons, GML also provides a means of encoding the range set
    in an arbitrary external encoding, such as a binary file.

    This encoding may be "well-known" but this is not required. This
    mode uses the gml:File element. The values of the coverage
    (attribute values in the range set) are transmitted in a external
    file that is referenced from the XML structure described by
    gml:FileType.  The external file is referenced by the
    gml:fileReference property that is an anyURI (the gml:fileName
    property has been deprecated).  This means that the external file
    may be located remotely from the referencing GML instance. The
    gml:compression property points to a definition of a compression
    algorithm through an anyURI.  This may be a retrievable, computable
    definition or simply a reference to an unambiguous name for the
    compression method. The gml:mimeType property points to a definition
    of the file mime type. The gml:fileStructure property is defined by
    a codelist. Note further that all values shall be enclosed in a
    single file. Multi-file structures for values are not supported in
    GML. The semantics of the range set is described as above using the
    gml:rangeParameters property. Note that if any compression algorithm
    is applied, the structure above applies only to the pre-compression
    or post-decompression structure of the file. Note that the fields
    within a record match the gml:valueComponents of the
    gml:CompositeValue in document order.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
