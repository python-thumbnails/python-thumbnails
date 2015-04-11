# -*- coding: utf-8 -*-
import os

THUMBNAIL_PATH = os.path.join(os.getcwd(), 'thumbnails-cache')
THUMBNAIL_URL = '/thumbnails/'
THUMBNAIL_ENGINE = 'thumbnails.engines.PillowEngine'
THUMBNAIL_CACHE_BACKEND = 'thumbnails.cache_backends.SimpleCacheBackend'
THUMBNAIL_CACHE_TIMEOUT = 60 * 60 * 24 * 365
THUMBNAIL_CACHE_CONNECTION_URI = None
THUMBNAIL_STORAGE_BACKEND = 'thumbnails.storage_backends.FilesystemStorageBackend'

THUMBNAIL_SCALE_UP = False
THUMBNAIL_QUALITY = 90
THUMBNAIL_COLORMODE = 'RGB'
THUMBNAIL_FALLBACK_FORMAT = 'JPEG'
THUMBNAIL_FORCE_FORMAT = None
THUMBNAIL_ALTERNATIVE_RESOLUTIONS = [2]

THUMBNAIL_FILTER_SIZE = '500'
THUMBNAIL_FILTER_OPTIONS = {'size': '500'}

THUMBNAIL_DUMMY = False
THUMBNAIL_DUMMY_URL = 'http://puppies.lkng.me/{width}x{height}'
