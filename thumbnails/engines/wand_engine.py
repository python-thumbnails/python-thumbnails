# -*- coding: utf-8 -*-

from .base import BaseThumbnailEngine


class WandEngine(BaseThumbnailEngine):
    """
    Image engine for wand.
    """
    def __init__(self):
        super(WandEngine, self).__init__()
        from wand.image import Image
        self._Image = Image

    def engine_image_size(self, image):
        return image.size

    def engine_load_image(self, original):
        return self._Image(blob=original.open().read())

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
        image.format = self.get_format(image, options)
        return image.make_blob()

    def engine_colormode(self, image, colormode):
        if colormode == 'RGB':
            image.type = 'truecolor'
        elif colormode == 'GRAY':
            image.type = 'grayscale'
        return image

    def engine_get_format(self, image):
        return image.format
