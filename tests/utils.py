# -*- coding: utf-8 -*-


def has_django():
    try:
        import django  # noqa isort:skip
        return True
    except ImportError:
        return False


def has_pillow():
    try:
        from PIL import Image
        return True
    except ImportError:
        return False
