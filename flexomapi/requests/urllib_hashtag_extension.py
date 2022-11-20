import re
import urllib3


extension_enabled = False


def ensure_extension_enabled() -> bool:
    global extension_enabled
    if extension_enabled:
        return False

    urllib3.util.url.URI_RE = re.compile(
        r"^(?:([a-zA-Z][a-zA-Z0-9+.-]*):)?"
        r"(?://([^\\/?#]*))?"
        r"([^?]*)"
        r"(?:\?([^#]*))?"
        r"(?:#(.*))?$",
        re.UNICODE | re.DOTALL,
    )
    extension_enabled = True
    return True
