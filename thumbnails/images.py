# -*- coding: utf-8 -*-
import os

import requests

from thumbnails.conf import settings


class Thumbnail(object):

    size = None, None
    image = None

    def __init__(self, name):
        self.name = name

    @property
    def path(self):
        return os.path.join(settings.THUMBNAIL_PATH, self.name)

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

    @property
    def exists(self):
        return os.path.exists(self.path)


class SourceFile(object):

    def __init__(self, source_file):
        self.file = source_file

    def open(self):
        if self.file.startswith('http'):
            return requests.get(self.file, stream=True).raw
        return open(self.file)
