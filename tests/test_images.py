# -*- coding: utf-8 -*-
import unittest

from thumbnails.images import Thumbnail


class ThumbnailTestCase(unittest.TestCase):

    def setUp(self):
        self.instance = Thumbnail('name')
        self.instance.size = 200, 400

    def test_name(self):
        self.assertEqual(self.instance.name, 'name')

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
