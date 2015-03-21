# -*- coding: utf-8 -*-
from thumbnails import helpers
from thumbnails.images import SourceFile, Thumbnail

__version__ = '0.1.0'


def get_thumbnail(original, size, crop=None, options=None):
    engine = helpers.get_engine()
    cache = helpers.get_cache_backend()
    original = SourceFile(original)
    thumbnail_name = helpers.generate_filename(original, size, crop, options)
    cached = cache.get(thumbnail_name)

    if cached:
        return cached

    thumbnail = Thumbnail(thumbnail_name)
    if not thumbnail.exists:
        options = engine.evaluate_options(options)
        thumbnail.image = engine.get_thumbnail(original, size, crop, options)
        thumbnail.save(options)
    cache.set(thumbnail)
    return thumbnail
