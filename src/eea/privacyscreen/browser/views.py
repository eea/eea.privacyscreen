""" Views """

from __future__ import absolute_import
from eea.privacyscreen.base import EMBED_BACKGROUNDS
from eea.privacyscreen.base import get_domain
from eea.privacyscreen.base import PRIVACY_STATEMENTS
from eea.privacyscreen.interfaces import IEmbedScreenSettings
from plone.registry.interfaces import IRegistry
from Products.Five.browser import BrowserView
from zope.component import getUtility


class PrivacyScreenPortal(BrowserView):
    """ Privacy screen portal, acceptance screen
    """

    def __call__(self):
        registry = getUtility(IRegistry, context=self.context)
        settings = registry.forInterface(IEmbedScreenSettings)

        domain = get_domain(self.request.form.get('src', '')) or 'default'

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
