# -*- coding: utf-8 -*-
from thumbnails.conf import settings
from thumbnails.images import Thumbnail

from .base import ThumbnailBaseEngine


class DummmyEngine(ThumbnailBaseEngine):

    def create(self, original, size, crop, options=None):
        thumbnail = Thumbnail('dummy_{}x{}'.format(size[0], size[1]))
        thumbnail.size = size
        thumbnail._url = self._get_url(size)
        return thumbnail

    def _get_url(self, size):
        return settings.THUMBNAIL_DUMMY_URL.format(size[0], size[1])
