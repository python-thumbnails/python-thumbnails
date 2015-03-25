# -*- coding: utf-8 -*-
from __future__ import absolute_import

from base64 import b64decode

from pgmagick import Blob, Geometry, Image

from .base import BaseThumbnailEngine


class PgmagickEngine(BaseThumbnailEngine):
    """
    Image backend for pgmagick, requires the pgpmagick package.
    """

    def engine_load_image(self, original):
        blob = Blob()
        blob.update(original.open().read())
        return Image(blob)

    def engine_raw_data(self, image, options):
        image.magick('JPEG')
        image.quality(options['quality'])
        blob = Blob()
        image.write(blob)
        return b64decode(blob.base64())

    def engine_image_size(self, image):
        geometry = image.size()
        return geometry.width(), geometry.height()

    def engine_scale(self, image, width, height):
        geometry = Geometry(width, height)
        image.scale(geometry)
        return image

    def engine_crop(self, image, size, crop, options):
        x, y = crop
        width, height = size
        geometry = Geometry(width, height, x, y)
        image.crop(geometry)
        return image

    def engine_cleanup(self, original):
        pass
