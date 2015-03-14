# -*- coding: utf-8 -*-


class Thumbnail(object):

    size = None, None

    def __init__(self):
        pass

    @property
    def width(self):
        return self.size[0]

    @property
    def height(self):
        return self.size[1]

    @property
    def ratio(self):
        return float(self.width) / float(self.height)

    @property
    def is_portrait(self):
        return self.ratio < 1

    @property
    def is_landscape(self):
        return self.ratio > 1
