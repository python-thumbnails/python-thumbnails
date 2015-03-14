# -*- coding: utf-8 -*-

from . import defaults


class SettingsWrapper(object):

    defaults = {}

    def __init__(self):
        self._load_from_module(defaults, self.defaults)
        for setting in dir(defaults):
            setattr(self.defaults, setting, getattr(defaults, setting))

        self._load_django_settings()

    def __getattr__(self, key):
        value = self.defaults.get(key, None)

        if value is None:
            raise AttributeError()

        return value

    def _load_from_module(self, _module, target):
        for setting in dir(_module):
            setattr(target, setting, getattr(_module, setting))
