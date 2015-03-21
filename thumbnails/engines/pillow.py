# -*- coding: utf-8 -*-
from PIL import Image

from thumbnails.compat import BytesIO

from .base import BaseThumbnailEngine


class PillowEngine(BaseThumbnailEngine):
    """
    Thumbnail engine for Pillow
    """

    def engine_load_image(self, original):
        return Image.open(BytesIO(original.open().read()))

    def engine_raw_data(self, image, options):
        pillow_options = {
            'format': 'JPEG',
            'quality': options['quality'],
        }
        _file = BytesIO()
        image.save(_file, **pillow_options)
        return _file.getvalue()

    def engine_image_size(self, image):
        return image.size

    def engine_scale(self, image, width, height):
        return image.resize((width, height), resample=Image.ANTIALIAS)

    def engine_crop(self, image, size, crop, options):
        x, y = crop
        width, height = size
        return image.crop((x, y, x + width, y + height))

    def engine_cleanup(self, original):
        pass
