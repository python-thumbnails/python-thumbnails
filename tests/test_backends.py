# -*- coding: utf-8 -*-
import unittest

from thumbnails.backends import generate_filename, get_thumbnail
from thumbnails.images import SourceFile, Thumbnail

from .compat import mock


class BackendTestCase(unittest.TestCase):
    def test_generate_filename(self):
        self.assertEqual(
            generate_filename(SourceFile('url'), '100x200', 'center', None),
            ['0af', 'a360db703bd5c2fe7c83843ce7738a0a6d37b']
        )
        self.assertEqual(
            generate_filename(SourceFile('url'), '200x200', 'center', None),
            ['851', '521c21fe9709802e9d4eb20a5fe84c18cd3ad']
        )

    @mock.patch('thumbnails.backends.cache_get', lambda x:  True)
    def test_get_thumbnail_cached(self):
        self.assertTrue(get_thumbnail('', '200'))

    @mock.patch('thumbnails.engines.base.ThumbnailBaseEngine.get_thumbnail')
    def test_get_thumbnail(self, mock_engine_get_thumbnail):
        thumbnail = get_thumbnail('http://puppies.lkng.me/400x600/', '200')
        self.assertTrue(mock_engine_get_thumbnail.called)
        self.assertTrue(isinstance(thumbnail, Thumbnail))
