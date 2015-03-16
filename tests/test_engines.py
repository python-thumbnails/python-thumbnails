# -*- coding: utf-8 -*-
import os
import unittest

from PIL import Image

from thumbnails.engines.base import ThumbnailBaseEngine
from thumbnails.engines.dummy import DummmyEngine
from thumbnails.engines.pillow import PillowEngine
from thumbnails.images import SourceFile


class EngineTestMixin(object):

    def setUp(self):
        self.engine = self.ENGINE()
        self.filename = os.path.join(os.path.dirname(__file__), 'test_image.jpg')
        self.file = SourceFile(self.filename)
        self.url = SourceFile('http://puppies.lkng.me/400x600/')

        image = Image.new('L', (400, 600))
        image.save(self.filename)

    def tearDown(self):
        os.remove(self.filename)

    @unittest.skip('Awaiting')
    def test_create_from_file(self):
        thumbnail = self.engine.create(self.file, (200, 300), None)
        self.assertEqual(thumbnail.size[0], 200)
        self.assertEqual(thumbnail.size[1], 300)

    def test_create_from_url(self):
        thumbnail = self.engine.create(self.url, (200, 300), None)
        self.assertEqual(thumbnail.size[0], 200)
        self.assertEqual(thumbnail.size[1], 300)


class BaseEngineTestCase(EngineTestMixin, unittest.TestCase):
    ENGINE = ThumbnailBaseEngine

    def test_create_from_file(self):
        with self.assertRaises(NotImplementedError):
            self.engine.create(self.file, (200, 300), None)

    def test_create_from_url(self):
        with self.assertRaises(NotImplementedError):
            self.engine.create(self.url, (200, 300), None)


class PillowEngineTestCase(EngineTestMixin, unittest.TestCase):
    ENGINE = PillowEngine


class DummyEngineTestCase(EngineTestMixin, unittest.TestCase):
    ENGINE = DummmyEngine

    def test_create_from_file(self):
        thumbnail = self.engine.create(self.file, (200, 300), None)
        self.assertEqual(thumbnail.width, 200)
        self.assertEqual(thumbnail.height, 300)
        self.assertEqual(thumbnail.url, 'http://puppies.lkng.me/200x300')

    def test_create_from_url(self):
        thumbnail = self.engine.create(self.url, (200, 300), None)
        self.assertEqual(thumbnail.width, 200)
        self.assertEqual(thumbnail.height, 300)
        self.assertEqual(thumbnail.url, 'http://puppies.lkng.me/200x300')
