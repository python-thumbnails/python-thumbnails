# -*- coding: utf-8 -*-
import unittest

from tests.utils import has_no_django
from thumbnails.cache_backends import DjangoCacheBackend, SimpleCacheBackend
from thumbnails.images import Thumbnail


class CacheBackendTestMixin(object):

    def setUp(self):
        self.backend = self.BACKEND()

    def test_get_empty(self):
        self.assertIsNone(self.backend.get('not-in-cache'))

    def test_set_and_get(self):
        thumbnail = Thumbnail(['n', 'ame'])
        self.backend.set(thumbnail)
        cached_thumbnail = self.backend.get(thumbnail.name)
        print(cached_thumbnail)
        self.assertTrue(isinstance(cached_thumbnail, Thumbnail))
        self.assertEqual(cached_thumbnail.name, thumbnail.name)


class SimpleCacheBackendTestCase(CacheBackendTestMixin, unittest.TestCase):
    BACKEND = SimpleCacheBackend


@unittest.skipIf(has_no_django(), 'Django is not installed')
class DjangoCacheBackendTestCase(CacheBackendTestMixin, unittest.TestCase):
    BACKEND = DjangoCacheBackend
