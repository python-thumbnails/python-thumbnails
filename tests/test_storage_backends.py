# -*- coding: utf-8 -*-
import os
import shutil
import unittest

from tests.utils import has_django
from thumbnails.storage_backends import (BaseStorageBackend, DjangoStorageBackend,
                                         FilesystemStorageBackend)


class StorageBackendTestMixin(object):

    def setUp(self):
        self.backend = self.BACKEND()

    def test_exists(self):
        self.assertTrue(self.backend.exists(os.path.join(os.getcwd(), 'setup.py')))
        self.assertFalse(self.backend.exists(os.path.join(os.getcwd(), 'stup.py')))

    def test_save(self):
        self.backend.save('t/est_file', b'123')
        self.assertTrue(os.path.exists(self.backend.path('t/est_file')))
        shutil.rmtree(self.backend.path('t'))


class BaseStorageBackendTestCase(unittest.TestCase):

    def setUp(self):
        self.backend = BaseStorageBackend()

    def test_path(self):
        self.assertEqual(self.backend.path('/an/absolute/path'), '/an/absolute/path')
        self.backend.location = 'location'
        self.assertEqual(self.backend.path('relative/path'), 'location/relative/path')


class FilesystemStorageBackendTestCase(StorageBackendTestMixin, unittest.TestCase):
    BACKEND = FilesystemStorageBackend

    def test_create_location_in_init(self):
        shutil.rmtree(self.backend.location)
        instance = self.BACKEND()
        os.path.exists(instance.location)


@unittest.skipIf(not has_django(), 'Django not installed')
class DjangoStorageBackendTestCase(StorageBackendTestMixin, unittest.TestCase):
    BACKEND = DjangoStorageBackend
