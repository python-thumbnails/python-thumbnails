# -*- coding: utf-8 -*-
import unittest

from thumbnails.cache_backends import BaseCacheBackend, DjangoCacheBackend, SimpleCacheBackend
from thumbnails.images import Thumbnail

from .compat import mock
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


class BaseCacheBackendTestCase(unittest.TestCase):

    def setUp(self):
        self.backend = BaseCacheBackend()

    def test_init(self):
        self.assertEqual(self.backend.TIMEOUT, 31536000)

    @mock.patch('thumbnails.cache_backends.BaseCacheBackend._get')
    def test_get_calls_backend_specific_get(self, mock__get):
        self.backend.get(['hi', 'there'])
        self.backend.get('key')
        mock__get.assert_has_calls([mock.call('hi/there'), mock.call('key')])

    @mock.patch('thumbnails.cache_backends.BaseCacheBackend._set')
    def test_set_calls_backend_specific_set(self, mock__set):
        thumbnail = Thumbnail(['hi', 'there'])
        self.backend.set(thumbnail)
        mock__set.assert_has_calls([mock.call('hi/there', thumbnail)])


class SimpleCacheBackendTestCase(CacheBackendTestMixin, unittest.TestCase):
    BACKEND = SimpleCacheBackend


@unittest.skipIf(not has_django(), 'Django is not installed')
class DjangoCacheBackendTestCase(CacheBackendTestMixin, unittest.TestCase):
    BACKEND = DjangoCacheBackend
