from collective.z3cform.datagridfield import BlockDataGridFieldFactory
from eea.privacyscreen.interfaces import IPrivacyScreenSettings
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.z3cform import layout
from z3c.form import form


class PrivacyScreenControlPanelForm(RegistryEditForm):
    form.extends(RegistryEditForm)
    schema = IPrivacyScreenSettings

    def updateFields(self):
        super(PrivacyScreenControlPanelForm, self).updateFields()
        self.fields['settings'].widgetFactory = BlockDataGridFieldFactory

    # def updateWidgets(self):
    #     super(PrivacyScreenControlPanelForm, self).updateWidgets()
    # self.widgets['settings'].allow_insert = True
    # self.widgets['settings'].allow_delete = True
    # self.widgets['settings'].auto_append = False
    # self.widgets['settings'].allow_reorder = False


PrivacyScreenControlPanelView = layout.wrap_form(
    PrivacyScreenControlPanelForm,
    ControlPanelFormWrapper
)
PrivacyScreenControlPanelView.label = \
    u"Privacy Screens for embedded content"
