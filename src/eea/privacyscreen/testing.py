# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import eea.privacyscreen


class EeaPrivacyscreenLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=eea.privacyscreen)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'eea.privacyscreen:default')


EEA_PRIVACYSCREEN_FIXTURE = EeaPrivacyscreenLayer()


EEA_PRIVACYSCREEN_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EEA_PRIVACYSCREEN_FIXTURE,),
    name='EeaPrivacyscreenLayer:IntegrationTesting',
)


EEA_PRIVACYSCREEN_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EEA_PRIVACYSCREEN_FIXTURE,),
    name='EeaPrivacyscreenLayer:FunctionalTesting',
)


EEA_PRIVACYSCREEN_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        EEA_PRIVACYSCREEN_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='EeaPrivacyscreenLayer:AcceptanceTesting',
)
