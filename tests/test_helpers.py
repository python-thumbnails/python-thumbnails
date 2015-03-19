# -*- coding: utf-8 -*-
import unittest

from thumbnails.helpers import generate_filename
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
