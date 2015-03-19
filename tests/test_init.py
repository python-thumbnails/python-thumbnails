# -*- coding: utf-8 -*-
import unittest

from thumbnails import get_thumbnail
from thumbnails.conf import settings
from thumbnails.images import Thumbnail

from .compat import mock


class GetThumbnailTestCase(unittest.TestCase):

    @mock.patch('{}.get'.format(settings.THUMBNAIL_CACHE_BACKEND), lambda o, x:  True)
    def test_get_thumbnail_cached(self):
        self.assertTrue(get_thumbnail('', '200'))

    @mock.patch('thumbnails.engines.base.ThumbnailBaseEngine.get_thumbnail')
    @mock.patch('thumbnails.engines.base.ThumbnailBaseEngine.save_image')
    @mock.patch('{}.set'.format(settings.THUMBNAIL_CACHE_BACKEND))
    def test_get_thumbnail(self, mock_engine_get_thumbnail, mock_save_image, mock_cache_set):
        thumbnail = get_thumbnail('http://puppies.lkng.me/400x600/', '200')
        self.assertTrue(mock_engine_get_thumbnail.called)
        self.assertTrue(mock_cache_set.called)
        self.assertTrue(mock_save_image.called)
        self.assertIsInstance(thumbnail, Thumbnail)
