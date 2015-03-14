# -*- coding: utf-8 -*-
from thumbnails import engines

__version__ = '0.1.0'


def get_thumbnail(*args, **kwargs):
    return engines.get_current_engine().get_thumbnail(*args, **kwargs)
