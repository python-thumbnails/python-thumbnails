# -*- coding: utf-8 -*-
import hashlib
import importlib

from thumbnails.conf import settings
from thumbnails.images import SourceFile, Thumbnail


def get_engine():
    modules = settings.THUMBNAIL_ENGINE.split('.')
    return getattr(importlib.import_module('.'.join(modules[:len(modules) - 1])), modules[-1])()


def get_cache_backend():
    modules = settings.THUMBNAIL_CACHE_BACKEND.split('.')
    return getattr(importlib.import_module('.'.join(modules[:len(modules) - 1])), modules[-1])()


def generate_filename(original, size, crop, options):
    h = hashlib.sha1(':'.join([original.file, str(size), str(crop)]).encode()).hexdigest()
    return [h[:3], h[3:]]


def get_thumbnail(original, size, crop=None, options=None):
    engine = get_engine()
    cache = get_cache_backend()
    original = SourceFile(original)
    thumbnail_name = generate_filename(original, size, crop, options)
    cached = cache.get(thumbnail_name)

    if cached:
        return cached

    thumbnail = Thumbnail(thumbnail_name)
    if not thumbnail.exists:
        thumbnail.image = engine.get_thumbnail(original, size, crop, options)
    cache.set(thumbnail)
    return thumbnail
