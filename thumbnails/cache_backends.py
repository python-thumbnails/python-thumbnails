# -*- coding: utf-8 -*-
import pickle
import re

from thumbnails import settings


class BaseCacheBackend(object):
    """
    Extendible cache backend that should be used when creating a new cache backend. Subclasses
    should only override methods prefixed with ``_``.
    """

    def __init__(self):
        self.TIMEOUT = settings.THUMBNAIL_CACHE_TIMEOUT

    def get(self, thumbnail_name):
        """
        Wrapper for ``_get``, which converts the thumbnail_name to String if necessary before
        calling ``_get``

        :rtype: Thumbnail
        """
        if isinstance(thumbnail_name, list):
            thumbnail_name = '/'.join(thumbnail_name)
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
        super(DjangoCacheBackend, self).__init__()
        from django.core.cache import cache  # noqa isort:skip
        self.cache = cache

    def _get(self, thumbnail_name):
        return self.cache.get(thumbnail_name.replace('/', ''))

    def _set(self, thumbnail_name, thumbnail):
        self.cache.set(thumbnail_name.replace('/', ''), thumbnail, timeout=self.TIMEOUT)


class RedisCacheBackend(BaseCacheBackend):
    """
    Cache backend that connects to Redis with redis-py. It uses the
    ``THUMBNAIL_CACHE_CONNECTION_URI`` setting as connection configuration.
    The setting should contain a string on the form: ``redis://host:port/db``,
    example: ``redis://127.0.0.1:6379/0`` will give the default settings.
    This backend does not sett time-to-live on the cached items, thus they will
    be in redis until they are deleted.

    If the settings string is not good enough for your configuration, it is possible to extend
    this backend and override ``get_settings``.
    """

    def __init__(self):
        import redis
        super(RedisCacheBackend, self).__init__()
        self.connection_uri = getattr(settings, 'THUMBNAIL_CACHE_CONNECTION_URI', None)
        self.redis = redis.StrictRedis(**self.get_settings())

    def _get(self, thumbnail_name):
        thumbnail = self.redis.get(thumbnail_name)
        if thumbnail is not None:
            return pickle.loads(thumbnail)

    def _set(self, thumbnail_name, thumbnail):
        return self.redis.set(thumbnail_name, pickle.dumps(thumbnail))

    def get_settings(self):
        """
        This creates a dict with keyword arguments used to create the redis client.
        It is used like ``redis.StrictClient(**self.get_settings())``. Thus, if the
        settings string is not enough to generate the wanted setting you can override
        this function.

        :return: A dict with keyword arguments for the redis client constructor.
        """
        host = '127.0.0.1'
        port = 6379
        db = 0
        if self.connection_uri is not None:
            re_connection_uri = r'redis://(?:([\w]+)@)?([\w\d\.]+):(\d+)(?:/(\d+))?'
            match = re.match(re_connection_uri, self.connection_uri)
            if match:
                if match.group(2):
                    host = match.group(2)
                if match.group(3):
                    port = int(match.group(3))
                if match.group(4):
                    db = int(match.group(4))

        return {
            'host': host,
            'port': port,
            'db': db
        }
