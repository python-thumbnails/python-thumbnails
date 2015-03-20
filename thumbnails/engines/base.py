# -*- coding: utf-8 -*-
import os

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
    """
    A base class for Thumbnail engines. Any thumbnail engine should be a subclass of this and
    implement all methods prefixed with ``engine``.
    """

    def get_thumbnail(self, original, size, crop, options):
        """
        Wrapper for .create() with cleanup.

        :param original:
        :param size:
        :param crop:
        :param options:
        :return: An image object
        """
        try:
            image = self.create(original, self.parse_size(size), crop, options)
        finally:
            self.cleanup(original)
        return image

    def create(self, original, size, crop, options=None):
        """
        Creates a thumbnail. It loads the image, scales it and crops it.

        :param original:
        :param size:
        :param crop:
        :param options:
        :return:
        """
        _options = options
        options = self.default_options()
        if _options:
            options.update(_options)
        image = self.engine_load_image(original)
        image = self.scale(image, size, crop, options)
        crop = self.parse_crop(crop, self.get_image_size(image), size)
        image = self.crop(image, size, crop, options)
        return image

    def scale(self, image, size, crop, options):
        """
        Wrapper for ``engine_scale``, checks if the scaling factor is below one or that scale_up
        option is set to True before calling ``engine_scale``.

        :param image:
        :param size:
        :param crop:
        :param options:
        :return:
        """
        original_size = self.get_image_size(image)
        factor = self._calculate_scaling_factor(original_size, size, crop is not None)

        if factor < 1 or options['scale_up']:
            width = int(original_size[0] * factor)
            height = int(original_size[1] * factor)
            image = self.engine_scale(image, width, height)

        return image

    def crop(self, image, size, crop, options):
        """
        Wrapper for ``engine_crop``, will return without calling ``engine_crop`` if crop is None.

        :param image:
        :param size:
        :param crop:
        :param options:
        :return:
        """
        if not crop:
            return image
        return self.engine_crop(image, size, crop, options)

    def cleanup(self, original):
        """
        Cleanup after thumbnail creation.

        :param original:
        """
        self.engine_cleanup(original)

    def get_image_size(self, image):
        """
        Wrapper for ``engine_image_size``

        :param image:
        :return: A tuple with width and height
        :rtype: tuple
        """
        return self.engine_image_size(image)

    def save_image(self, image, options, location):
        """
        Wrapper for ``engine_save_image``. Ensures that the folder where the thumbnail should be
        saved exists.

        :param image:
        :param options:
        :param location: The location where the thumbnail should be stored.
        """
        directory = os.path.dirname(location)
        if not os.path.exists(directory):
            os.mkdir(directory)
        self.engine_save_image(image, options, location)

    def _calculate_scaling_factor(self, original_size, size, has_crop):
        factors = []
        if size[0] is not None:
            factors.append(float(size[0]) / original_size[0])
        if size[1] is not None:
            factors.append(float(size[1]) / original_size[1])

        if has_crop:
            return max(factors)
        return min(factors)

    def default_options(self):
        return {
            'scale_up': settings.THUMBNAIL_SCALE_UP,
            'quality': settings.THUMBNAIL_QUALITY
        }

    @staticmethod
    def parse_size(size):
        """
        Parses size string into a tuple

        :param size: String on the form '100', 'x100 or '100x200'
        :return: Tuple of two integers for width and height
        :rtype: tuple
        """
        if size.startswith('x'):
            return None, int(size.replace('x', ''))
        if 'x' in size:
            return int(size.split('x')[0]), int(size.split('x')[1])
        return int(size), None

    def parse_crop(self, crop, original_size, size):
        """
        Parses crop into a tuple usable by the crop function.

        :param crop: String with the crop settings.
        :param original_size: A tuple of size of the image that should be cropped.
        :param size: A tuple of the wanted size.
        :return: Tuple of two integers with crop settings
        :rtype: tuple
        """
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
        """
        Calculates crop offset based on percentage.

        :param percent: A percentage representing the size of the offset.
        :param original_length: The length the distance that should be cropped.
        :param length: The desired length.
        :return: The offset in pixels
        :rtype: int
        """
        return int(
            max(0,
                min(percent * original_length / 100.0, original_length - length / 2) - length / 2)
        )

    @staticmethod
    def create_thumbnail_object(name):
        return Thumbnail(name)

    def engine_load_image(self, original):
        """
        Engine specific loading of image, should be implemented by all subclasses.

        :param original: The file that should be loaded.
        :return: An image as an image object used by the engine.
        """
        raise NotImplementedError

    def engine_save_image(self, image, options, location):
        """
        Engine specific saving of image, should be implemented by all subclasses.

        :param image: The image object that should be saved.
        :param options: Options that should be used in order to save the image e.g. quality.
        :param location: The location where the image should be saved.
        """
        raise NotImplementedError

    def engine_image_size(self, image):
        """
        Engine specific fetching of image size, should be implemented by all subclasses.

        :param image: The image to check size of.
        :return: A tuple of two integers with width and height
        :rtype: tuple
        """
        raise NotImplementedError

    def engine_scale(self, image, width, height):
        """
        Engine specific scaling, should be implemented by all subclasses.

        :param image: The image object that should be scaled.
        :param width: The wanted width
        :param height: The wanted height
        :return:
        """
        raise NotImplementedError

    def engine_crop(self, image, size, crop, options):
        """
        Engine specific cropping, should be implemented by all subclasses.

        :param image:
        :param size:
        :param crop:
        :param options:
        :return:
        """
        raise NotImplementedError

    def engine_cleanup(self, original):
        """
        Engine specific cleanup, should be implemented by all subclasses.

        :param original:
        :return:
        """
        raise NotImplementedError
