# -*- coding: utf-8 -*-
from copy import deepcopy
import os
import unittest
import mock

from tests.utils import has_no_django
from thumbnails.conf.wrapper import SettingsWrapper


class SettingsWrapperTestCase(unittest.TestCase):

    def test_default_values(self):
        settings = SettingsWrapper()
        self.assertEqual(settings.THUMBNAIL_ENGINE, 'thumbnails.engines.PillowEngine')

    def test_override_by_thumbnail_settings_module(self):
        env = deepcopy(os.environ)
        env['THUMBNAILS_SETTINGS_MODULE'] = 'tests.thumbnails_settings'

        with mock.patch.dict('os.environ', env):
            settings = SettingsWrapper()
            self.assertEqual(settings.THUMBNAIL_ENGINE, 'thumbnails.engines.DummyEngine')

        settings = SettingsWrapper()
        self.assertEqual(settings.THUMBNAIL_ENGINE, 'thumbnails.engines.PillowEngine')

    @unittest.skipIf(has_no_django(), 'Django not installed')
    def test_django_defaults(self):
        settings = SettingsWrapper()
        self.assertEqual(
            settings.THUMBNAIL_CACHE_BACKEND,
            'thumbnails.cache_backends.DjangoCacheBackend'
        )
