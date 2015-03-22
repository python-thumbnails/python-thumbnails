# -*- coding: utf-8 -*-
import unittest

from thumbnails.conf import settings
from thumbnails.images import Thumbnail

from .compat import mock


class ThumbnailTestCase(unittest.TestCase):

    def setUp(self):
        self.instance = Thumbnail(['n', 'ame'])
        self.instance.size = 200, 400

    def test_name(self):
        self.assertEqual(self.instance.name, 'n/ame')

    def test_path(self):
        self.assertTrue(self.instance.path.endswith('thumbnails-cache/n/ame.jpg'))

    def test_url(self):
        self.assertTrue(self.instance.url.endswith('/n/ame.jpg'))

    def test_width(self):
        self.assertEqual(self.instance.width, 200)

    def test_height(self):
        self.assertEqual(self.instance.height, 400)

    def test_ratio(self):
        self.assertEqual(self.instance.ratio, 0.5)

    def test_is_portrait(self):
        self.assertTrue(self.instance.is_portrait)
        self.instance.size = 400, 200
        self.assertFalse(self.instance.is_portrait)

    def test_is_landscape(self):
        self.assertFalse(self.instance.is_landscape)
        self.instance.size = 400, 200
        self.assertTrue(self.instance.is_landscape)

    @mock.patch('{}.exists'.format(settings.THUMBNAIL_STORAGE_BACKEND))
    def test_exists(self, mock_exists):
        self.instance = Thumbnail(['name'])
        self.assertTrue(self.instance.exists)
        mock_exists.assert_called_with(self.instance.path)
