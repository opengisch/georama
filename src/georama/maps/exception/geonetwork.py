from georama.core.exceptions.base import GeoramaBaseError


class GeoNetworkError(GeoramaBaseError):
    def __init__(self, message="Request to GeoNetwork failed", uuid=None):
        self.uuid = uuid
        super().__init__(message)

    def __str__(self):
        base = super().__str__()
        if self.uuid:
            return f"[Record {self.uuid}] {base}"
        return base
