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

.. attribute:: THUMBNAIL_CACHE_TIMEOUT
    :noindex:

    | A timeout parameter for cache backends that does not support eternal items.
    | **Default:** ``60 * 60 * 24 * 365`` (a year in seconds)

.. attribute:: THUMBNAIL_STORAGE_BACKEND
    :noindex:

    | **Default:** ``thumbnails.storage_backends.FilesystemStorageBackend``
    | **Default in Django:** ``thumbnails.storage_backends.DjangoStorageBackend``


Image options
-------------

.. attribute:: THUMBNAIL_SCALE_UP
    :noindex:

    | If this is set to ``True`` the thumbnails can be scaled bigger than
      the original.
    | **Default:** ``False``

.. attribute:: THUMBNAIL_QUALITY
    :noindex:

    | Quality sent to the engine. 
    | **Default:** ``90``

.. attribute:: THUMBNAIL_COLORMODE
    :noindex:

    | The default colormode for thumbnails. Supports all values supported by pillow. In other
      engines there is a best effort translation from pillow modes to the modes supported by the
      current engine.
    | **Default:** ``'RGB'``

.. attribute:: THUMBNAIL_FALLBACK_FORMAT
    :noindex:

    | If the engine is not able to detect file type from the source or the file type is not
      supported this format will be used.
    | **Defaults:** ``'JPEG'``

.. attribute:: THUMBNAIL_FALLBACK_FORMAT
    :noindex:

    | This will override the original image format, however, passing format into ``get_thumbnail``
      will override this value.
    | **Defaults:** ``None``

.. attribute:: THUMBNAIL_ALTERNATIVE_RESOLUTIONS
    :noindex:

    | Defines which alternative resolutions should be created. Each item in the list will create
      an alternative version with the number as a proportions-factor.
    | **Default:** ``[2]``


Templatetags and filters
------------------------

.. attribute:: THUMBNAIL_FILTER_OPTIONS
    :noindex:

        | The options passed into ``get_thumbnail`` by the Markdown and HTML filter. It can contain
          all options that is supported by ``get_thumbnails``, however size is required.
        | **Default:** ``{'size': '500'}``


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
      and height, ``THUMBNAIL_DUMMY_URL.format(width=width, height=height)``
    | **Default:** `http://puppies.lkng.me/{width}x{height}`
