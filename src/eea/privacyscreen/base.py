ATTRIBUTES = {
    "data-embed-group": "group",
    "data-embed-screenshot": "screenshot",
    "data-embed-title": "embed_title"
}


DEFAULT_PRIVACY_STATEMENT = "Generic default privacy statement"


def detect_esri(src):
    if 'arcgis.com' in src:
        return True


PRIVACY_STATEMENTS = {
    "esri": {
        "detect": detect_esri,
        "text": """ This content is hosted by a third party (ESRI);
        by showing the external content you accept the terms and
        conditions of:
        <a
        target="_blank"
        href="https://www.esri.com/en-us/privacy/overview">www.esri.com/en-us/privacy/overview</a>
        """
    },
    "default": {
        "detect": lambda req: False,
        "text": DEFAULT_PRIVACY_STATEMENT,
    }
}


EMBED_BACKGROUNDS = {
    'map': '/++plone++privacyscreen/map.png'
}


def get_domain(src):
    """ Get the privacy settings domain to be used, based on request
    """

    for domain, info in PRIVACY_STATEMENTS.items():
        if info['detect'](src):
            return domain
