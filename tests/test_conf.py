# -*- coding: utf-8 -*-
import os
import unittest

from thumbnails.conf.wrapper import SettingsWrapper


class SettingsWrapperTestCase(unittest.TestCase):

    def test_default_values(self):
        settings = SettingsWrapper()
        self.assertEqual(settings.THUMBNAIL_ENGINE, 'thumbnails.engines.PillowEngine')

    def test_override_by_thumbnail_settings_module(self):
        os.environ['THUMBNAILS_SETTINGS_MODULE'] = 'tests.thumbnails_settings'
        settings = SettingsWrapper()
        self.assertEqual(settings.THUMBNAIL_ENGINE, 'thumbnails.engines.DummyEngine')
        del os.environ['THUMBNAILS_SETTINGS_MODULE']
