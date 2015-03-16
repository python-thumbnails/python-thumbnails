# -*- coding: utf-8 -*-
from abc import abstractmethod


class BaseCacheBackend(object):

    def get(self, thumbnail_name):
        if isinstance(thumbnail_name, list):
            thumbnail_name = ''.join(thumbnail_name)
        return self._get(thumbnail_name)

    def set(self, thumbnail):
        thumbnail_name = thumbnail.name
        if isinstance(thumbnail_name, list):
            thumbnail_name = ''.join(thumbnail_name)
        return self._set(thumbnail_name, thumbnail)

    @abstractmethod
    def _get(self, thumbnail_name):
        pass

    @abstractmethod
    def _set(self, thumbnail_name, thumbnail):
        pass


class SimpleCacheBackend(BaseCacheBackend):

    thumbnails = {}

    def _get(self, thumbnail_name):
        if thumbnail_name in self.thumbnails:
            return self.thumbnails[thumbnail_name]

    def _set(self, thumbnail_name, thumbnail):
        self.thumbnails[thumbnail_name] = thumbnail
