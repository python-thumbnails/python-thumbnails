# -*- coding: utf-8 -*-
import importlib
import json
import os


def has_installed(dependency):
    try:
        importlib.import_module(dependency)
        return True
    except ImportError:
        return False


def has_django():
    return has_installed('django')


def has_pillow():
    return has_installed('PIL.Image')


def has_redis():
    return has_installed('redis')


class OverrideSettings(object):

    def __init__(self, **settings):
        self.settings = settings

    def __enter__(self):
        os.environ['overridden_settings'] = json.dumps(self.settings)

    def __exit__(self, *args, **kwargs):
        del os.environ['overridden_settings']


override_settings = OverrideSettings
