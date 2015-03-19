Settings
========

.. attribute:: THUMBNAIL_PATH
    :noindex:

    | The path where thumbnails are saved.
    | **Default:** ``os.getcwd() + '/thumbnails-cache'``
    | **Default in Django:** ``django.conf.settings.MEDIA_ROOT + '/thumbnails-cache'``

.. attribute:: THUMBNAIL_URL
    :noindex:

    | The prefix for the url property of an Thumbnail object. The url property
      will contain this prefix and the relative path from ``THUMBNAIL_PATH``.
    | **Default:** ``'/thumbnails/''``
    | **Default in Django:** ``django.conf.settings.MEDIA_URL + '/thumbnails-cache'``

.. attribute:: THUMBNAIL_ENGINE
    :noindex:

    **Default:** ``thumbnails.engines.PillowEngine``

.. attribute:: THUMBNAIL_CACHE_BACKEND
    :noindex:

    | **Default:** ``thumbnails.cache_backends.SimpleCacheBackend``
    | **Default in Django:** ``thumbnails.cache_backends.DjangoCacheBackend``

Image options
-------------

.. attribute:: THUMBNAIL_SCALE_UP
    :noindex:

    | If this is set to ``True`` the thumbnails can be scaled bigger than
      the original.
    | **Default:** ``False``


Dummy thumbnails
----------------

.. attribute:: THUMBNAIL_DUMMY
    :noindex:

    | Activates the dummy thumbnail functionality, when this is active the
      original image will not be opened.
    | **Default:** `False`

.. attribute:: THUMBNAIL_DUMMY_FALLBACK
    :noindex:

    | Makes the dummy thumbnail functionality only be used if the thumbnail
      cannot be created.
    | **Default:** `False`

.. attribute:: THUMBNAIL_DUMMY_URL
    :noindex:

    | This is the url that the dummy url is generated from. It should be a
      string that can be used with ``string.format`` and the arguments are width
      and height, ``THUMBNAIL_DUMMY_URL.format(width, height)``
    | **Default:** `http://puppies.lkng.me/{}x{}`
