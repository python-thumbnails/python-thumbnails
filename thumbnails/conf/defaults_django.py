# -*- coding: utf-8 -*-
import os

from django.conf import settings as django_settings

THUMBNAIL_PATH = os.path.join(django_settings.MEDIA_ROOT, 'thumbnails-cache')
THUMBNAIL_URL = django_settings.MEDIA_URL + 'thumbnails-cache'
THUMBNAIL_CACHE_BACKEND = 'thumbnails.cache_backends.DjangoCacheBackend'
THUMBNAIL_STORAGE_BACKEND = 'thumbnails.storage_backends.DjangoStorageBackend'
