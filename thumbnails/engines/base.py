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


    def _calculate_scaling_factor(self, original_size, size, options):
        return 1

