# -*- coding: utf-8 -*-
from thumbnails.conf import settings


class ThumbnailBaseEngine(object):

    def create(self, image, size, crop, options=None):
        if options is None:
            options = self.get_default_options()
        image = self.scale(image, size, crop, options)
        image = self.crop(image, size, crop, options)
        return image

    def scale(self, image, size, crop, options):
        upscale = options['scale_up']
        original_size = self.get_image_size(image)
        factor = self._calculate_scaling_factor(original_size, size, options)

        if factor < 1 or upscale:
            width = int(original_size[0] * factor)
            height = int(original_size[1] * factor)
            image = self.engine_scale(image, width, height)

        return image

    def crop(self, image, size, crop, options):
        if not crop:
            return image

        return self.engine_crop(image, size, crop, options)

    def engine_scale(self, image, width, height):
        raise NotImplementedError

    def engine_crop(self, image, size, crop, options):
        raise NotImplementedError

    def _calculate_scaling_factor(self, original_size, size, options):
        return NotImplemented

    def get_image_size(self, image):
        return NotImplemented

    def get_default_options(self):
        return {
            'scale_up': settings.THUMBNAIL_SCALE_UP
        }
