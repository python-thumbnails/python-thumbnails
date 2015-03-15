# -*- coding: utf-8 -*-
import unittest

from thumbnails.backends import ThumbnailBackend
from thumbnails.images import Thumbnail


class BackendTestCase(unittest.TestCase):
    def test_generate_filename(self):
        self.assertEqual(
            ThumbnailBackend.generate_filename('url', '100x200', 'center', None),
            ['0af', 'a360db703bd5c2fe7c83843ce7738a0a6d37b']
        )
        self.assertEqual(
            ThumbnailBackend.generate_filename('url', '200x200', 'center', None),
            ['851', '521c21fe9709802e9d4eb20a5fe84c18cd3ad']
        )

    def test_create_thumbnail_object(self):
        name = ['851', '521c21fe9709802e9d4eb20a5fe84c18cd3ad']
        self.assertTrue(isinstance(ThumbnailBackend.create_thumbnail_object(name), Thumbnail))
