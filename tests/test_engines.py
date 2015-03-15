# -*- coding: utf-8 -*-
import os
import unittest

from PIL import Image

from thumbnails.engines.base import ThumbnailBaseEngine
from thumbnails.engines.dummy import DummmyEngine


class EngineTestMixin(object):
    engine = None

    def setUp(self):
        self.engine = self.ENGINE()
        self.filename = os.path.join(os.path.dirname(__file__), 'test_image.jpg')
        image = Image.new('L', (400, 600))
        image.save(self.filename)

    def tearDown(self):
        os.remove(self.filename)

    def test_create(self):
        thumbnail = self.engine.create(self.filename, '200x300', None)
        self.assertEqual(thumbnail.width, 200)
        self.assertEqual(thumbnail.height, 300)
        self.assertEqual(thumbnail.url, '')


class BaseEngineTestCase(EngineTestMixin, unittest.TestCase):
    ENGINE = ThumbnailBaseEngine

    def test_create(self):
        with self.assertRaises(NotImplementedError):
            self.engine.create(self.filename, '200x300', None)

class DummyEngineTestCase(EngineTestMixin, unittest.TestCase):
    ENGINE = DummmyEngine

    def test_create(self):
        thumbnail = self.engine.create(self.filename, (200, 300), None)
        self.assertEqual(thumbnail.width, 200)
        self.assertEqual(thumbnail.height, 300)
        self.assertEqual(thumbnail.url, 'http://puppies.lkng.me/200x300')
