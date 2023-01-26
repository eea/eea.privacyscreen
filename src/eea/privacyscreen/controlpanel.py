""" Controlpanel """

from __future__ import absolute_import
from eea.privacyscreen.interfaces import IEmbedScreenSettings
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.z3cform import layout
from z3c.form import form


# from collective.z3cform.datagridfield import BlockDataGridFieldFactory
# from eea.privacyscreen.interfaces import IPrivacyScreenSettings


class EmbedScreenControlPanelForm(RegistryEditForm):
    form.extends(RegistryEditForm)
    schema = IEmbedScreenSettings

    # def updateFields(self):
    #     super(EmbedScreenControlPanelForm, self).updateFields()
    # self.fields['settings'].widgetFactory = BlockDataGridFieldFactory

    # def updateWidgets(self):
    #     super(PrivacyScreenControlPanelForm, self).updateWidgets()
    # self.widgets['settings'].allow_insert = True
    # self.widgets['settings'].allow_delete = True
    # self.widgets['settings'].auto_append = False
    # self.widgets['settings'].allow_reorder = False


EmbedScreenControlPanelView = layout.wrap_form(
    EmbedScreenControlPanelForm,
    ControlPanelFormWrapper
)
EmbedScreenControlPanelView.label = \
    u"Privacy Screens for embedded content"
