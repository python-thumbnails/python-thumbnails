# -*- coding: utf-8 -*-
import os

from django.conf import settings

THUMBNAIL_PATH = os.path.join(settings.MEDIA_ROOT, 'thumbnails')
THUMBNAIL_URL = settings.MEDIA_URL + 'thumbnails'
THUMBNAIL_CACHE_BACKEND = 'thumbnails.cache_backends.DjangoCacheBackend'
