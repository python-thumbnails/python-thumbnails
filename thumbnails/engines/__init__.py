# -*- coding: utf-8 -*-
from thumbnails.engines.pillow import PillowEngine


def get_current_engine():
    return PillowEngine()
