# -*- coding: utf-8 -*-
# pylint: disable=C0301
"""Setup tests for this package."""
from __future__ import absolute_import
from eea.privacyscreen.testing import EEA_PRIVACYSCREEN_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that eea.privacyscreen is properly installed."""

    layer = EEA_PRIVACYSCREEN_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if eea.privacyscreen is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'eea.privacyscreen'))

    def test_browserlayer(self):
        """Test that IEeaPrivacyscreenLayer is registered."""
        from eea.privacyscreen.interfaces import (
            IEeaPrivacyscreenLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IEeaPrivacyscreenLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = EEA_PRIVACYSCREEN_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['eea.privacyscreen'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if eea.privacyscreen is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'eea.privacyscreen'))

    def test_browserlayer_removed(self):
        """Test that IEeaPrivacyscreenLayer is removed."""
        from eea.privacyscreen.interfaces import \
            IEeaPrivacyscreenLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IEeaPrivacyscreenLayer,
            utils.registered_layers())
