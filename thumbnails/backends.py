# -*- coding: utf-8 -*-
import hashlib

from thumbnails.engines import get_current_engine
from thumbnails.images import SourceFile, Thumbnail


def cache_get(thumbnail_name):
    return None


def cache_set(thumbnail, original):
    return NotImplemented


def generate_filename(original, size, crop, options):
    h = hashlib.sha1(':'.join([original.file, str(size), str(crop)]).encode()).hexdigest()
    return [h[:3], h[3:]]


def get_thumbnail(original, size, crop=None, options=None):
    engine = get_current_engine()
    original = SourceFile(original)
    thumbnail_name = generate_filename(original, size, crop, options)
    cached = cache_get(thumbnail_name)

    if cached:
        return cached

    thumbnail = Thumbnail(thumbnail_name)
    if not thumbnail.exists:
        thumbnail.image = engine.get_thumbnail(original, size, crop, options)
    cache_set(thumbnail, original)
    return thumbnail
