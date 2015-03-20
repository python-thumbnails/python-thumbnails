# -*- coding: utf-8 -*-


class BaseCacheBackend(object):
    """
    Extendible cache backend that should be used when creating a new cache backend. Subclasses
    should only override methods prefixed with ``_``.
    """

    def get(self, thumbnail_name):
        """
        Wrapper for ``_get``, which converts the thumbnail_name to String if necessary before
        calling ``_get``

        :rtype: Thumbnail
        """
        if isinstance(thumbnail_name, list):
            thumbnail_name = ''.join(thumbnail_name)
        return self._get(thumbnail_name)

    def set(self, thumbnail):
        """
        Wrapper for ``_set``.
        """
        return self._set(thumbnail.name, thumbnail)

    def _get(self, thumbnail_name):
        """
        Backend specific handling of get, should be overridden by subclasses.

        :param thumbnail_name: String or list with the name/hash of the thumbnail.
        :rtype: Thumbnail
        """
        raise NotImplementedError

    def _set(self, thumbnail_name, thumbnail):
        """
        Backend specific handling of set, should be overridden by subclasses.

        :param thumbnail_name: String with the name of the thumbnail.
        :param thumbnail: The Thumbnail object that should be cached.
        """
        raise NotImplementedError


class SimpleCacheBackend(BaseCacheBackend):
    """
    Cache backend that stores objects in a dict on the backend instance.
    """

    thumbnails = {}

    def _get(self, thumbnail_name):
        if thumbnail_name in self.thumbnails:
            return self.thumbnails[thumbnail_name]

    def _set(self, thumbnail_name, thumbnail):
        self.thumbnails[thumbnail_name] = thumbnail


class DjangoCacheBackend(BaseCacheBackend):
    """
    Cache backend that uses Django's cache.
    """

    def __init__(self):
        from django.core.cache import cache  # noqa isort:skip
        self.cache = cache

    def _get(self, thumbnail_name):
        return self.cache.get(thumbnail_name.replace('/', ''))

    def _set(self, thumbnail_name, thumbnail):
        self.cache.set(thumbnail_name.replace('/', ''), thumbnail)
