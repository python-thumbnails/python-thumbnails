# -*- coding: utf-8 -*-
from thumbnails.engines.base import BaseThumbnailEngine  # noqa
from thumbnails.engines.pillow import PillowEngine  # noqa
from thumbnails.engines.dummy import DummyEngine  # noqa

try:
    from thumbnails.engines.wand import WandEngine  # noqa
except ImportError:
    WandEngine = None


try:
    from thumbnails.engines.pgmagick import PgmagickEngine  # noqa
except ImportError:
    PgmagickEngine = None
