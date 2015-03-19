# -*- coding: utf-8 -*-
import unittest

from thumbnails.cache_backends import SimpleCacheBackend
from thumbnails.engines import PillowEngine
from thumbnails.helpers import generate_filename, get_cache_backend, get_engine
from thumbnails.images import SourceFile


class HelpersTestCase(unittest.TestCase):

    def test_generate_filename(self):
        self.assertEqual(
            generate_filename(SourceFile('url'), '100x200', 'center', None),
            ['0af', 'a360db703bd5c2fe7c83843ce7738a0a6d37b']
        )
        self.assertEqual(
            generate_filename(SourceFile('url'), '200x200', 'center', None),
            ['851', '521c21fe9709802e9d4eb20a5fe84c18cd3ad']
        )

    def test_get_engine(self):
        self.assertIsInstance(get_engine(), PillowEngine)

    def test_get_cache_backend(self):
        self.assertIsInstance(get_cache_backend(), SimpleCacheBackend)
