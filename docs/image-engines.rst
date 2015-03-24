Image engines
-------------

python-thumbnails uses interchangeable image engines to make it possible to use the
imaging framework you like the best. python-thumbnails should have a few to select
from. However, if the framework you want to use is not supported. Extend ``BaseThumbnailEngine``
to create your own. If you think your engine is valuable to others a pull-request is always
appreciated.

.. autoclass:: thumbnails.engines.BaseThumbnailEngine
    :members:

.. autoclass:: thumbnails.engines.PillowEngine

.. autoclass:: thumbnails.engines.WandEngine

.. autoclass:: thumbnails.engines.DummyEngine
