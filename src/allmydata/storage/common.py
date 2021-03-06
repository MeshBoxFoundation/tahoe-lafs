from future.utils import PY3

import os.path
from allmydata.util import base32

class DataTooLargeError(Exception):
    pass
class UnknownMutableContainerVersionError(Exception):
    pass
class UnknownImmutableContainerVersionError(Exception):
    pass


def si_b2a(storageindex):
    return base32.b2a(storageindex)

def si_a2b(ascii_storageindex):
    return base32.a2b(ascii_storageindex)

def storage_index_to_dir(storageindex):
    """Convert storage index to directory path.

    Returns native string.
    """
    sia = si_b2a(storageindex)
    if PY3:
        # On Python 3 we expect paths to be unicode.
        sia = sia.decode("ascii")
    return os.path.join(sia[:2], sia)
