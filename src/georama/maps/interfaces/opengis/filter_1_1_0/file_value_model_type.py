from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/gml"


class FileValueModelType(Enum):
    """
    List of codes that identifies the file structure model for records stored in
    files.
    """

    RECORD_INTERLEAVED = "Record Interleaved"
