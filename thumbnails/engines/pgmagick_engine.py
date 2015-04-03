# -*- coding: utf-8 -*-
from base64 import b64decode

from .base import BaseThumbnailEngine


class PgmagickEngine(BaseThumbnailEngine):
    """
    Image backend for pgmagick, requires the pgmagick package.
    """

    def __init__(self):
        super(PgmagickEngine, self).__init__()
        from pgmagick import Blob, Geometry, Image, ImageType
        self._Blob = Blob
        self._Geometry = Geometry
        self._Image = Image
        self._ImageType = ImageType

    def engine_load_image(self, original):
        blob = self._Blob()
        blob.update(original.open().read())
        return self._Image(blob)

    def engine_raw_data(self, image, options):
        image.magick(self.get_format(image, options))
        image.quality(options['quality'])
        blob = self._Blob()
        image.write(blob)
        return b64decode(blob.base64())

    def engine_image_size(self, image):
        geometry = image.size()
        return geometry.width(), geometry.height()

    def engine_scale(self, image, width, height):
        geometry = self._Geometry(width, height)
        image.scale(geometry)
        return image

    def engine_crop(self, image, size, crop, options):
        x, y = crop
        width, height = size
        geometry = self._Geometry(width, height, x, y)
        image.crop(geometry)
        return image

    def engine_cleanup(self, original):
        pass

    def engine_colormode(self, image, colormode):
        if colormode == 'RGB':
            image.type(self._ImageType.TrueColorMatteType)
        elif colormode == 'GRAY':
            image.type(self._ImageType.GrayscaleMatteType)
        return image

    def engine_get_format(self, image):
        _format = image.format()
        if _format == 'Joint Photographic Experts Group JFIF format':
            return 'JPEG'
        if _format == 'Portable Network Graphics':
            return 'PNG'
        if _format == 'CompuServe graphics interchange format':
            return 'GIF'
        return _format
