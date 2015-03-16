# -*- coding: utf-8 -*-
import hashlib

from thumbnails.engines import get_current_engine
from thumbnails.images import SourceFile, Thumbnail

CROP_ALIASES = {
    'x': {
        'left': 0,
        'center': 50,
        'right': 100
    },
    'y': {
        'top': 0,
        'center': 50,
        'bottom': 100
    }
}


class ThumbnailBackend(object):
    def get_thumbnail(self, original, size, crop=None, options=None):
        engine = get_current_engine()
        original = SourceFile(original)
        thumbnail_name = self.generate_filename(original, size, crop, options)
        cached = self.cache_get(thumbnail_name)

        if cached:
            return cached

        size = self.parse_size(size)
        crop = self.parse_crop(crop, size)
        thumbnail = self.create_thumbnail_object(thumbnail_name)

        if not thumbnail.exists():
            try:
                self.create_thumbnail(original, size, crop, options, thumbnail)
            finally:
                engine.cleanup(original)

        self.cache_set(thumbnail, original)
        return thumbnail

    def create_thumbnail(self, original_image, size, crop, options, thumbnail):
        thumbnail.image = get_current_engine().create(original_image, size, crop, options)
        print(thumbnail.image)

    def cache_get(self, thumbnail_name):
        return None

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
    def parse_crop(crop, original_size):
        if crop is None:
            return None

        crop = crop.split(' ')
        if len(crop) == 1:
            crop = crop[0]
            x_crop = 50
            y_crop = 50
            if crop in CROP_ALIASES['x']:
                x_crop = CROP_ALIASES['x'][crop]
            elif crop in CROP_ALIASES['y']:
                y_crop = CROP_ALIASES['y'][crop]
        else:
            if crop[0] in CROP_ALIASES['x']:
                x_crop = CROP_ALIASES['x'][crop[0]]
            else:
                x_crop = float(crop[0])

            if crop[0] in CROP_ALIASES['x']:
                y_crop = CROP_ALIASES['y'][crop[1]]
            else:
                y_crop = float(crop[1])

        x_offset = ThumbnailBackend.calculate_offset(x_crop, original_size[0])
        y_offset = ThumbnailBackend.calculate_offset(y_crop, original_size[1])
        return x_offset, y_offset

    @staticmethod
    def calculate_offset(percent, range):
        return int(max(0, min(percent * range / 100.0, range)))

    @staticmethod
    def generate_filename(original, size, crop, options):
        h = hashlib.sha1(':'.join([original.file, str(size), str(crop)]).encode()).hexdigest()
        return [h[:3], h[3:]]

    @staticmethod
    def create_thumbnail_object(name):
        return Thumbnail(name)

backend = ThumbnailBackend()
get_thumbnail = backend.get_thumbnail
