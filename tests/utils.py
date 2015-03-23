# -*- coding: utf-8 -*-
import importlib


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
