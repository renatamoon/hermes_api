# STANDARD IMPORTS
from enum import IntEnum


class InternalCode(IntEnum):
    SUCCESS = 200
    VALUE_ERROR = 10
    INTERNAL_SERVER_ERROR = 500

    def __repr__(self):
        return self.value
