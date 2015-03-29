0.4.0
~~~~~
 - Add support for base64 encoded images as source
 - Add support for colormode through setting the option ``colormode`` or the setting
   ``THUMBNAIL_COLORMODE``.

0.3.0
~~~~~
 - Add Django templatetag ``get_thumbnail``
 - Catch IOError and OSError in PillowEngine.engine_load_image and throw ThumbnailError, which
   will be catched in get_thumbnail if ``THUMBNAIL_DEBUG = False``.

0.2.1
~~~~~

0.2.0
~~~~~

 - PgmagickEngine
 - WandEngine
 - Higher maxblock in PillowEngine.engine_raw_data

0.1.0
~~~~~

 - Expendable image engine, storage backend and cache backend
 - PillowBackend
 - FilesystemStorageBackend
 - SimpleCacheBackend
 - RedisCacheBackend
 - Django integrations

   - DjangoStorageBackend
   - DjangoCacheBackend
   - Settings integration and defaults for django

 - Support for dummy thumbnails
