# -*- coding: utf-8 -*-
from __future__ import absolute_import

from wand.image import Image

from .base import BaseThumbnailEngine


class WandEngine(BaseThumbnailEngine):
    """
    Image engine for wand.
    """

    def engine_image_size(self, image):
        return image.size

    def engine_load_image(self, original):
        return Image(blob=original.open().read())

    def engine_scale(self, image, width, height):
        image.resize(width, height)
        return image

    def engine_cleanup(self, original):
        pass

    def engine_crop(self, image, size, crop, options):
        x, y = crop
        width, height = size
        image.crop(x, y, width=width, height=height)
        return image

    def engine_raw_data(self, image, options):
        image.compression_quality = options['quality']
        return image.make_blob()
