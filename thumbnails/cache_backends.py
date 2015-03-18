# -*- coding: utf-8 -*-


class BaseCacheBackend(object):

    def get(self, thumbnail_name):
        if isinstance(thumbnail_name, list):
            thumbnail_name = ''.join(thumbnail_name)
        return self._get(thumbnail_name)

    def set(self, thumbnail):
        return self._set(thumbnail.name, thumbnail)

    def _get(self, thumbnail_name):
        raise NotImplementedError

    def _set(self, thumbnail_name, thumbnail):
        raise NotImplementedError


class SimpleCacheBackend(BaseCacheBackend):

    thumbnails = {}

    def _get(self, thumbnail_name):
        if thumbnail_name in self.thumbnails:
            return self.thumbnails[thumbnail_name]

    def _set(self, thumbnail_name, thumbnail):
        self.thumbnails[thumbnail_name] = thumbnail


class DjangoCacheBackend(BaseCacheBackend):

    def __init__(self):
        from django.core.cache import cache  # noqa isort:skip
        self.cache = cache

    def _get(self, thumbnail_name):
        return self.cache.get(thumbnail_name.replace('/', ''))

    def _set(self, thumbnail_name, thumbnail):
        self.cache.set(thumbnail_name.replace('/', ''), thumbnail)
