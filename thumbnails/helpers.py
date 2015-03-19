# -*- coding: utf-8 -*-
import hashlib
import importlib

from thumbnails.conf import settings


def generate_filename(original, size, crop, options):
    h = hashlib.sha1(':'.join([original.file, str(size), str(crop)]).encode()).hexdigest()
    return [h[:3], h[3:]]


def get_engine():
    modules = settings.THUMBNAIL_ENGINE.split('.')
    return getattr(importlib.import_module('.'.join(modules[:len(modules) - 1])), modules[-1])()


def get_cache_backend():
    modules = settings.THUMBNAIL_CACHE_BACKEND.split('.')
    return getattr(importlib.import_module('.'.join(modules[:len(modules) - 1])), modules[-1])()
