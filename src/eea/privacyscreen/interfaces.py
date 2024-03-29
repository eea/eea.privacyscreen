# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from __future__ import absolute_import
from collective.z3cform.datagridfield.registry import DictRow
# from plone.app.textfield import RichText
# from plone.app.z3cform.wysiwyg.widget import WysiwygFieldWidget
# from plone.autoform import directives
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.schema import Int
from zope.schema import Text
from zope.schema import TextLine
from zope.schema import Tuple


class IEeaPrivacyscreenLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IProtectedDestination(Interface):
    """ NOTE: Not used at the moment
    """

    detect = TextLine(title=u"Regexp to detect this destination website",
                      required=False)
    # directives.widget('statement', WysiwygFieldWidget)
    # statement = RichText(title=u"Privacy Statement", required=True)
    privacy_statement = Text(title=u"Privacy statement", required=False)


class IPrivacyScreenSettings(Interface):
    """ NOTE: Not used at the moment
    """

    settings = Tuple(title=u"Settings",
                     required=False,
                     value_type=DictRow(title=u"Website Settings",
                                        schema=IProtectedDestination))


class IEmbedScreenSettings(Interface):
    """ Generic settings for the embed screen

    Used for configuration form in control panel
    """

    lifetime_days = Int(title=u"Cookie lifetime, in days",
                        required=True,
                        default=10)
    cookie_domain = TextLine(
        title=u"Cookie domain",
        description=u"User preferences will be saved in a cookie for this "
        u"domain",
        default=u".eea.europa.eu"
    )
