# -*- coding: utf-8 -*-
import hashlib

from thumbnails.engines import get_current_engine
from thumbnails.images import Thumbnail


class ThumbnailBackend(object):
    def get_thumbnail(self, original, size, crop=None, options=None):
        engine = get_current_engine()
        original = self.read_original(original)
        thumbnail_name = self.generate_filename(original, size, crop, options)
        cached = self.cache_get(thumbnail_name)

        if cached:
            return cached

        size = self.parse_size(size)
        crop = self.parse_crop(crop)
        thumbnail = self.create_thumbnail_object(thumbnail_name)

        if not thumbnail.exists():
            try:
                original_image = engine.get_image(original)
            except IOError:
                return thumbnail

            try:
                self.create_thumbnail(original_image, size, crop, options, thumbnail)
            finally:
                engine.cleanup(original_image)

        self.cache_set(thumbnail, original)
        return thumbnail

    def read_original(self, original):
        return NotImplemented

    def create_thumbnail(self, original_image, size, crop, options, thumbnail):
        return NotImplemented

    def cache_get(self, thumbnail_name):
        return NotImplemented

    def cache_set(self, thumbnail, original):
        return NotImplemented

    @staticmethod
    def parse_size(size):
        """
        Parses size string into a tuple
        :param size: String on the form '100', 'x100 or '100x200'
        :return: Tuple of two integers for width and height
        """
        if size.startswith('x'):
            return None, int(size.replace('x', ''))
        if 'x' in size:
            return int(size.split('x')[0]), int(size.split('x')[1])
        return int(size), None

    @staticmethod
    def parse_crop(crop):
        return 0, 0

    @staticmethod
    def generate_filename(original, size, crop, options):
        h = hashlib.sha1(':'.join([original, size, crop]).encode()).hexdigest()
        return [h[:3], h[3:]]

    @staticmethod
    def create_thumbnail_object(name):
        return Thumbnail(name)

backend = ThumbnailBackend()
get_thumbnail = backend.get_thumbnail
