# -*- coding: utf-8 -*-


class ThumbnailBaseEngine(object):

    def create(self, image, size, crop=None, options=None):
        image = self.cropbox(image, size, crop, options)
        image = self.scale(image, size, crop, options)
        image = self.crop(image, size, crop, options)
        return image

    def cropbox(self, image, size, crop, options):
        raise NotImplementedError

    def scale(self, image, size, crop, options):
        raise NotImplementedError

    def crop(self, image, size, crop, options):
        raise NotImplementedError

    def parse_size(self, size):
        """
        Parses size string into a tuple
        :param size: String on the form '100', 'x100 or '100x200'
        :return: Tuple of two integers for width and height
        """
        if size.startswith('x'):
            return None, int(size.replace('x', ''))
        if 'x' in size:
            return int(size.split('x')[0]), int(size.split('x')[1])
        return int(size), None
