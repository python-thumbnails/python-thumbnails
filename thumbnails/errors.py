# -*- coding: utf-8 -*-


class ThumbnailError(Exception):
    def __init__(self, message, exception=None):
        super(ThumbnailError, self).__init__(message)
        self.exception = exception
