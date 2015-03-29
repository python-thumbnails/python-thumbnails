# -*- coding: utf-8 -*-
from PIL import Image, ImageFile

from thumbnails.compat import BytesIO
from thumbnails.errors import ThumbnailError

from .base import BaseThumbnailEngine


class PillowEngine(BaseThumbnailEngine):
    """
    Thumbnail engine for Pillow
    """

    def engine_load_image(self, original):
        image = Image.open(BytesIO(original.open().read()))
        try:
            image.load()
        except (IOError, OSError) as e:
            raise ThumbnailError('Could not load image', exception=e)
        return image

    def engine_raw_data(self, image, options):
        ImageFile.MAXBLOCK = max(ImageFile.MAXBLOCK, int(image.size[0] * image.size[1]))
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

    def engine_colormode(self, image, colormode):
        if colormode == 'RGB' or colormode == 'RGBA':
            if image.mode == 'RGBA':
                return image
            if image.mode == 'LA':
                return image.convert('RGBA')
            return image.convert(colormode)

        if colormode == 'GRAY':
            return image.convert('L')
        return image.convert(colormode)
