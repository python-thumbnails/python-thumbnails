# -*- coding: utf-8 -*-

from . import defaults


class SettingsWrapper(object):

    defaults = {}

    def __init__(self):
        self._load_from_module(defaults, self.defaults)

    def __getattr__(self, key):
        value = self.defaults.get(key, None)

        if value is None:
            raise AttributeError('No setting for "{}".'.format(key))

        return value

    def _load_from_module(self, _module, target):
        for setting in dir(_module):
            if not setting.startswith('_'):
                if isinstance(target, dict):
                    target[setting] = getattr(_module, setting)
                else:
                    setattr(target, setting, getattr(_module, setting))
