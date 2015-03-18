# -*- coding: utf-8 -*-
from thumbnails.conf import settings
from thumbnails.images import Thumbnail

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


class ThumbnailBaseEngine(object):

    def get_thumbnail(self, original, size, crop, options):
        try:
            image = self.create(original, self.parse_size(size), crop, options)
        finally:
            self.cleanup(original)
        return image

    def create(self, original, size, crop, options=None):
        if options is None:
            options = self.get_default_options()
        image = self.engine_load_image(original)
        image = self.scale(image, size, crop, options)
        crop = self.parse_crop(crop, self.get_image_size(image), size)
        image = self.crop(image, size, crop, options)
        return image

    def scale(self, image, size, crop, options):
        original_size = self.get_image_size(image)

        if original_size is NotImplemented:
            raise NotImplementedError

        factor = self._calculate_scaling_factor(original_size, size, crop is not None)

        if factor < 1 or options['scale_up']:
            width = int(original_size[0] * factor)
            height = int(original_size[1] * factor)
            image = self.engine_scale(image, width, height)

        return image

    def crop(self, image, size, crop, options):
        if not crop:
            return image
        return self.engine_crop(image, size, crop, options)

    def cleanup(self, original):
        pass

    def get_image_size(self, image):
        return self.engine_image_size(image)

    def get_image_info(self, image):
        return self.engine_image_info(image) or {}

    def engine_load_image(self, original):
        raise NotImplementedError

    def engine_save_image(self, image, location):
        raise NotImplementedError

    def engine_image_size(self, image):
        raise NotImplementedError

    def engine_image_info(self, image):
        raise NotImplementedError

    def engine_scale(self, image, width, height):
        raise NotImplementedError

    def engine_crop(self, image, size, crop, options):
        raise NotImplementedError

    def _calculate_scaling_factor(self, original_size, size, has_crop):
        factors = []
        if size[0] is not None:
            factors.append(float(size[0]) / original_size[0])
        if size[1] is not None:
            factors.append(float(size[1]) / original_size[1])

        if has_crop:
            return max(factors)
        return min(factors)

    def get_default_options(self):
        return {
            'scale_up': settings.THUMBNAIL_SCALE_UP
        }

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

    def parse_crop(self, crop, original_size, size):
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

        x_offset = self.calculate_offset(x_crop, original_size[0], size[0])
        y_offset = self.calculate_offset(y_crop, original_size[1], size[1])
        return int(x_offset), int(y_offset)

    @staticmethod
    def calculate_offset(percent, original_length, length):
        return int(max(0, min(percent * original_length / 100.0, original_length - length / 2) - length / 2))

    @staticmethod
    def create_thumbnail_object(name):
        return Thumbnail(name)
