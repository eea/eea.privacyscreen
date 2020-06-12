from eea.privacyscreen.interfaces import IEmbedScreenSettings
from plone.registry.interfaces import IRegistry
from Products.Five.browser import BrowserView
from zope.component import getUtility


def detect_esri(request):
    return True


DEFAULT_PRIVACY_STATEMENT = "Generic default privacy statement"

PRIVACY_STATEMENTS = {
    "esri": {
        "detect": detect_esri,
        "text": """ This content is hosted by a third party (<a
        href="https://www.esri.com">www.esri.com</a>); by showing the
        external content you accept the terms and conditions of:
        <a
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


def get_domain(request):
    """ Get the privacy settings domain to be used, based on request
    """

    for domain, info in PRIVACY_STATEMENTS.items():
        if info['detect'](request):
            return domain


class PrivacyScreenPortal(BrowserView):
    """ Privacy screen portal, acceptance screen
    """

    def __call__(self):
        registry = getUtility(IRegistry, context=self.context)
        settings = registry.forInterface(IEmbedScreenSettings)

        domain = get_domain(self.request) or 'default'

        form = self.request.form

        self.title = form.get('embed_title', u'External content')
        self.embed_type = form.get('embed_type', 'map')
        self.portal_url = self.context.portal_url()
        self.iframe_url = form.get('src')
        self.group = form.get('group', 'default')

        # TODO: use embed_type to get fallback background
        self.embed_background = form.get(
            'screenshot', EMBED_BACKGROUNDS.get(self.embed_type))
        self.settings = settings
        self.privacy_notification = PRIVACY_STATEMENTS.get(domain)['text']
        return self.index()
