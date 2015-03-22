# -*- coding: utf-8 -*-
import hashlib
import os
import unittest

from PIL import Image

from thumbnails.engines.base import BaseThumbnailEngine
from thumbnails.engines.dummy import DummyEngine
from thumbnails.engines.pillow import PillowEngine
from thumbnails.errors import ThumbnailError
from thumbnails.images import SourceFile, Thumbnail

from .compat import mock
from .utils import has_pillow


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

    @mock.patch('thumbnails.engines.BaseThumbnailEngine.create')
    @mock.patch('thumbnails.engines.BaseThumbnailEngine.cleanup')
    def test_get_thumbnail(self, mock_create, mock_cleanup):
        self.engine.get_thumbnail(self.file, '200', None, None)
        self.assertTrue(mock_create.called)
        self.assertTrue(mock_cleanup.called)

    @mock.patch('thumbnails.engines.BaseThumbnailEngine.create', side_effect=ThumbnailError())
    @mock.patch('thumbnails.engines.BaseThumbnailEngine.cleanup')
    def test_get_thumbnail_fail(self, mock_create, mock_cleanup):
        self.engine.get_thumbnail(self.file, '200', None, None)
        self.assertTrue(mock_create.called)
        self.assertTrue(mock_cleanup.called)

    def test_create_from_file(self):
        thumbnail = self.engine.create(self.file, (200, 300), None)
        self.assertEqual(thumbnail.size[0], 200)
        self.assertEqual(thumbnail.size[1], 300)

    def test_create_from_url(self):
        thumbnail = self.engine.create(self.url, (200, 300), None)
        self.assertEqual(thumbnail.size[0], 200)
        self.assertEqual(thumbnail.size[1], 300)

    def test_create_with_crop(self):
        thumbnail = self.engine.create(self.url, (200, 200), 'center')
        self.assertEqual(thumbnail.size[0], 200)
        self.assertEqual(thumbnail.size[1], 200)

    def test_no_scale_no_crop(self):
        thumbnail = self.engine.create(self.url, (400, 600), None)
        self.assertEqual(thumbnail.size[0], 400)
        self.assertEqual(thumbnail.size[1], 600)

    def test_raw_data(self):
        image = Image.new('L', (400, 600))
        raw_data = self.engine.raw_data(image, self.engine.default_options())
        self.assertEqual(
            hashlib.sha1(raw_data).hexdigest(),
            'cd63a4ccd85070c76db822ca5ccb11ba59966256'
        )

    def test_cleanup(self):
        self.assertIsNone(self.engine.cleanup(self.file))


class BaseEngineTestCase(unittest.TestCase):

    def setUp(self):
        self.engine = BaseThumbnailEngine()

    def test__calculate_scaling_factor_without_crop(self):
        calculate_scaling_factor = self.engine._calculate_scaling_factor
        original_size = (400, 600)
        self.assertEqual(calculate_scaling_factor(original_size, (400, 600), False), 1)
        self.assertEqual(calculate_scaling_factor(original_size, (100, 600), False), 0.25)
        self.assertEqual(calculate_scaling_factor(original_size, (400, 300), False), 0.5)
        self.assertEqual(calculate_scaling_factor(original_size, (200, 300), False), 0.5)
        self.assertEqual(calculate_scaling_factor(original_size, (200, None), False), 0.5)
        self.assertEqual(calculate_scaling_factor(original_size, (None, 300), False), 0.5)

    def test_create_thumbnail_object(self):
        name = ['851', '521c21fe9709802e9d4eb20a5fe84c18cd3ad']
        self.assertIsInstance(self.engine.create_thumbnail_object(name), Thumbnail)

    def test_parse_size(self):
        self.assertEqual(self.engine.parse_size('100'), (100, None))
        self.assertEqual(self.engine.parse_size('100x200'), (100, 200))
        self.assertEqual(self.engine.parse_size('1x10'), (1, 10))
        self.assertEqual(self.engine.parse_size('x1000'), (None, 1000))

    def test_parse_crop(self):
        self.assertEqual(self.engine.parse_crop('center', (200, 200), (100, 100)), (50, 50))
        self.assertEqual(self.engine.parse_crop('top', (200, 200), (100, 100)), (50, 0))
        self.assertEqual(self.engine.parse_crop('bottom', (200, 200), (100, 100)), (50, 100))
        self.assertEqual(self.engine.parse_crop('left', (200, 200), (100, 100)), (0, 50))
        self.assertEqual(self.engine.parse_crop('right', (200, 200), (100, 100)), (100, 50))

    def test_calculate_offset(self):
        self.assertEqual(self.engine.calculate_offset(0, 1000, 200), 0)
        self.assertEqual(self.engine.calculate_offset(50, 1000, 200), 400)
        self.assertEqual(self.engine.calculate_offset(100, 1000, 200), 800)

    def test_evaluate_options(self):
        self.assertEqual(self.engine.evaluate_options(None), self.engine.default_options())
        self.assertEqual(self.engine.evaluate_options({}), self.engine.default_options())
        self.assertEqual(self.engine.evaluate_options({'quality': 50})['quality'], 50)
        self.assertEqual(
            len(self.engine.evaluate_options({'quality': 50}).keys()),
            len(self.engine.evaluate_options({}).keys()),
        )

    def test_calculate_alternative_resolution_size(self):
        self.assertEqual(
            self.engine.calculate_alternative_resolution_size(2, (100, None)),
            (200, None)
        )
        self.assertEqual(
            self.engine.calculate_alternative_resolution_size(2, (100, 150)),
            (200, 300)
        )
        self.assertEqual(
            self.engine.calculate_alternative_resolution_size(2, (None, 150)),
            (None, 300)
        )
        self.assertEqual(
            self.engine.calculate_alternative_resolution_size(1.5, (100, 100)),
            (150, 150)
        )


class DummyEngineTestCase(unittest.TestCase):

    def setUp(self):
        self.engine = DummyEngine()
        self.filename = os.path.join(os.path.dirname(__file__), 'test_image.jpg')
        self.file = SourceFile(self.filename)
        self.url = SourceFile('http://puppies.lkng.me/400x600/')

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


@unittest.skipIf(not has_pillow(), 'Pillow not installed')
class PillowEngineTestCase(EngineTestMixin, unittest.TestCase):
    ENGINE = PillowEngine
