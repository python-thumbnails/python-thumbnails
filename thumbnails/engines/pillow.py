# -*- coding: utf-8 -*-
from thumbnails.compat import BytesIO
from thumbnails.engines.base import ThumbnailBaseEngine

try:
    from PIL import Image
except ImportError:
    import Image


class PillowEngine(ThumbnailBaseEngine):

    def engine_load_image(self, original):
        return Image.open(BytesIO(original.open().read()))

    def engine_save_image(self, image, location):
        image.save(location)

    def get_image_size(self, image):
        return image.size

    def get_image_info(self, image):
        return image.info or {}

    def engine_scale(self, image, width, height):
        return image.resize((width, height), resample=Image.ANTIALIAS)

    def engine_crop(self, image, size, crop, options):
        x, y = crop
        width, height = size
        return image.crop((x, y, x + width, y + height))
