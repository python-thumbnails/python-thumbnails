# -*- coding: utf-8 -*-
import codecs
import os

from .conf import settings
from .compat import makedirs


class BaseStorageBackend(object):

    def __init__(self):
        self.location = settings.THUMBNAIL_PATH

    def path(self, path):
        """
        Creates a path based on the location attribute of the backend and the path argument
        of the function. If the path argument is an absolute path the path is returned.

        :param path: The path that should be joined with the backends location.
        """
        if os.path.isabs(path):
            return path
        return os.path.join(self.location, path)

    def open(self, name, **kwargs):
        raise NotImplementedError

    def exists(self, name):
        raise NotImplementedError

    def save(self, name, data):
        raise NotImplementedError


class FilesystemStorageBackend(BaseStorageBackend):
    """
    A storage engine that uses Python built in filesystem functionality.
    """

    def __init__(self):
        super(FilesystemStorageBackend, self).__init__()
        if not os.path.exists(self.location):
            makedirs(self.location, exist_ok=True)

    def open(self, name, mode='rb', encoding=None, errors='strict'):
        return codecs.open(self.path(name), mode=mode, encoding=encoding, errors=errors)

    def exists(self, name):
        return os.path.exists(self.path(name))

    def save(self, name, data):
        if not os.path.exists(os.path.dirname(self.path(name))):
            makedirs(os.path.dirname(self.path(name)), exist_ok=True)

        with open(self.path(name), 'wb') as f:
            f.write(data)
