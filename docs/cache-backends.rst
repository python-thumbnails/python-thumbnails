Cache backends
--------------

The cache backends is used to store references to already created thumbnails in order to
avoid unnecessary disk or network usage. The ``Thumbnail`` object is cached and will be returned
directly in ``get_thumbnail`` if the cache returns it.

.. autoclass:: thumbnails.cache_backends.BaseCacheBackend
    :members:
    :private-members:

.. autoclass:: thumbnails.cache_backends.SimpleCacheBackend
    :members:
    :private-members:

.. autoclass:: thumbnails.cache_backends.DjangoCacheBackend
    :members:
    :private-members:

.. autoclass:: thumbnails.cache_backends.RedisCacheBackend
    :members:
    :private-members:
