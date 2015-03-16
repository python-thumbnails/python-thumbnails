# -*- coding: utf-8 -*-
import os

THUMBNAIL_PATH = os.path.join(os.getcwd(), 'thumbnails')
THUMBNAIL_ENGINE = 'thumbnails.engines.PillowEngine'
THUMBNAIL_CACHE_BACKEND = 'thumbnails.cache_backends.SimpleCacheBackend'

THUMBNAIL_SCALE_UP = False

THUMBNAIL_DUMMY = False
THUMBNAIL_DUMMY_URL = 'http://puppies.lkng.me/{}x{}'
