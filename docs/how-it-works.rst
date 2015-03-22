How python-thumbnail works
--------------------------

python-thumbnails have a single function that should be used for most thumbnail generations.
It is ``thumbnails.get_thumbnail``. That function will use the correct backends to fetch or create
the thumbnail.

The first that will happen when that function is called is that a hash is generated based on the
image path or url, the wanted size, the wanted crop and other options that are given that differ
from the defaults [1]_. That hash is used to lookup in cache and in the file path of the thumbnail.

After the hash is created the thumbnail info will be retrieved from the cache, if it is in the
cache the function will return with the info about the thumbnail. In the case that the cache has no
information about the given hash the storage system will be checked to se if there is a saved
thumbnail for that hash. If there is, info about the thumbnail is returned.

If there exist no thumbnail file for the given hash the thumbnail will be created using the current
image engine and saved with the storage engine before saving the information about the created
thumbnail in the cache.

After creating the thumbnail an extra thumbnail will be created for every resolution listed in the
alternative resolution setting. Note that the there is no check if the alternative resolution
exists. The alternative resolution thumbnails will only be created if the standard resolution
thumbnail does not exist.

.. [1] The reason for only adding options that differ from the defaults is to avoid massive
       regeneration of thumbnails if the defaults changes.
