# -*- coding: utf-8 -*-
import unittest

from thumbnails.cache_backends import DjangoCacheBackend, SimpleCacheBackend
from thumbnails.images import Thumbnail

from .utils import has_django


class CacheBackendTestMixin(object):

    def setUp(self):
        self.backend = self.BACKEND()

    def test_get_empty(self):
        self.assertIsNone(self.backend.get('not-in-cache'))

    def test_set_and_get(self):
        thumbnail = Thumbnail(['n', 'ame'])
        self.backend.set(thumbnail)
        cached_thumbnail = self.backend.get(thumbnail.name)
        self.assertIsInstance(cached_thumbnail, Thumbnail)
        self.assertEqual(cached_thumbnail.name, thumbnail.name)


class SimpleCacheBackendTestCase(CacheBackendTestMixin, unittest.TestCase):
    BACKEND = SimpleCacheBackend


@unittest.skipIf(not has_django(), 'Django is not installed')
class DjangoCacheBackendTestCase(CacheBackendTestMixin, unittest.TestCase):
    BACKEND = DjangoCacheBackend
