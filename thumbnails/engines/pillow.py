# -*- coding: utf-8 -*-
from PIL import Image

from thumbnails.compat import BytesIO
from thumbnails.engines.base import ThumbnailBaseEngine


class PillowEngine(ThumbnailBaseEngine):

    def engine_load_image(self, original):
        return Image.open(BytesIO(original.open().read()))

    def engine_save_image(self, image, options, location):
        pillow_options = {
            'quality': options['quality'],
        }
        image.save(location, **pillow_options)

    def engine_image_size(self, image):
        return image.size

    def engine_scale(self, image, width, height):
        return image.resize((width, height), resample=Image.ANTIALIAS)

    def engine_crop(self, image, size, crop, options):
        x, y = crop
        width, height = size
        return image.crop((x, y, x + width, y + height))
