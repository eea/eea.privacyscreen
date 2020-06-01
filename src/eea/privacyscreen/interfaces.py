# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from collective.z3cform.datagridfield import DictRow
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.textfield import RichText
from plone.z3cform import layout
from z3c.form import form
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.schema import List
from zope.schema import TextLine


class IEeaPrivacyscreenLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IProtectedDestination(Interface):
    """
    """

    detect = TextLine(title=u"Regexp to detect this destination website",
                      required=True)
    statement = RichText(title=u"Privacy Statement", required=True)


class IProtectedDestinations(Interface):
    """ Client settings for ArcGIS
    """

    settings = List(title=u"Settings",
                    value_type=DictRow(title=u"Website Settings",
                                       schema=IProtectedDestination))


class ProtectedDestinationsControlPanelForm(RegistryEditForm):
    form.extends(RegistryEditForm)
    schema = IProtectedDestinations


ProtectedDestinationsControlPanelView = layout.wrap_form(
    ProtectedDestinationsControlPanelForm,
    ControlPanelFormWrapper
)
ProtectedDestinationsControlPanelView.label = \
    u"Privacy Screens for embedded content"
