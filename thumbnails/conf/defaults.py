# -*- coding: utf-8 -*-
import os

THUMBNAIL_PATH = os.path.join(os.getcwd(), 'thumbnails-cache')
THUMBNAIL_URL = '/thumbnails/'
THUMBNAIL_ENGINE = 'thumbnails.engines.PillowEngine'
THUMBNAIL_CACHE_BACKEND = 'thumbnails.cache_backends.SimpleCacheBackend'
THUMBNAIL_STORAGE_BACKEND = 'thumbnails.storage_backends.FilesystemStorageBackend'

THUMBNAIL_SCALE_UP = False
THUMBNAIL_QUALITY = 90
THUMBNAIL_ALTERNATIVE_RESOLUTIONS = [2]

THUMBNAIL_DUMMY = False
THUMBNAIL_DUMMY_URL = 'http://puppies.lkng.me/{}x{}'
