# -*- coding: utf-8 -*-
from thumbnails.engines.base import BaseThumbnailEngine  # noqa
from thumbnails.engines.dummy import DummyEngine  # noqa


try:
    from thumbnails.engines.pillow_engine import PillowEngine  # noqa
except ImportError:
    PillowEngine = None


try:
    from thumbnails.engines.wand_engine import WandEngine  # noqa
except ImportError:
    WandEngine = None


try:
    from thumbnails.engines.pgmagick_engine import PgmagickEngine  # noqa
except ImportError:
    PgmagickEngine = None
