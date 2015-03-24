# -*- coding: utf-8 -*-
from thumbnails import helpers
from thumbnails.conf import settings
from thumbnails.images import SourceFile, Thumbnail

__version__ = '0.1.0c4'


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
        size = engine.parse_size(size)
        thumbnail.image = engine.get_thumbnail(original, size, crop, options)
        thumbnail.save(options)

        for resolution in settings.THUMBNAIL_ALTERNATIVE_RESOLUTIONS:
            resolution_size = engine.calculate_alternative_resolution_size(resolution, size)
            image = engine.get_thumbnail(original, resolution_size, crop, options)
            thumbnail.save_alternative_resolution(resolution, image, options)

    cache.set(thumbnail)
    return thumbnail
